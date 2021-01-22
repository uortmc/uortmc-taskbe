FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PORT=8000
EXPOSE 8000
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ENTRYPOINT exec python3 /code/taskbackend/manage.py runserver 0.0.0.0:${PORT}

