import requests
from private import getDoc

def loginWebsit(cert_path):
    url = 'https://det.sit.trabalho.gov.br/servicos'

    try:
        response = requests.get(url, cert=cert_path, verify=True)

        if response.status_code == 200:
            print("✅ Acesso com certificado realizado com sucesso!")
        else:
            print(f"⚠️ Falha no acesso. Código HTTP: {response.status_code}")

    except requests.exceptions.SSLError as ssl_err:
        print("❌ Erro SSL — verifique se o certificado e a chave estão corretos ou se falta a cadeia de certificados.")
        print(ssl_err)

    except Exception as e:
        print("❌ Ocorreu um erro inesperado:")
        print(e)

if __name__ == "__main__":
    loginWebsit(getDoc.getCertificate())
