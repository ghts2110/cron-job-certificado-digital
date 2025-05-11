def verificar_mensagens(session, token, cnpj):
    url = f"https://det.sit.trabalho.gov.br/services/v1/caixapostal/{cnpj}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    response = session.get(url, headers=headers)

    if response.status_code == 200:
        if not response.text.strip():
            print(f"📭 CNPJ {cnpj} acessado com sucesso, mas sem retorno de mensagens (resposta vazia).")
            return

        try:
            mensagens = response.json()
            if mensagens:
                print(f"📬 {len(mensagens)} mensagens para o CNPJ {cnpj}:")
                for msg in mensagens:
                    titulo = msg.get('titulo', 'Sem título')
                    print(f"- {titulo}")
            else:
                print(f"📭 Nenhuma mensagem encontrada para o CNPJ {cnpj}.")
        except Exception as e:
            print("❌ Erro ao interpretar JSON:")
            print(e)
    else:
        print(f"❌ Erro HTTP {response.status_code}")