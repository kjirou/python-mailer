# coding: utf8
import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate

__version__ = '1.0.0'


class Mailer(object):

    def __init__(
        self, from_addr, to_addrs, encoding='iso-2022-jp',
        smtp_server='localhost:25'
    ):
        self._from_addr = from_addr
        self._to_addrs = to_addrs
        self._encoding = encoding
        self._smtp_server = smtp_server

    def _create_message(self, subject, body):
        u''' subject/body are unicode only'''
        subject_str = subject.encode(self._encoding)
        body_str = body.encode(self._encoding)

        message = MIMEText(body_str, 'plain', self._encoding)
        message['Subject'] = Header(subject_str, self._encoding)
        message['From'] = self._from_addr
        message['To'] = self._to_addrs[0]
        message['Date'] = formatdate()
        return message

    def send(self, subject, body):
        smtp = smtplib.SMTP(self._smtp_server)
        message = self._create_message(subject, body)
        smtp.sendmail(self._from_addr, self._to_addrs, message.as_string())
        smtp.close()
