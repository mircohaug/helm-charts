# Container image that runs your code
FROM python:alpine

WORKDIR /github/workspace

RUN pip install bump2version && apk add git

COPY bump-version.py /bump-version.py

CMD sh -c 'git config --global --add safe.directory $(pwd) && python /bump-version.py'
