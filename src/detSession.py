import requests
from private import getDoc

def iniciar_sessao(cert_path):
    url = 'https://det.sit.trabalho.gov.br/servicos'

    session = requests.Session()

    try:
        response = session.get(url, cert=cert_path, verify=True, allow_redirects=True)

        if response.status_code == 200:
            print("✅ Autenticado com sucesso!")
            # print(response.text)  
            return session
        else:
            print(f"❌ Erro {response.status_code}")
            return None
    except requests.exceptions.SSLError as ssl_err:
        print("🔒 Erro SSL — certificado ou cadeia inválida:")
        print(ssl_err)

if __name__ == "__main__":
    iniciar_sessao(getDoc.getCertificate())
