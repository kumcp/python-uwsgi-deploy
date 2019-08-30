

def validate_extension_name(filename, allow_extensions):
    """Validate extension is in alloe_extensions or not

    Arguments:
        filename {string} -- filename checking
        allow_extensions {[string]} -- list allowed extensions

    Raises:
        ValueError: filename does not have extension
        ValueError: File extension is not valid
    """

    if "." not in filename:
        raise ValueError("filename does not include extension")

    if filename.rsplit(".", 1)[1].lower() not in allows_extensions:
        raise ValueError("file extension is not valid")
