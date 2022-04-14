# Container image that runs your code
FROM python:alpine

RUN pip install bump2version && apk add git

COPY bump-version.py /bump-version.py

RUN bump2version --version && git --version

ENTRYPOINT ["python" ,"/bump-version.py"]
