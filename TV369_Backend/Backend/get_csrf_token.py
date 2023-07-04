import requests
from bs4 import BeautifulSoup
import re


def extract_csrf_token(response):
    soup = BeautifulSoup(response.content, "html.parser")
    csrf_input = soup.find("input", attrs={"name": "csrfmiddlewaretoken"})
    if csrf_input:
        return csrf_input["value"]
    else:
        raise ValueError("CSRF token not found in the response.")
