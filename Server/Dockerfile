FROM python:3

RUN mkdir application

COPY ./app.py application/app.py

WORKDIR application



EXPOSE 8081

RUN pip install flask

CMD ["python3","./app.py"]
