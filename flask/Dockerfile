FROM python:3.9

MAINTAINER "oren sultan orensu1210@gamil.com"
 
WORKDIR /src

COPY . /src

RUN /usr/local/bin/python -m pip install --upgrade pip &pip install -r requirements.txt --no-cache-dir

EXPOSE 5000

ENTRYPOINT ["python"]

CMD [ "./MainScore.py" ]
