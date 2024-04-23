import smtplib

sender = "Private Person <mailtrap@demomailtrap.com>"
receiver = "A Test User <linoone104@gmail.com>"

message = f"""\
Subject: Academic Probation Notice
To: {receiver}
From: {sender}

Academic Probation Notification-Do not reply to this email, I hope this message finds you well. I wanted to inform you that, following a review of your academic performance you are currently on academic probation."""

with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
    server.starttls()
    server.login("api", "c718b4483cd28992ae4089da8297df64")
    server.sendmail(sender, receiver, message)