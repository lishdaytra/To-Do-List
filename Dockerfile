FROM python:3.11.6



# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip



RUN useradd -rms /bin/bash todo && chmod 777 /opt /run

RUN mkdir /ToDoList

WORKDIR /ToDoList

ADD . /ToDoLits/

RUN mkdir /ToDoList/static && chown -R todo:todo /ToDoList && chmod 755 /ToDoList

COPY --chown=todo:ToDoLits . .

RUN pip install -r requirements.txt

USER todo

CMD ["gunicorn","-b","0.0.0.0:8001","core.wsgi:application"]
