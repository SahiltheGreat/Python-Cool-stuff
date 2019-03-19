from bs4 import BeautifulSoup
import requests
page_url= "https://www.smbc-comics.com/"
page_response = requests.get(page_url, timeout=5)
page_content = BeautifulSoup(page_response, "html.parser")
