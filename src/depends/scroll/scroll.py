from dataclasses import dataclass
from enum import Enum

import sqlalchemy as sa
from fastapi import Query


SCROLLABLE_MAX_LIMIT: int = 100


class ScrollDirection(str, Enum):
    ASC = "asc"
    DESC = "desc"


@dataclass
class ScrollColumn:
    name: str
    direction: ScrollDirection

    def __str__(
        self
    ) -> str:

        if self.direction == ScrollDirection.DESC:
            prefix = "-"
        else:
            prefix = ""
        return f"{prefix}{self.name}"


@dataclass
class Scroll:
    limit: int
    offset: int
    available: list[str]
    current: list[ScrollColumn]

    def get(
        self,
        column: str
    ) -> ScrollColumn | None:
        return next((
            item for item in self.current
            if item.name == column
        ), None)

    def add(
        self,
        column: str,
        direction: ScrollDirection = ScrollDirection.ASC
    ) -> None:

        # Проверяем
        if self.get(column):
            return

        # Добавляем столбец в список сортировки
        self.current.append(ScrollColumn(
            name=column,
            direction=direction
        ))

    def apply(
        self,
        q: sa.sql.Select
    ):

        q_sub = q.alias("scr")
        q_scr = sa.select(q_sub)

        # Сортировка
        for column in self.current:
            if (col := q_sub.columns.get(column.name)) is None:
                continue
            if column.direction == ScrollDirection.ASC:
                order = col.asc()
            elif column.direction == ScrollDirection.DESC:
                order = col.desc()
            q_scr = q_scr.order_by(order)

        # Пагинация
        return q_scr.limit(self.limit).offset(self.offset)


class ScrollDepend(type):

    def __new__(
        cls,
        available: list[str]
    ):

        # Сортировка
        param_sort = None
        if available:
            param_sort = Query(
                None,
                description="Сортировка: " + ", ".join((
                    f"__{item}__"
                    for item in available
                ))
            )

        def call_with_sort(
            self,
            limit: int = Query(
                SCROLLABLE_MAX_LIMIT,
                description="Количество строк",
                le=SCROLLABLE_MAX_LIMIT,
                ge=1
            ),
            offset: int = Query(
                0,
                description="Смещение первой строки",
                ge=0
            ),
            sort: str | None = param_sort
        ) -> Scroll:

            # Сортировка
            sort_ = list()
            if sort:
                for col in sort.split(","):
                    if col.startswith("-"):
                        col_ = ScrollColumn(col[1:], ScrollDirection.DESC)
                    else:
                        col_ = ScrollColumn(col, ScrollDirection.ASC)
                    if col_.name in available:
                        sort_.append(col_)

            # Возвращаем сортировку
            return Scroll(
                limit=limit,
                offset=offset,
                available=available,
                current=sort_
            )

        def call_wo_sort(
            self,
            limit: int = Query(
                SCROLLABLE_MAX_LIMIT,
                description="Количество строк",
                le=SCROLLABLE_MAX_LIMIT,
                ge=1
            ),
            offset: int = Query(
                0,
                description="Смещение первой строки",
                ge=0
            )
        ) -> Scroll:
            return Scroll(
                limit=limit,
                offset=offset,
                available=[],
                current=[]
            )

        # Выбираем функцию пагинации
        call = {
            True: call_with_sort,
            False: call_wo_sort
        }[param_sort is not None]

        # Возвращаем объект с нужной функцией
        inst = super().__new__(
            cls,
            cls.__name__,
            tuple(),
            {"__call__": call}
        )
        return inst()
