FROM python:3

ENV PYTHONUNBUFFERED 1

# add app
COPY . /app

# set working directory
WORKDIR /app

# install requirements
RUN pip install -r requirements.txt

# run server
CMD gunicorn -b 0.0.0.0:5000 manage:app