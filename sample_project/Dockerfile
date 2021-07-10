FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# set up work directory
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
ENTRYPOINT ["python", "/code/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]



