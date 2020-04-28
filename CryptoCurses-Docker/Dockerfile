FROM python:3

RUN adduser -s /home/cq/CryptoCurses.py -c "CryptoCurses user" cq
RUN passwd -d cq

COPY --chown cq:cq ./CryptoCurses.py /home/cq/
COPY --chown cq:cq ./CryptoQuote/CryptoQuote.py /home/cq/CryptoQuote/

RUN chmod +x /home/cq/CryptoCurses.py

RUN apt update && apt install -y openssh-server && rm -rf /var/lib/apt/lists/*

RUN sed -i.bak 's/#PermitEmptyPasswords no/PermitEmptyPasswords yes/g' /etc/ssh/sshd_config
RUN sed -i.bak 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config

RUN service ssh restart

EXPOSE 22/tcp
