FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PORT=3002
ENV INFOBACKEND_URL=http://127.0.0.1:3001
EXPOSE 3002
WORKDIR /code
COPY requirements.txt /code/
RUN python3 -m pip install -r requirements.txt
COPY . /code/
#ENTRYPOINT VS CMD, do not do it, remote debbuging doesnt work
#ENTRYPOINT exec python3 /code/taskbackend/manage.py runserver 0.0.0.0:${PORT}
CMD exec python3 /code/taskbackend/manage.py runserver 0.0.0.0:${PORT}

