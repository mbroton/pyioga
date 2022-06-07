from setuptools import setup

setup(
    name="pyioga",
    version="0.1.1",
    description="Python IMAP OAuth2 Gmail Authenticator Helper",
    url="https://github.com/mbroton/pyioga",
    author="Michal Broton",
    author_email="michal@broton.dev",
    license="GPL-3.0",
    packages=["pyioga"],
    install_requires=[
        "google-api-python-client>=2.49.0",
        "google-auth>=2.6.6",
        "google-auth-oauthlib>=0.5.1",
        "google-auth-httplib2>=0.1.0",
        "click>=8.1.3",
    ],
    entry_points={
        "console_scripts": ["pyioga=pyioga.__main__:cli"],
    },
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Communications :: Email :: Post-Office :: IMAP",
    ],
)
