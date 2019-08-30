from os import listdir


def list_file(folder_path, filters):
    """Get list of file items/folder in a folder path

    Arguments:
        folder_path {string} -- folder_path need to check
        filters {tuple|string} -- extension|string for filter ending

    Returns:
        tuple -- list of item in folder
    """
    return [item for item in listdir(folder_path) if item.endswith(filters)]
