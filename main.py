from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib


def send_email(recipient, subject, msg):
    sender = 'Sonic269'
    password = 'bfyhbqfhuglefydz'

    server = smtplib.SMTP('smtp.yandex.ru:587')
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(msg)
        msg['Subject'] = subject
        server.sendmail(sender, recipient, msg.as_string())
        return 'Message send'
    except Exception as exception:
        return f'Check ur credentails\n{exception}'


def main():
    recipient = "Sonic144@mail.ru"
    subject = "Тест"
    msg = "Тестовое письмо"

    print(send_email(recipient, subject, msg))


if __name__ == '__main__':
    main()




















# pass = bfyhbqfhuglefydz

