import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage

with smtplib.SMTP_SSL('smtp.zone.eu', 465) as server:



    server.login('python@mrartful.com', 'qwe576!sdf')

    msg = EmailMessage()
    msg['From'] = 'python@mrartful.com'
    msg['To'] = 'dmitrbelan@gmail.com'
    msg['Subject'] = 'This is test email sent by python script'
    msg.set_content('Sample email sent by python')
    msg.add_alternative( f'<h1>Hello I am just a test email created by Python! TEST TEST TEST</h1>', subtype='html')

    server.send_message(msg)

