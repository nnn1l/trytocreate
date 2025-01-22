import requests
import logging
from requests.exceptions import HTTPError
from pprint import pprint

PROTOCOL = "https://"
BASE_URL = "genshin-impact.fandom.com/wiki/Raiden_Shogun"

def get_page_content():
    url = PROTOCOL + BASE_URL
    logging.info(f"GET request to {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except HTTPError as exc:
        logging.error(f"Request failed. Details: {exc}")
        raise exc
    return response.text

pprint(get_page_content())


def download_to_txt(domain, save_path):
    url = f"https://{domain}/robots.txt"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(save_path, 'w') as file:
            file.write(response.text)
        print(f"robots.txt successfully saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download robots.txt: {e}")


download_to_txt("genshin-impact.fandom.com", "robots.txt")