
def remove_duplicate(list_data):
    """Remove duplicate items in a list
    
    Arguments:
        list_data {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """

    return list(dict.fromkeys(list_data))


def merge_unique(*arr_list):
    """Merge a list of array into 1 array which have unique items only

    Returns:
        [type] -- [description]
    """

    result = []

    for arr in arr_list:
        result = remove_duplicate(result + arr)

    return result


def flatten_list(list_data):
    """Flatten a list

    Arguments:
        list_data {list}

    Returns:
        flat_list {list}
    """

    flat_list = [item for sublist in list_data for item in sublist]

    return flat_list
