import requests
from bs4 import BeautifulSoup
from flask import jsonify
import random

def get_jobs(count: int, shuffle:bool):
    url = "https://www.python.org/jobs"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    pages = len(soup.find_all("ul",attrs={"class":"pagination"})[0].find_all("li")) - 2
    # totalJobs = 0
    # for pageNumber in range(1,pages + 1):
    #     pageRequest = requests.get("https://www.python.org/jobs/?page=" + str(pageNumber))
    #     pageSource = BeautifulSoup(pageRequest.content,"lxml")
    #     jobs = pageSource.find("div",attrs={"class":"row"}).ol.find_all("li")
    #     # После получения всех вакансий пройдёмся циклом по ним, чтобы получить детали
    #     for job in jobs:
    #         name = job.h2.find("a").text
    #         location = job.find("span",attrs={"class":"listing-location"}).text
    #         company = job.find("span",attrs={"class":"listing-company-name"}).br.next.strip()
    #         publish_time = job.find("time").text
    #         totalJobs += 1
    #         print(name,company,location,publish_time,sep="\n")
    #         print("-"*60)

    # return "Найдено {} вакансий.".format(totalJobs)
    c = 0
    items = []
    for pageNumber in range(1,pages + 1):
         pageRequest = requests.get("https://www.python.org/jobs/?page=" + str(pageNumber))
         pageSource = BeautifulSoup(pageRequest.content,'html.parser')
         jobs = pageSource.find("div",attrs={"class":"row"}).ol.find_all("li")
         if (c == count):
            break
         for job in jobs:
             name = job.h2.find("a").text
             location = job.find("span",attrs={"class":"listing-location"}).text
             company = job.find("span",attrs={"class":"listing-company-name"}).br.next.strip()
             publish_time = job.find("time").text
             items.append(dict(name = job.h2.find("a").text,location = job.find("span",attrs={"class":"listing-location"}).text,company = job.find("span",attrs={"class":"listing-company-name"}).br.next.strip(),publish_time = job.find("time").text))
             c += 1
             if (c == count):
                break
    if (shuffle == True):
        random.shuffle(items)
    
    return items

    #         totalJobs += 1
    #         print(name,company,location,publish_time,sep="\n")
    #         print("-"*60)

def parse_jobs(name: str, location: str, company:str, publish_time:str):
    return jsonify(name=name,location=location,company=company,publish_time=publish_time)
