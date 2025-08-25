import smtplib
import ssl
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")


def send_reset_email(to_email: str, reset_link: str):
    msg = EmailMessage()
    msg["Subject"] = "Redefinição de Senha - Tokaki"
    msg["From"] = EMAIL_USER
    msg["To"] = to_email

    msg.set_content(f"""
Olá,

Recebemos um pedido para redefinir sua senha.

Clique no link abaixo para redefini-la (válido por 1 hora):
{reset_link}

Se você não solicitou essa redefinição, ignore este email.

Equipe Tokaki
""")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
