from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(START_URL)
headers = ["V Mag. (mV)",	"Proper name"	,"Bayer designation","Distance (ly)",	
"Spectral class",	"Mass (M☉)",	"Radius (R☉)",	"Luminosity (L☉)"]
soup = bs(page.text,'html.parser')
table =soup.find("table")
temp_list= []
table_rows = table.find_all('tr')         
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)       
with open("final.csv", "w",encoding="utf-8") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(temp_list)