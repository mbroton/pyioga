<div id="top"></div>



<!-- 
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
  -->

<h3 align="center">Pyioga</h3>

  <p align="center">
    Python IMAP OAuth2 Gmail Authenticator Helper
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This project helps to setup Google OAuth2 authentication for IMAP connection with Gmail.

If you want to read emails from Gmail in your automated E2E tests or scripts, you're in a right place!

This project is built to guide you through the process. Pyioga is an additional layer built on Google authentication libraries to make it easy.


## Getting Started

### Google account setup

First, start with setting up google account.

### Pyioga installation

Install package using pip

```
pip install pyioga
```

Generate token file, based on downloaded client secrets file

```
pyioga --client-secret-file client_secrets.json --output-file token.json
```

You are ready to go!

## Usage

Assuming you went through installation and you have client secrets file and token file (also known as "authorized user file") you can acquire token used for IMAP authentication.


<p align="right">(<a href="#top">back to top</a>)</p>