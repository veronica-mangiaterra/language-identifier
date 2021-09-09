from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
options = Options()
options.add_argument("--headless")#this is used to avoid to open the browser
driver = webdriver.Chrome(r"/chromedriver.exe", options=options)
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from sklearn import feature_extraction
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix

wiki_url_list = ["https://it.wikipedia.org/wiki/Pagina_principale", "https://es.wikipedia.org/wiki/Wikipedia:Portada", "https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal", "https://nl.wikipedia.org/wiki/Hoofdpagina"]
path_txt = [r"C:\Users\user\Desktop\it_txt.txt", r"C:\Users\user\Desktop\es_txt.txt", r"C:\Users\user\Desktop\fr_txt.txt", r"C:\Users\user\Desktop\ne_txt.txt" ]

def get_random_page(wiki_url):
    """This first function is used to obtain the text associated with the link to the random page in the wikipedia homepage"""
    rand_response = requests.get(wiki_url)
    rand_source = rand_response.text
    rand_soup = BeautifulSoup(rand_source, "lxml")
    random_page = rand_soup.find("li", id= "n-randompage")
    return random_page.get_text()
random_texts = [get_random_page(url)for url in wiki_url_list]
zip_wiki_random_txt = zip(wiki_url_list, random_texts, path_txt)
wiki_random_txt = tuple(zip_wiki_random_txt) #I stored in a variable, all three items that I need as input of the next function

def get_content (wiki_url,random, path):
    """this function gets as an input a wikipedia url, the text associated with the 'random page' link and a path to a txt
    file where it will store the text. It goes to the home page of wikipedia and till it collects 1.000.000 words, it keeps navigating the 
    random page and appending the text to a list. When it get to the number of words required, it open the txt file and write there
    the text"""
    l_one = [] #I created a list, where all the text will be stored
    driver.get(wiki_url)
    while len(l_one)<1000000:
        driver.find_element_by_link_text(random).click() #with the"find element by link text" method the first
        #element with the link text value matching the location will be returned, then with the "click" method it's possible to
        # click in that link
        response= requests.get(driver.current_url)
        source = response.text
        soup = BeautifulSoup(source, "lxml")
        some_wiki = soup.find_all("p")
        l=[]
        for tag in some_wiki:
            l.append(tag.get_text().split(" "))
        print(l)
        for sent in l:
            for word in sent:
                l_one.append(word)
        print(l_one)
        print(len(l_one))
    txt = open(path, "a", encoding="utf8")
    txt.write(" ".join(l_one))
    txt.close()
    return len(l_one)

for wiki, rand, path in wiki_random_txt:
    get_content(wiki, rand, path)
