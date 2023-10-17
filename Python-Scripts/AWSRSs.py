import feedparser
import json
import os
import schedule
import time
import requests


# Network Error Checking
def NetworkError_Checking(feed_url):

    try:
        response = requests.get(feed_url)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        exit(0)

#Checking the JSON Errors
def JsonErrorChecking(feed_url):
    try:
        feed_data = feedparser.parse(feed_url)

    except json.JSONDecodeError as e:
        print("Invalid JSON data:", e)
        exit(0)
    except Exception as e:
        print("An unexpected error occurred:", e)
        exit(0)


def AWS_RSS_Function():
    JSON_Filename = "AWS_RSS.json"                  #JSON File name

    open(JSON_Filename, "w")

    fileolddata=[]                                              # empty list to store data that is in the file.

    with open(JSON_Filename, "r") as json_file:                 # opening the file wuith read mode  
        file_size = os.path.getsize(JSON_Filename)
        if file_size != 0:                                      #checking if file is empty
            checkdata = json.load(json_file)

            for filedata in checkdata:                          #appending data of json file to another list variable
                fileolddata.append(filedata)

    RSS_feed_URL='https://aws.amazon.com/blogs/aws/feed/'

    NetworkError_Checking(RSS_feed_URL)                         # checking for network error
    JsonErrorChecking(RSS_feed_URL)                             # checking for JSON error

    feedparsing = feedparser.parse(RSS_feed_URL)                # parsing the feed from the given link of AWS feed.

    i=0
    for feeddata in feedparsing:

        guidinfo=feedparsing.entries[i].guid                    # Filering out the data from the entries of XML file
        titleinfo = feedparsing.entries[i].title
        linkinfo = feedparsing.entries[i].link
        descriptioninfo = feedparsing.entries[i].description
        i+=1


        RSS_Retrieved_data = {                                  # setting the dictionary in the proper way that will later be added to json file if it is not the duplicate from the file
            "guid": guidinfo,
            "Title": titleinfo,
            "Link": linkinfo,
            "Description": descriptioninfo
        }

        file_size = os.path.getsize(JSON_Filename)

        duplicate=False
        
        if file_size != 0:                                      # checking if file is non empty
            with open(JSON_Filename, "r") as json_file:         # opening file with read mode to get data
                checkdata = json.load(json_file)

            j=0
            for ids in checkdata:                               # Loop created to check if there is duplicate in the folder then make the flag true
                rssdata=checkdata[j]
                guiddata=rssdata["guid"]                        # check with the attribute of guid to find the duplicates available in file
                if(guidinfo == guiddata):       
                    duplicate=True
                    break
                j+=1
                
        if(duplicate == True):                                  # checking if duplicate available in json file then move on to other file
            continue
        else:
            fileolddata.append(RSS_Retrieved_data)              # if duplicate not found append it to json file old data

            with open(JSON_Filename, "w") as json_file:         # overwrites the json file with list having previous data as well.
                json.dump(fileolddata, json_file, indent=4)


# First call to function before schedule start
AWS_RSS_Function()          

schedule.every(15).minutes.do(AWS_RSS_Function) 

while True:
    schedule.run_pending()                                      #sleep is used to make program neutral and do not utilize processor power
    time.sleep(1)



