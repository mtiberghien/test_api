def get_method(param=None):
    message = "query parameter was not defined" if param is None else "query parameter is '{}'".format(param)
    return dict(message=message)


def set_method(body):
    param_1 = body.get("param_1")
    param_2 = body.get("param_2")
    return dict(message="{} + {} = {}".format(param_1, param_2, param_1 + param_2))
