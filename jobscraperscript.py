from urllib.request import Request, urlopen
from fake_useragent import UserAgent
import random
from bs4 import BeautifulSoup
from IPython.core.display import clear_output
import requests
# Here I provide some proxies for not getting caught while scraping
ua = UserAgent() # From here we generate a random user agent
proxies = [] # Will contain proxies [ip, port]

# Main function
def main():
  # Retrieve latest proxies
  URL = "https://realpython.github.io/fake-jobs/"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  #print(page.text)
  results = soup.find(id="ResultsContainer")
  #print(results.prettify())
  job_elements = results.find_all("div", class_="card-content")
  for job_element in job_elements:
    print(job_element, end="\n"*2)
if __name__ == '__main__':
  main()


