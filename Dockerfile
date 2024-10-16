FROM python:3.12
WORKDIR /sumup_challenge
COPY . /sumup_challenge/
RUN pip install -r requirements.txt
