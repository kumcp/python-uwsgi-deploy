

def filter_dict_by_keys(dic, list_keys):
    """Filter dictionary by keys in list_keys only

    Arguments:
        dic {dict} -- dictionary
        list_keys {list} -- list string key

    Returns:
        dict -- new dictionary contain only keys
    """

    return {key: dic[key] for key in list_keys}


def filter_list_exclude_keys(dic, list_keys):
    """Filter dictionary by key not in list_keys

    Arguments:
        dic {dict} -- dictionary
        list_keys {list} -- list string key

    Returns:
        dict -- new dictionary not contain key in list_keys
    """

    return {key: dic[key] for key in dic.keys() if key not in list_keys}


def filter_dict(dic, filter_func):
    """Filter dictionary with a function receive key, value

    Arguments:
        dic {dict} -- dictionary
        filter_func {lambda key, value} -- filter function

    Returns:
        dict -- new dictionary with some keys valid
    """

    return {key: dic[key] for key in dic.keys() if filter_func(key, dic[key])}


def transform_list_dict(list_keys, list_values):
    """Transform list keys and list values into a dictionary with the match index

    Arguments:
        list_keys {list} -- list keys string (unique)
        list_values {list} -- list values following index

    Returns:
        dict -- dictionary have information from list_keys and list_values
    """

    return {
        key: list_values[index] for index, key in enumerate(list_keys) if index < len(list_values)
    }


def get_value_list(dic, key_list=None):
    """Get values as a list from a dictionary.
    The result will be in order or key_list

    Arguments:
        dic {dict} -- a dictionary
        key_list {list} -- key list of dictionary

    Returns:
        list -- list of values has order in key_list
    """

    if key_list is None:
        return list(dic.values())

    return [dic[key] for key in key_list]


def get_deep_value_dict(deep_dict):
    """Get deep values from a dictionary

       Arguments:
           deep_dict {dict} -- a dictionary

           {'Total access': {'2019/03/19': 1, '2019/03/20': 1, '2019/03/15': 2}}

       Returns:
           list -- list of deep values
       """
    arr_result = []
    for key, value in deep_dict.items():
        for value_deep in value.values():
            arr_result.append(value_deep)
    return arr_result


def convert_dict_data(data_analyze):
    """convert data from list to dict with first element of each item in list data as key
         Arguments:
            data_analyze {list} -- input list
        Returns:
            category_dict -- get first element of each item in list data as key
            category_dict={"order": ["order", "want", "need"]}

    """
    category_dict = {}
    for index, line in enumerate(data_analyze):
        category_dict[line[0].lower().strip()] = line

    return category_dict
