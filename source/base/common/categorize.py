
from .string_handle import include_items


def categorize(item, category_map, matching_func):
    """HOF which create categorize function by checking an item
    in a category_map is valid with matching_func or not

    Arguments:
        item {any} -- item need to be categorized
        category_map {dict} -- category map. It should be a dict with
                                key and value is all item in the list
        matching_func {lambda item, category_items} -- matching function
                                        define when is the valid

    Returns:
        str -- category group key name
    """

    for key in sorted(category_map.keys()):
        if matching_func(item, category_map[key]):
            return key

    return None


def categorize_include(item, category_map):
    """return category_key if item has keys included in category map (take first)

    Arguments:
        item {*} -- item need categorizing
        category_map {dict} -- category map

    Returns:
        str -- category_key or None
    """

    return categorize(item, category_map, include_items)


def categorize_exact(item, category_map):
    """return category_key if item in category map

    Arguments:
        item {*} -- item need categorizing
        category_map {dict} -- category map

    Returns:
        str -- category_key or None
    """

    def exact_logic(item, category_list): return item in category_list

    return categorize(item, category_map, exact_logic)
