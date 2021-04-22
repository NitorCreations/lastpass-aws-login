#!/bin/bash
rm -rf build dist
VERSION=$1
MESSAGE="$2"
bumpversion --new-version $VERSION --message "$MESSAGE" setup.py
python setup.py sdist bdist_wheel
gpg -o dist/lastpass_aws_login-${VERSION}-py2.py3-none-any.whl.asc -a -b dist/lastpass_aws_login-${VERSION}-py2.py3-none-any.whl
gpg -o dist/lastpass-aws-login-${VERSION}.tar.gz.asc -a -b dist/lastpass-aws-login-${VERSION}.tar.gz
twine upload dist/*