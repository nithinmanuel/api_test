FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# set up work directory
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/
EXPOSE 8000
ENTRYPOINT ["python", "sample_project/manage.py"]
CMD ["runserver", "127.0.0.1:8000"]

