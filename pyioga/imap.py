def get_auth_string(username: str, access_token: str) -> str:
    return "user={}\1auth=Bearer {}\1\1".format(username, access_token)
