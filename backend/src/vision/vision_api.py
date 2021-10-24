import os
import json
from google.cloud import vision
import io
import base64

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.environ['GCP_KEY_FILE']


def is_usable(path, given_label):
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    labels = client.label_detection(image=image).label_annotations
    for label in labels:
        if label.score > 0.5 and label.description.lower() == given_label.lower():
            return True
    return False
