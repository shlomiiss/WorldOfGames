FROM python:3.10-slim
RUN apt-get update
RUN apt install bash
WORKDIR /app
#ENV WOG_APP=MainGame.py
ENV PATH /usr/local/bin:$PATH
COPY requirements.txt /app
RUN python3 -m pip install -r requirements.txt
COPY *.py /app
COPY Scores.txt /
COPY /templates  /app/templates
#CMD [ "python", "./MainGame.py" ]
#EXPOSE 30000
#ENTRYPOINT ["/bin/bash","tail", "-f", "/dev/null"]
ENTRYPOINT ["tail", "-f", "/dev/null"]