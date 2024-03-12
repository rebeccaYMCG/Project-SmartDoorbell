import requests
from http.client import responses
from io import BytesIO

# azure face api key and endpoint goes here 
azure_face_api_key = "b1fda5c17aa547c5a13a79d11b75c4f6"
azure_face_api_endpoint = "https://smartringerapi.cognitiveservices.azure.com/T"

# url to image
iamge_url = "IMAGE URL" # should send to SQL database

# azure face api endpoint
face_api_url = f"{azure_face_api_endpoint}/face/v1.0/detect"

# header request
headers = {
    "Content-Type": "application/json",
    "Ocp-apim-Subscription-key": azure_face_api_key,
}

# params request
params = {
    "returnFaceId": "true",
    "returnFaceLandmarks": "false",
    "returnFaceAttributes": "gender,age,smile,facialHair,glasses,emotion",
}

# body request
body = {"url"}

# send the post request to azure face api
responce = requests.post(face_api_url, params=params, headers=headers, json=body)

# check for success
if responce.status_code == 200:
    detected_faces = responce.json()

    # process the detected faces
    for face in detected_faces:
        face_id = face["faceId"]
        face_attributes = face["faceAttributes"]

        print(f"Face ID: {face_id}")
        print(f"Age: {face_attributes['age']}")
        print(f"Gender: {face_attributes['gender']}")
        print(f"Smile: {face_attributes['smile']}")
        print(f"Glasses: {face_attributes['glasses']}")
        print(f"Emotion: {face_attributes['emotion']}")

else:
    print(f"Error: {responses.status_code}, {responses.text}")