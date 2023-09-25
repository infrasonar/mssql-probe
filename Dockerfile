FROM python:3.9
ADD . /code
WORKDIR /code
RUN echo -e "\
\n\
[provider_sect]\n\
default = default_sect\n\
legacy = legacy_sect\n\
\n\
[default_sect]\n\
activate = 1\n\
\n\
[legacy_sect]\n\
activate = 1\
" >> /etc/ssl/openssl.cnf
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
