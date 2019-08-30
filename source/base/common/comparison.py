

def compare_content(item1, item2):
    return item1 == item2


def compare_content_list(list1, list2, compare_order=True):
    """Compare 2 list if content is already inside other list or not

    list1 = [1,2,3]
    list2 = [1,2,3]
    list 3 = [3,1,2]
    list4 = [1,2,3,1]
    -> compare_content_list(list1, list2) == True
    -> compare_content_list(list1, list3) == False
    -> compare_content_list(list1, list3, False) == True

    NOTE: if compare_order is False, list will not care about
    the duplicate item, so 2 items have the same value will be treated
    as 1 item, but if compare_order is True the number of item will be checked


    Arguments:
        list1 {[type]} -- [description]
        list2 {[type]} -- [description]

    Keyword Arguments:
        compare_order {bool} -- Take order to compare or not (default: {True})

    Returns:
        Boolean -- Result compare 2 lists
    """

    if compare_order:
        result = [item for index, item in enumerate(
            list1) if item == list2[index]]
    else:
        result = [item for item in list1 if item in list2]

    return len(result) == len(list2) and len(list1) == len(list2)


def compare_content_dict(dict1, dict2, list_order=False):

    if type(dict1) is list:
        return compare_content_list(dict1, dict2, list_order)

    if type(dict1) is dict:
        for key in dict1:
            if not compare_content_dict(dict1[key], dict2[key]):
                return False

        return True

    return compare_content(dict1, dict2)
