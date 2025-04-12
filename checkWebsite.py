import requests
from dotenv import load_dotenv
import os

load_dotenv()

def is_friday():
    url = os.getenv('WEBSITE_URL')

    try:
        response = requests.get(url)
        response.raise_for_status()
        
    except Exception as e:
        print(f"Erro ao acessar o site: {e}")
        return False

if __name__ == "__main__":
    is_friday()