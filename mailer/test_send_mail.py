# coding: utf8

#
# Usage:
#   python test_send_mail.py from@email to@email
#
import sys
from mailer import Mailer

args = sys.argv[1:]

FROM_EMAIL = args[0]
TO_EMAIL = args[1]

if __name__ == '__main__':
    mailer = Mailer(FROM_EMAIL, [TO_EMAIL])
    mailer.send(
        u'件名ですケンメイです',
        u'本文です\nホンブンです\nほんぶんです'
    )
