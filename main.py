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

requestReponse = requests.get(requestURL)
print(requestReponse.status_code)
#print requestReponse.text

responseBody = requestReponse.text

linkIter = re.finditer(linkRegex, responseBody)
matchList = list(linkIter)
matches = [matchItem.group(1) for matchItem in matchList]
#print(len(matches))




def findLinks( title ):
    baseURLstart = 'https://en.wikipedia.org/api/rest_v1/page/html/'
    baseURLend = '?redirect=true'

    requestURL = baseURLstart + title + baseURLend
    #print requestURL
    requestReponse = requests.get(requestURL)
    print (requestReponse.status_code)
    if requestReponse.status_code == 200 :
        linkIter = re.finditer(linkRegex, requestReponse.text)
        matchList = list(linkIter)
        matches = [matchItem.group(1) for matchItem in matchList]
        return matches
    else:
        print ("REST API error")
        return []

allMatches = []
for match in matches:
    if match == destinationPage:
        print ("I found it!")
        break
    print(match)
    allMatches.extend(findLinks(match))
found = False
print(len(allMatches))
allMatches = set(allMatches)
print(len(allMatches))
while not found:
    matches = allMatches
    allMatches = []
    for match in matches:
        if match == destinationPage:
            print ("I found it!")
            found = True
            break
        print(match)
        allMatches.extend(findLinks(match))
    print(len(allMatches))
    allMatches = set(allMatches)
    print(len(allMatches))
