FROM python:3.8
USER root
RUN mkdir /app
COPY . /app/
WORKDIR /app/
RUN pip3 install -r requirements.txt
ENV AIRFLOW_HOME='/app/airflow'
ENV AIRFLOW_COR_DAGBAG_IMPORT_TIMEOUT='1000'
ENV AIRFLOW_COR_ENABLE_ZCOM_PICKLING='True'
ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN='sqlite:////app/airflow/airflow.db'
RUN airflow db init
RUN airflow users create -e darshanrokkad2003@gmail.com -f darshan -l rokkad -p admin -r Admin -u admin
RUN chmod 777 start.sh
RUN apt update -y
ENTRYPOINT [ "/bin/sh" ]
CMD [ "start.sh" ]