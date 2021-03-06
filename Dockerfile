FROM python:3.9.2-slim
ENV PORT=5000
ENV VERSION=v1.0
ENV DEBUG="false"
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y curl
RUN pip3.9 install flask
RUN pip3.9 install gitpython
RUN git clone https://github.com/srishkalra/mywebproject.git
WORKDIR mywebproject
RUN chmod u+x myapp.py
CMD ["python", "myapp.py"]
