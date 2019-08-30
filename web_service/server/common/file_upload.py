from flask import request, current_app


def validate_file_request(filename, request):
    """Validate file upload with the name given

    Arguments:
        filename {str} -- file name need validate
        request {flask.request} -- flask request object

    Returns:
        file {FileStorage} -- File object storing data

    Raise:
        ValueError: Filename upload has some problems
        AttributeError: Filename cannot be found.
    """

    if filename not in request.files:
        raise AttributeError("You have not select the file yet.")

    file = request.files.get(filename)

    if file.filename == "":
        raise ValueError("No selected file.")

    if not (file and allowed_file(file.filename)):
        raise ValueError("File extension is not allowed.")

    return file


def allowed_file(filename):
    """Check if file upload has the allowed extensions or not

    NOTE: This function only check for extension in file name,
    so it may not guaranteer to be secured yet, but okay for now.

    Arguments:
        filename {str} -- File name need to check

    Returns:
        Boolean -- Allowed file or not
    """

    allows_extensions = current_app.config["ALLOWED_EXTENSIONS"]

    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in allows_extensions
