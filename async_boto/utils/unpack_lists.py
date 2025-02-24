from typing import List, Any


def unpack_lists(list_: List[Any]) -> List[Any]:
    unpacked_list = []
    for item in list_:
        if isinstance(item, list):
            unpacked_list.extend(unpack_lists(item))
            continue
        unpacked_list.append(item)
    return unpacked_list
