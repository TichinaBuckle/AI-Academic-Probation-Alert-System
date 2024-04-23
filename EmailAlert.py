import smtplib

sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

message = f"""\
Subject: Academic Probation Notification
To: {receiver}
From: {sender}

Academic Probation Notification-Do not reply to this email, I hope this message finds you well. I wanted to inform you that, following a review of your academic performance you are currently on academic probation."""

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    server.starttls()
    server.login("7bc90479fda654", "288824f564c517")
    server.sendmail(sender, receiver, message)