

def has_key(dictionary, *args):
    """Check if dictionary has key (and child key)

    Arguments:
        dictionary {dict} -- Dictionary need check

    Returns:
        Boolean -- False if key do not exist, True otherwise
    """

    check_object = dictionary
    for key in args:
        check_object = check_object.get(key)
        if check_object is None:
            return False

    return True


def has_keys(dictionary, *keys_list):
    for keys in keys_list:
        if not has_key(dictionary, *keys):
            return False, keys

    return True, []
