FROM tiangolo/uwsgi-nginx-flask:python3.9.5
WORKDIR ./
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk --no-cache
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
ENTRYPOINT [ "python" ]
CMD ["flask", "python"]