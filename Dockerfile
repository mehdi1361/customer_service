FROM python
RUN apt upgrade
RUN apt update


COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN apt-get install -y nano
RUN apt install -y cron
COPY . .
COPY ./customer/management/commands/run_command.txt /etc/cron.d/
RUN chmod 644 /etc/cron.d/run_command.txt
RUN crontab /etc/cron.d/run_command.txt
RUN touch /var/log/cron.log

#ENV PORT 8000
#EXPOSE 8000
