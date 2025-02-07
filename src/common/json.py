import ujson


def loads(val: str):
    return ujson.loads(val)


def dump(
    val,
    **kwargs,
) -> bytes:
    return ujson.dumps(val, **kwargs).encode("utf-8")


def dumps(
    val,
    **kwargs,
) -> str:
    return dump(val, **kwargs).decode("utf-8")
