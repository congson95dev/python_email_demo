# python_email_demo

### test smtp email:

https://www.gmass.co/smtp-test

---

### email template html example:

https://github.com/leemunroe/responsive-html-email-template/blob/master/email.html

---

### send email in queue by redis

install redis on local:

`sudo apt-get install redis`

install venv:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

create redis worker:

`python3 worker.py`

send mail:

`python3 main.py`

after that, it will send email to you.

---

alternative, we could install redis and redis worker by `docker-compose`

https://github.com/testdrivenio/flask-ses-rq/blob/master/docker-compose.yml#L37

for docker run, replace `redis_url` with `redis_url` of docker, then run:

`docker compose up --build -d`

after that, it will send email to you.