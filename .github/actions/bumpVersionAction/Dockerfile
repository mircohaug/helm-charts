# Container image that runs your code
FROM python:alpine

WORKDIR /work

RUN pip install bump2version && apk add git && git config --global --add safe.directory /work

COPY bump-version.py /bump-version.py

ENTRYPOINT ["python" ,"/bump-version.py"]
