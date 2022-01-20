# Container image that runs your code
FROM python:alpine

RUN pip install bump2version

COPY entrypoint.sh /entrypoint.sh
COPY bump-version.py /bump-version.py

#ENTRYPOINT ["python" ,"bump-version.py"]
ENTRYPOINT ["/entrypoint.sh"]
