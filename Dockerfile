FROM python:3

RUN adduser --shell /home/cq/CryptoCurses.py --gecos "CryptoCurses user" --disabled-password cq
RUN passwd -d cq

COPY ./CryptoCurses.py /home/cq/
COPY ./CryptoQuote/CryptoQuote.py /home/cq/CryptoQuote/

RUN chown -R cq:cq /home/cq/
RUN chmod +x /home/cq/CryptoCurses.py

RUN apt update && apt install -y openssh-server && rm -rf /var/lib/apt/lists/*

RUN sed -i.bak 's/#PermitEmptyPasswords no/PermitEmptyPasswords yes/g' /etc/ssh/sshd_config
RUN sed -i.bak 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config

CMD service ssh start && bash

EXPOSE 22/tcp
