FROM python:3

RUN mkdir Client_application

COPY ./app_client.py /Client_application/app_client.py

WORKDIR Client_application





RUN pip install requests

CMD ["python3","./app_client.py"]
