<div id="top"></div>

<h3 align="center">Pyioga</h3>

  <p align="center">
    Python IMAP OAuth2 Gmail Authenticator Helper
  </p>
</div>

## About The Project

This project helps to setup Google OAuth2 authentication for IMAP connection with Gmail.

If you want to read emails from Gmail in your automated E2E tests or scripts, you're in a right place!

This project is built to guide you through the process. Pyioga is an additional layer built on Google authentication libraries to make it easy.


## Getting Started

### Google account setup

* Go to [GCP Credentials page](https://console.cloud.google.com/apis/credentials)
* Create credentials -> OAuth Client ID -> Web Application
* Add authorized redirect URI "http://localhost/" (trailing slash is important!)
* Download credentials json file (client secrets)

### Pyioga installation

Install package using pip

```
pip install pyioga
```

Generate token file, based on downloaded client secrets file. During this step a web browser is going to pop up with request for permissions.

```
pyioga init --client-secret-file <path to client secrets file> --output-file <path e.g. token.json>
```

Having token file, you are ready to go!

## Usage

Assuming you went through installation and you have token file (also known as "authorized user file") you can use it to authenticate IMAP connections, using pyioga's functions.

Example with Python's builtin library imaplib
```py3
import imaplib
import pyioga

username = "user@gmail.com"
access_token = pyioga.get_access_token("token.json")
client = imaplib.IMAP4_SSL(host="imap.gmail.com")
client.authenticate("XOAUTH2", authobject=lambda x: pyioga.get_auth_string(username, access_token))
# ('OK', [b'user@gmail.com authenticated (Success)'])
```

Example with [imap-tools](https://github.com/ikvk/imap_tools)
```py3
import pyioga
from imap_tools import MailBox, AND

username = "user@gmail.com"
access_token = pyioga.get_access_token("token.json")
with MailBox('imap.gmail.com').xoauth2(username, access_token) as mailbox:
    for msg in mailbox.fetch():
        print(msg.date, msg.subject, len(msg.text or msg.html))
```

`pyioga.get_access_token` is ensuring you will receive a valid token - otherwise it should raise an exception.

<p align="right">(<a href="#top">back to top</a>)</p>