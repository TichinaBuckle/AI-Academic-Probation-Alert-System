import smtplib

sender = "Private Person <mailtrap@demomailtrap.com>"
receiver = "A Test User <linoone104@gmail.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
    server.starttls()
    server.login("api", "c718b4483cd28992ae4089da8297df64")
    server.sendmail(sender, receiver, message)