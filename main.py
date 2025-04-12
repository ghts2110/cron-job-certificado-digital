import smtplib
import os
import checkWebsite 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def send_email():    
    try:
        user = os.getenv('EMAIL_USER')
        password = os.getenv('EMAIL_PASS')
        receiver = os.getenv('EMAIL_RECEIVER')

        servidor_email = smtplib.SMTP('smtp.gmail.com', 587)
        servidor_email.starttls()

        servidor_email.login(user, password)

        mensagem = MIMEMultipart()
        mensagem['From'] = user
        mensagem['To'] = receiver
        mensagem['Subject'] = 'Notificação automática: Verificação de certificado digital'

        ans = checkWebsite.isitchristmas()
        corpo = "Verificação automática: "
        if(ans == False):
            corpo += "ainda não é Natal :("
        else:
            corpo += "é Natal 🎄"

        mensagem.attach(MIMEText(corpo, 'plain'))

        servidor_email.sendmail(user, receiver, mensagem.as_string())
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    send_email()
