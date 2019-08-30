

def remove_multi_space(str):
    return ' '.join(str.split())


def remove_space(str):
    return "".join(str.split())


def filter_empty_string(str_list):
    return [str_item for str_item in str_list if len(str_item) > 0]


def include_items(initial_string, list_compare):
    """Check if initial_string contains one of the word in list_compare

    Arguments:
        initial_string {str} -- String need to check
        list_compare {list} -- list of words will match to group

    Returns:
        Boolean -- Result True or False.
    """
    for item in filter_empty_string(list_compare):
        item = item.strip()
        if item in initial_string and item != '':
            return True

    return False
