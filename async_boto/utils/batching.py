from typing import List, Any


def chunks(list_: List[Any], n: int):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(list_), n):
        yield list_[i : i + n]


def list_to_batches(list_: List[Any], batch_size: int) -> List[List[Any]]:
    return list(chunks(list_, batch_size))
