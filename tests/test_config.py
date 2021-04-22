from lastpass_aws_login import conf
import pytest
import argparse

try:
    # For Python 3.5 and later
    import configparser
except ImportError:
    # Fall back to Python 2
    import ConfigParser as configparser  # noqa: F401

args = {
    "profile": "test-profile",
    "user": "test@example.com",
    "no_prompt": False,
    "duration": None,
    "role": None,
    "verbose": None,
    "saml_id": None,
}

params = {
    "lastpass_role_arn": "arn:aws:iam::123456789012:role/test_role",
    "lastpass_saml_id": "12345",
    "lastpass_default_username": "test@example.com",
}

sections = {"profile test-profile": params}


def test_init_no_profile_found(args_patched):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        config = conf.init()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1
    assert args_patched.call_count == 1


def test_init(args_patched, aws_config_patched):
    config = conf.init()
    for mock in aws_config_patched:
        mock.call_count == 1
    args_patched.call_count == 1
    _verify_config(args, params)


def _verify_config(args, params):
    config = conf.init()
    assert config.PROFILE == args["profile"]
    assert config.CONFIG_PROFILE == "profile {}".format(args["profile"])
    assert config.ROLE_ARN == params["lastpass_role_arn"]
    assert config.NO_PROMPT == args["no_prompt"]


@pytest.fixture
def args_patched(mocker):
    return mocker.patch(
        "argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(**args)
    )


@pytest.fixture
def aws_config_patched(mocker):
    mock1 = mocker.patch("configparser.ConfigParser.__getitem__", return_value=params)
    mock2 = mocker.patch("configparser.ConfigParser.read", return_value=None)
    mock3 = mocker.patch("configparser.ConfigParser.has_section", return_value=True)
    return mock1, mock2, mock3
