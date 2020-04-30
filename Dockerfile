FROM python:3

RUN adduser --shell /home/cq/CryptoCurses.py --gecos "CryptoCurses user" --disabled-password cq
RUN passwd -d cq

COPY ./CryptoCurses.py /home/cq/
COPY ./CryptoQuote/CryptoQuote.py /home/cq/CryptoQuote/

RUN chown -R cq:cq /home/cq/
RUN chmod +x /home/cq/CryptoCurses.py

RUN apt-get update && apt-get install -y openssh-server fail2ban && rm -rf /var/lib/apt/lists/*

RUN sed -i.bak 's/#PermitEmptyPasswords no/PermitEmptyPasswords yes/g' /etc/ssh/sshd_config
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/g' /etc/ssh/sshd_config
RUN echo 'Protocol 2' >> /etc/ssh/sshd_config
RUN sed -i.bak 's/nullok_secure/nullok/' /etc/pam.d/common-auth
RUN sed -i.bak '/backend/c\backend = systemd' /etc/fail2ban/jail.conf

CMD service ssh start && service fail2ban start && bash

EXPOSE 22/tcp
