import smtplib
from email.message import EmailMessage
from os import getenv

class EmailService:
    def send_email(self, to: str, subject: str, body: str) -> None:
        smtp_server = getenv("SMTP_SERVER")
        smtp_port = int(getenv("SMTP_PORT", 587))
        smtp_user = getenv("SMTP_USERNAME")
        smtp_password = getenv("SMTP_PASSWORD")
        from_email = getenv("FROM_EMAIL", smtp_user)

        if not all([smtp_server, smtp_user, smtp_password]):
            raise ValueError("SMTP configuration is missing in environment variables.")

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = from_email
        msg["To"] = to
        msg.set_content(body)

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
