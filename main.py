import re
import requests
from requests.auth import HTTPDigestAuth
import json


linkRegex = 'a\\ rel\\=\\"mw\\:WikiLink\\"\\ href\\=\\"\\.\\/([^\s]+)\\"'
textFile = 'testPage.html'

#with open(textFile, 'r') as wordFile:
#    textString=wordFile.read().replace('\n', '')




baseURLstart = 'https://en.wikipedia.org/api/rest_v1/page/html/'
baseURLend = '?redirect=true'

targetPage = 'Artificial_intelligence'
destinationPage = 'Fatigue_(material)'

requestURL = baseURLstart + targetPage + baseURLend

print(requestURL)

requestResponse = requests.get(requestURL)
print(requestResponse.status_code)
#print requestResponse.text

responseBody = requestResponse.text

linkIter = re.finditer(linkRegex, requestResponse.text)
regexList = list(linkIter)
linksFromPage = [regexMatch.group(1) for regexMatch in regexList]
#print(len(matches))



def findLinks( title ):
    baseURLstart = 'https://en.wikipedia.org/api/rest_v1/page/html/'
    baseURLend = '?redirect=true'

    requestURL = baseURLstart + title + baseURLend
    #print requestURL
    requestReponse = requests.get(requestURL)
    print (requestResponse.status_code)
    if requestResponse.status_code == 200 :
        linkIter = re.finditer(linkRegex, requestResponse.text)
        RegexList = list(linkIter)
        linksFromPage = [regexMatch.group(1) for regexMatch in regexList]
        return linksFromPage
    else:
        print ("REST API error")
        return []

allLinks = []
for link in linksFromPage:
    if link == destinationPage:
        print ("I found it!")
        break
    print(link)
    linksFromPage.extend(findLinks(link))
found = False
print(len(linksFromPage))
linksFromPage = set(linksFromPage)
print(len(linksFromPage))
while not found:
    searchSpace = linksFromPage
    linksFromPage = []
    for link in SearchSpace:
        if match == destinationPage:
            print ("I found it!")
            found = True
            break
        print(link)
        linksFromPage.extend(findLinks(link))
    print(len(linksFromPage))
    linksFromPage = set(linksFromPage)
    print(len(linksFromPage))
