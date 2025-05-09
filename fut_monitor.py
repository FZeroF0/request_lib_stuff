import os
import smtplib
import requests

r = requests.get('https://coreyms.com', timeout=5)

if r.status_code != 200:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login()
t=os.environ.get(mail1)
print(t)
