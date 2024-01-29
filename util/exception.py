class RichCannotRequest(Exception):
    """
    Rich Cannot Request
    """


class RichRequestNotSuccess(Exception):
    """
    Rich Request is not 200
    """


class RichCannotParseJSON(Exception):
    """
    Rich cannot parse a json which given to it
    """


class RichConfigNotFound(Exception):
    """
    Rich Config Not Found
    """

class RichConfigError(Exception):
    """
    Rich Config Erorr
    """