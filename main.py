#################################################
# Title: Jive API Helper
# Description: Python Code to Run API for Jive
# Author: Hitesh Solanky
# Date: 21/09/2020
# Jive Rest API: v3
#################################################

import requests, json
from requests.auth import HTTPBasicAuth

# Initialize Constants
username = 'admin'
password= 'admin123'
API_PREFIX = 'https://jive-hop-se7.jivelandia.com/api/core/v3/'
headers = {'Content-Type' : 'application/json;charset=UTF-8;' }
auth = HTTPBasicAuth(username, password)
        
def getAllContents():
    """ 
    The function to get All Contents. 
        
    Returns: 
        Response JSON: Response returned from the API Endpoint as JSON
    """
    response = requests.get(url = API_PREFIX + 'contents', auth = auth) 
    return response.json()

def getContentById(id):
    """ 
    Function to get Detailed Data about a content

    Parameters: 
        id (Integer): The contentID of the object
        
    Returns: 
        Response JSON: Response returned from the API Endpoint as JSON
    """
    response = requests.get(url = API_PREFIX + 'contents/' + id, auth = auth) 
    return response.json()

def addDocumentToGroupOrSpace(subject, contentText, parentPlaceURI):
    """ 
    Function to Add content to a Space or Group

    Parameters: 
        subject (String): The Subject of the Document
        contentText (String): The Text of the Document
        parentPlaceURI (String): The URI of the parent space or group to which the content needs to be added
        
    Returns: 
        Response JSON: Response returned from the API Endpoint as JSON
    """
    payload = {
                'content':
                        {'type':'text/html',
                        'text': contentText },
                'subject': subject,
                'type': 'document' ,
                'visibility': 'place', 
                'parent': parentPlaceURI
                }
    response = requests.post(url = API_PREFIX + 'contents', auth = auth, headers = headers, data = json.dumps(payload))
    return response.json()


def createMultipleDocuemntsInGroup():
    parentSpaceURI = 'https://jive-hop-se7.jivelandia.com/api/core/v3/places/1773'
    for i in range(1, 1001):
        try:
            documentIndex = str(i)
            contentText = 'some random content 21 sep 2020 doc-index-' + documentIndex
            subject = 'some subject doc-index-' + documentIndex
            print('Adding content --- ' + documentIndex)
            response = addDocumentToGroupOrSpace(subject, contentText, parentSpaceURI)
            if('error' not in response):
                print('Success Adding Content --- ' + documentIndex)
            else:
                print('Error Adding Content --- ' + documentIndex)
                print (response)
        except Exception as inst:
            print(type(inst))    # the exception instance
            print(inst.args)     # arguments stored in .args
            print(inst) 
        

if __name__ == '__main__':
    print('Program Started !')
    
    # Write your code here
    createMultipleDocuemntsInGroup()
    
    print('Program End !')
    