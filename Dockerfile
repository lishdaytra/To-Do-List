FROM python:3.11.6

SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash todo && chmod 777 /opt /run

WORKDIR /todo

RUN mkdir /todo/static && chown -R todo:todo /todo && chmod 755 /todo

COPY --chown=todo:todo . .

RUN pip install -r requirements.txt

USER todo

CMD ["gunicorn","-b","0.0.0.0:8001","core.wsgi:application"]
