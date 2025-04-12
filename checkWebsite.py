import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

def isitchristmas():
    url = os.getenv('WEBSITE_URL')

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        answer = soup.find(id="answer").get_text(strip=True)
        return answer.upper() == "SIM"
    except Exception as e:
        print(f"Erro ao acessar o site: {e}")
        return False

if __name__ == "__main__":
    ans = isitchristmas()
    print(ans)