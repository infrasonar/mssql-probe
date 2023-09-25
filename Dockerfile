# Version must be pinned to 3.9.16; otherwise each check returns with the following error:
#   unsupported hash type md4;
FROM python:3.9.16
ADD . /code
WORKDIR /code
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]