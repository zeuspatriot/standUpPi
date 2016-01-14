import requests
import picamera

camera = picamera.PiCamera()
req = requests
faceKey = "da746b93c6374e0189d3976e36bf67ee"

arrayPhotoHolder = []


# error Handling needs to be added
def create_person_group(groupId, personGroupName):
    data = {
        "name": personGroupName,
        "userData": "group of users in face rec system"
    }
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": faceKey,
        "Accept": "application/json"
    }
    url = 'https://api.projectoxford.ai/face/v1.0/persongroups/' + groupId
    return req.put(url, data=str(data), headers=headers)


# error Handling needs to be added
def get_person_group(groupId):
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": faceKey,
        "Accept": "application/json"
    }
    url = "https://api.projectoxford.ai/face/v1.0/persongroups/" + groupId
    return req.get(url, headers=headers)


# error Handling needs to be added
def train_person_group(groupId):
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": faceKey,
        "Accept": "application/json"
    }
    url = "https://api.projectoxford.ai/face/v1.0/persongroups/" + groupId + "/train"
    return req.post(url, headers=headers)


# error Handling needs to be added
def create_person(groupId, personName, personComment=""):
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": faceKey
    }
    data = {
        "name": personName,
        "userData": personComment
    }
    url = "https://api.projectoxford.ai/face/v1.0/persongroups/" + groupId + "/persons"
    return req.post(url, data=str(data), headers=headers)  # returns ID of a user in a response


# error Handling needs to be added
def add_person_face(groupId, personId, image, personComment="", targetFace=""):
    headers = {
        "Content-Type": "application/octet-stream",
        "Ocp-Apim-Subscription-Key": faceKey
    }
    data = image
    url = "https://api.projectoxford.ai/face/v1.0/persongroups/" + groupId + "/persons/" + personId + "/persistedFaces?" + personComment + "&" + targetFace
    return req.post(url, data=str(data), headers=headers)  # returns persistedFaceId in response


# error Handling needs to be added
def detect_face():
    headers = {
        "Content-Type": "application/octet-stream",
        "Ocp-Apim-Subscription-Key": faceKey
    }
    data = take_photo()
    url = "https://api.projectoxford.ai/face/v1.0/detect?returnFaceId=true"
    return req.post(url, data=str(data), headers=headers).json()

def detect_face_manual(photo):
    headers = {
        "Content-Type": "application/octet-stream",
        "Ocp-Apim-Subscription-Key": faceKey
    }
    data = photo
    url = "https://api.projectoxford.ai/face/v1.0/detect?returnFaceId=true"
    return req.post(url, data=str(data), headers=headers).json()


# error Handling needs to be added
def get_person_list(groupId):
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": faceKey
    }
    url = "https://api.projectoxford.ai/face/v1.0/persongroups/" + groupId + "/persons"
    return req.get(url, headers=headers)


# error Handling needs to be added
def get_person(groupId, personId):
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": faceKey
    }
    url = "https://api.projectoxford.ai/face/v1.0/persongroups/" + groupId + "/persons/" + personId
    return req.get(url, headers=headers)  # returns ID of a user in a response


# error Handling needs to be added
def update_person(groupId, personId, updatedData):
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": faceKey
    }
    data = updatedData
    url = "https://api.projectoxford.ai/face/v1.0/persongroups/" + groupId + "/persons/" + personId
    return req.patch(url, data=str(data), headers=headers)


# error Handling needs to be added
def create_face_list(faceListId, faceListName, faceListComment="no comments"):
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": faceKey
    }
    data = {
        "name": faceListName,
        "userData": faceListComment
    }
    url = "https://api.projectoxford.ai/face/v1.0/facelists/" + faceListId
    return req.put(url, data=str(data), headers=headers)


# asd list was created

# error Handling needs to be added
def get_face_list(faceListId):
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": faceKey
    }
    url = "https://api.projectoxford.ai/face/v1.0/facelists/" + faceListId
    return req.get(url, headers=headers)


# error Handling needs to be added
def add_face_to_face_list(faceListId, faceURL, faceComment="", faceRectangle=""):
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": faceKey
    }
    data = {
        "url": faceURL
    }
    url = "https://api.projectoxford.ai/face/v1.0/facelists/" + faceListId + "/persistedFaces?userData=" + faceComment + "&targetFace=" + faceRectangle
    return req.post(url, data=str(data), headers=headers)


# error Handling needs to be added
def find_similar_face(faceId, faceListId, maxNumberOfResults=1):
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": faceKey
    }
    data = {
        "faceId": faceId,
        "faceListId": faceListId,
        "maxNumOfCandidatesReturned": maxNumberOfResults
    }
    url = "https://api.projectoxford.ai/face/v1.0/findsimilars"
    return req.post(url, data=str(data), headers=headers)


# error Handling needs to be added
def identify_face(faceIdArray, faceListId, maxNumberOfResults=1):
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": faceKey
    }
    data = {
        "personGroupId": faceListId,
        "faceIds": faceIdArray,
        "maxNumOfCandidatesReturned": maxNumberOfResults
    }
    url = "https://api.projectoxford.ai/face/v1.0/identify"
    return req.post(url, data=str(data), headers=headers)


def take_photo():
    camera.capture("face.jpg")
    photo = open("face.jpg", "rb")
    photo_binary = photo.read()
    photo.close()
    return photo_binary
