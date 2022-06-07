from typing import Optional
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

_SCOPES = ["https://mail.google.com/"]  # Scope for IMAP

_credentials_cache: Optional[Credentials] = None


def get_access_token(authorized_user_file: str, cache: bool = False) -> str:
    global _credentials_cache
    if _credentials_cache is not None and cache:
        credentials = _credentials_cache
    else:
        credentials = get_credentials(authorized_user_file)
    credentials = ensure_nonexpired(
        credentials, authorized_user_file=authorized_user_file
    )
    if cache:
        _credentials_cache = credentials
    return credentials.token


def get_credentials(authorized_user_file: str) -> Credentials:
    return Credentials.from_authorized_user_file(authorized_user_file, _SCOPES)


def get_authorized_user_file(
    client_secret_file: str, output_file: str, port: int = 0
) -> None:
    flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, _SCOPES)
    credentials = flow.run_local_server(port=port)
    _save_credentials(credentials, authorized_user_file=output_file)


def ensure_nonexpired(
    credentials: Credentials, authorized_user_file: Optional[str] = None
) -> Credentials:
    if credentials.expired:
        if not credentials.refresh_token:
            raise ValueError("Refresh token is not available")
        credentials.refresh(Request())
        if authorized_user_file:
            _save_credentials(credentials, authorized_user_file=authorized_user_file)
    return credentials


def _save_credentials(credentials: Credentials, authorized_user_file: str) -> None:
    with open(authorized_user_file, "w") as file:
        file.write(credentials.to_json())
