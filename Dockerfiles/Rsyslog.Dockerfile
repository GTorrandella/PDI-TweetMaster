FROM rsyslog/syslog_appliance_alpine:latest

COPY ./rsyslog.conf /etc/rsyslog.conf