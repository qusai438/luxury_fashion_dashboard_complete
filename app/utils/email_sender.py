import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
FROM_NAME = os.getenv("EMAIL_FROM_NAME", "Luxury Fashion Store")

def send_return_update_email(to_email, order_id, status):
    if not to_email:
        return

    subject = f"Return Request Update – Order #{order_id}"
    status_text = {
        "Approved": "✅ Your return has been approved.",
        "Rejected": "❌ Unfortunately, your return request was rejected.",
        "Pending": "⏳ Your return request is under review."
    }.get(status, f"Your return request is now marked as: {status}")

    html_content = f"""
    <html>
      <body>
        <p>Hello,</p>
        <p>{status_text}</p>
        <p><strong>Order ID:</strong> {order_id}</p>
        <p>Thank you for shopping with us.<br>{FROM_NAME}</p>
      </body>
    </html>
    """

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"{FROM_NAME} <{SMTP_USER}>"
    msg["To"] = to_email
    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, to_email, msg.as_string())
    except Exception as e:
        print(f"[Email Error] Failed to send email to {to_email}: {e}")
