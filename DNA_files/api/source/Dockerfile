# Dockerfile

# pull the official docker image
FROM python:3.11.1-slim

# set work directory


# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY DNA_files/api/source/requirements.txt .
RUN pip install -r requirements.txt

#COPY api_docker/app /app 

WORKDIR /app/src


CMD [ "uvicorn", "main:app",  "--host", "0.0.0.0", "--port", "80" ]
#CMD ["python", "app/src/inf.py"] 
