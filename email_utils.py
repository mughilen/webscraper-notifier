import smtplib
import json

def send_email(subject, body, config):
    sender = config["sender_email"]
    receiver = config["receiver_email"]
    password = config["email_password"]

    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP(config["smtp_server"], config["smtp_port"]) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, message)
            print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", e)
