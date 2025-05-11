from detSession import iniciar_sessao
from detApi import verificar_mensagens
from private import getDoc

if __name__ == "__main__":
    session = iniciar_sessao(getDoc.getCertificate())

    if session:
        token = "<Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhbXIiOiJhY2Vzc28uZ292IiwiY25waiI6IiIsImNwZlJlc3BvbnNhdmVsIjoiIiwiZXhwIjoxNzQ2OTQ5NTA1LCJwZXJmaWwiOm51bGwsInBqIjpmYWxzZSwic3ViIjoiNTcwNzE3NjQ0NjgiLCJ1c2VybmFtZSI6IkdFUk1BTkEgTUVMTyBUT1JSRVMgU0FOVE9TIn0.OJRlQjR7tGTg6ioqtc31CuhH2wmf8_-ofNhNb1-zEnE>"
        verificar_mensagens(session, token, '03956551000111')
