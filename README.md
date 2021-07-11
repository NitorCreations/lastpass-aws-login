# `lastpass-aws-login`: AWS LastPass SAML CLI

[![PyPI version](https://badge.fury.io/py/lastpass-aws-login.svg)](https://badge.fury.io/py/lastpass-aws-login)
[![Codeship Status for NitorCreations/lastpass-aws-login](https://app.codeship.com/projects/c0fb24eb-34be-4ec3-ae3b-5254134b44c9/status?branch=master)](https://app.codeship.com/projects/442687)

Tool for using AWS CLI with LastPass SAML.

LastPass code from here: https://github.com/omnibrian/aws-lp, SAML and profile management code mostly from here: https://github.com/NitorCreations/adfs-aws-login

## Installation

This tool is published on pypi.org:

```
pip install lastpass-aws-login
```

## Usage

You will need to look up your SAML configuration ID for the AWS role you wish to join. This is in the generated launch URL in the LastPass console, it will look something similar to `https://lastpass.com/saml/launch/cfg/25`. In this case, the configuration ID is `25`, enter this number into the configuration

## Run

The executable is called `lastpass-aws-login`. Log in with default profile by simply running `lastpass-aws-login` or specify a profile with `lastpass-aws-login --profile [profile]`. 

See `lastpass-aws-login -h` for more options.

If the environment variable `LASTPASS_DEFAULT_PASSWORD` is defined, that will be used as the password.

## Configure

Configure the profiles in `$HOME/.aws/config`. Following is an example with all supported configuration keys (and a few aws default ones):
```
[profile example]
region=us-east-1
output=json
lastpass_default_username=test.user@example.com
lastpass_role_arn=arn:aws:iam::1234567890:role/DeployRole
lastpass_session_duration=8
lastpass_saml_id=25
```
