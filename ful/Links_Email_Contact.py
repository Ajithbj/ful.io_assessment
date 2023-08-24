import re
import requests
from bs4 import BeautifulSoup

def get_website_details(url):
  
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  
  social_links = []
  for link in soup.find_all('a'):
    if 'facebook' in link.get('href'):
      social_links.append(link.get('href')) 
    elif 'linkedin' in link.get('href'):
      social_links.append(link.get('href'))

  emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', response.text)
  
  phone_numbers = re.findall(r'\+?[0-9]+(?:\s?[0-9]+){8,}', response.text)
  
  print("Social links:")
  print(*social_links, sep = "\n")
  
  print("\nEmail/s:")
  print(*emails, sep = "\n")

  print("\nContact:") 
  print(*phone_numbers, sep = "\n")


s='https://ful.io'  #input()
get_website_details(s)