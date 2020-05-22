FROM python:3.7.6-slim

COPY requirements.txt requirements.txt 

ENV BUILD_DEPS="python-dev build-essential gcc iputils-ping" \ 
    PYTHON_DEPS="cython numpy"

RUN apt-get update \
    && apt-get install -y ${BUILD_DEPS} --no-install-recommends \
    && pip install --upgrade pip \
    && pip install ${PYTHON_DEPS} \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python preload.py
RUN  chmod +x start.sh 

EXPOSE 80
CMD ["sh", "./start.sh"]
