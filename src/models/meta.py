from functools import cache

from sqlalchemy import MetaData


@cache
def get_metadata() -> MetaData:
    return MetaData()


metadata = get_metadata()
