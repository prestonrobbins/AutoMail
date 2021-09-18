# dont name python file "email.py" or it will break
#  https://www.youtube.com/watch?v=JRCJ6RtE3xU
from secrets import (MY_EMAIL, MY_PASSWORD)
# import smtplib
# from email.message import EmailMessage

# EMAIL_ADDRESS = os.envriron.get('MY_EMAIL')
# EMAIL_PASSWORD = os.envriron.get('MY_PASSWORD')

# msg = EmailMessage()
# msg['Subject'] = 'Grab dinner this weekend?'
# msg['From'] = MY_EMAIL
# msg['To'] = 'prestonshottss@gmail.com'
# msg.set_content('This is an automated message, did it send!')

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(MY_EMAIL, MY_PASSWORD)
#     smtp.send_message(msg)



# HOW TO SEND IN A TEST ENVIORNMENT
import smtplib

from secrets import (MY_EMAIL, MY_PASSWORD)

with smtplib.SMTP('localhost', 1025) as smtp:

    subject = 'Get together soon?'
    body = 'how about a hike and hotpot October 2nd?'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(MY_EMAIL, MY_EMAIL, msg)


# RUN THIS COMMAND IN YOUR TERMINAL TO SEE EMAIL, THEN RUN THE CODE
# python3 -m smtpd -c DebuggingServer -n localhost:1025