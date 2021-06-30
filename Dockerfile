FROM python:3.8.7-slim-buster

EXPOSE 80

COPY ./app /app

WORKDIR /app

RUN pip install -r requirements.txt

ARG buildtime_variable = "HostName=airq-iot-hub2.azure-devices.net;SharedAccessKeyName=airq-iot-hub-sap;SharedAccessKey=FNcFeMKvaqfNV0Y2TbhzsheTF9QU67Koe5+F9k+Gm/Q="
ENV CONNECTION_STRING =$buildtime_variable

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

