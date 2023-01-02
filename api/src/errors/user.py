class UserNotFoundError(Exception):
    """Raises when a user is not found"""


class UserBadCredentials(Exception):
    """Raises when bad credentials was provided"""
