from flask import jsonify


def simple_response(http_code, result_code, message):
    """Handle simple response for API result

    Arguments:
        http_code {int} -- http code for the message
        result_code {str} -- result code of an action.
        message {str} -- detail message

    Returns:
        dict -- json response
    """
    return jsonify({
        "code": http_code,
        "result_code": result_code,
        "message": message
    }), http_code


def responseFileNotFound(message, result_code="FILE_NOT_FOUND"):
    return simple_response(404, result_code, message)


def responseBadRequest(message, result_code="BAD_REQUEST"):
    return simple_response(400, result_code, message)


def responseUnauthorized(message, result_code="UNAUTHORIZED"):
    return simple_response(401, result_code, message)


def responseForbidden(message, result_code="FORBIDDEN"):
    return simple_response(403, result_code, message)


def responseSuccess(message, result_code="OK"):
    return simple_response(200, result_code, message)


def responseCreated(message, result_code="CREATED"):
    return simple_response(201, result_code, message)
