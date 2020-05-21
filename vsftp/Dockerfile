FROM ubuntu:18.04
MAINTAINER Armands
RUN apt-get update
RUN apt-get install -y vsftpd
#RUN systemctl start vsftpd\ 
#RUN systemctl enable vsftpd\
#RUN ufw allow 20/tcp\
#	&& ufw allow 21/tcp\
COPY vsftpd.conf /etc/vsftpd/vsftpd.conf
COPY vsftpd.userlist /etc/vsftpd.userlist
#RUN systemctl restart vsftpd\ 
