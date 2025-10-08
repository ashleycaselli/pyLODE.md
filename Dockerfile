ARG PYTHON_VERSION=3.14-slim
FROM python:$PYTHON_VERSION

MAINTAINER pyLODE.md Developers <https://github.com/ashleycaselli/pyLODE.md/graphs/contributors>

USER root

RUN apt-get update && \
	apt-get upgrade -y --allow-downgrades --allow-remove-essential --allow-change-held-packages

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

# copy the current directory contents
ADD . /app

WORKDIR /app

# install pyLODE.md from source, ensures we always use the latest development branch
RUN python3 setup.py install

RUN cd ./pylodemd

ENTRYPOINT ["pylodemd"]
