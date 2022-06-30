FROM python:3.10-slim
RUN apt-get update
RUN apt install bash
WORKDIR /app
ENV PATH /usr/local/bin:/Tmp:$PATH
COPY requirements.txt /app
RUN python3 -m pip install -r requirements.txt
COPY *.py /app
COPY Scores.txt /tmp
COPY /templates  /app/templates
ENTRYPOINT ["python", "MainGame.py"]