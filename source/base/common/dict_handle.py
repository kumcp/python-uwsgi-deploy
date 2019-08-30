from .validate import has_key


def summary_list_dict(*dict_list):
    """Compute list dict with the sum of all key

    Ex:
    summary_list_dict([
        { "time": 1, "amount": 2},
        { "time": 2, "amount": 3},
        { "time": 3, "amount": 4},
    ]) -> { "time": 6 , "amount": 9 }


    Returns:
        [type] -- [description]
    """
    def summary_compute(prev, current):
        for key in current:
            if prev.get(key) is not None:
                prev[key] = prev[key] + current[key]
            else:
                prev[key] = current[key]

        return prev

    return compute_list_dict(summary_compute, *dict_list)


def compute_list_dict(func, *dict_list):
    """Compute a list of dictionary to get the result

    Ex:

    compute_list_dict(lambda prev,
        curr: { "amount": prev["amount"] + curr["amount"] },
        { "time": 1, "amount": 2},
        { "time": 2, "amount": 3},
        { "time": 3, "amount": 4},
    ) -> { "time": 6 , "amount": 9 }

    Arguments:
        func {fuction} -- Computing function

    Returns:
        dict -- Computed result after run through the list dict
    """
    result = {}

    for curr_dict in dict_list:
        result = func(result, curr_dict)

    return result


def map_dict(dict_object, mapping_table):
    """Mapping a dict to another dict with different keys in mapping_table

    Arguments:
        dict_object {dict} -- Source dictionary
        mapping_table {dict} -- keys and values are string
                                which represent for new keys set

    Returns:
        dict -- New dict with new key/value set
    """
    return {key: dict_object[val] for key, val in mapping_table.items()}


def map_list_dict(list_dict_object, mapping_table):
    """Mapping a list of dict to another list of dict
    with different keys in mapping_table

    Arguments:
        list_dict_object {list} -- Source list object or dict
        mapping_table {dict} -- keys and values are string
                                which represent for new keys set

    Returns:
        list -- New list dict with new key/value set
    """
    return [map_dict(vars(item), mapping_table) for item in list_dict_object]
