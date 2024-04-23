import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

sender = 'linoone104@gmail.com'
receivers = ['r.o.ramoune@gmail.com']

# Create the HTML message
html = f"""\
<html>
  <head></head>
  <body>
    <p>Hello,<br>This is an email with HTML content.</p>
    <p>Here is an <a href="https://www.gmail.com">example link</a>.</p>
  </body>
</html>
"""

# Create the email message
message = MIMEMultipart()
message['From'] = sender
message['To'] = ', '.join(receivers)
message['Subject'] = 'Email with HTML content and attachment'

# Add the HTML content
message.attach(MIMEText(html, 'html'))

# Add the attachment
#with open('example.txt', "rb") as f:
 #   part = MIMEApplication(f.read(), _subtype="txt")
#    part.add_header('content-disposition', 'attachment', filename='example.txt')
 #   message.attach(part)

# Send the email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('linoone104@gmail.com', 'riverview104')
text = message.as_string()
server.sendmail(sender, receivers, text)
server.quit()

print("Successfully sent email")