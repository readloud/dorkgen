FROM ubuntu:trusty
RUN apt update

RUN sudo apt-get install -y software-properties-common \
  && add-apt-repository ppa:ondrej/php \
  && apt-get update

RUN apt install -y --force-yes \
    curl \
    libcurl3 \
    libcurl3-dev \
    php5 \
    php5-cli \
    php5-curl \
    git

RUN git clone https://github.com/anonymasz/dorkgen.git
WORKDIR $PWD/SCANNER-INURLBR
RUN chmod +x inurlbr.php
RUN ln -s $PWD/inurlbr.php /usr/bin/inurlbr.php