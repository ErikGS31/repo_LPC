import argparse
import re
import sys
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

RE_EMAIL = re.compile('[^@]+@[^@]+\.[a-zA-Z]{2,}')

def email_type(value):
    if not RE_EMAIL.match(value):
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid email")
    return value

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', '--u', type= email_type, help= 'Escriba su correo de Gmail')
    parser.add_argument('--password', type= str, help= 'Escriba su token/contraseña')
    parser.add_argument('--addressee', type = email_type, help= 'Escriba el destinatario')
    parser.add_argument('--subject', type= str, help= 'Escriba un asunto')
    args = parser.parse_args()
    sys.stdout.write(str(send_mail(args)))

def send_mail(args):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(args.user, args.password)
    message = MIMEMultipart('Alternative')
    message['Subject'] = args.subject
    message['from'] = args.user
    message['to'] = args.addressee
    
    html = f"""
    <html>
    <body>
        Hola {args.addressee}
        Mensaje de prueba para el laboratorio
    </body>
    </html>
    """

    parte_html = MIMEText(html, "html")
    message.attach(parte_html)
    archivo = 'C:\Users\Erik\Documents\repo_LPC\practica8\Fondo_DB.jpeg'
    with open(archivo, 'rb') as att:
        content_att = MIMEBase('aplication', 'octet-stream')
        content_att.set_payload(att.read())

    content_att.add_header(
        'Content-Disposition',
        f'attachment; filename= Fondo_DB',
    )
    message.attach(content_att)
    text = message.as_string
    smtp.send_message(message)
    smtp.quit
    return('El mensaje de envio correctamente')

if __name__ == '__main__':
    main()
