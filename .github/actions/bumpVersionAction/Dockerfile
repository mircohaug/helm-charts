# Container image that runs your code
FROM python:alpine

WORKDIR /github/workspace

RUN pip install bump2version && apk add git && git config --global --add safe.directory /github/workspace

COPY bump-version.py /bump-version.py

ENTRYPOINT ["python" ,"/bump-version.py"]
