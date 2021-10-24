import os
import json
import hmac
import base64
import hashlib
import requests
from subprocess import Popen, PIPE, DEVNULL
from google.cloud import vision
import io


def is_usable(path, given_label):
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    labels = client.label_detection(image=image).label_annotations

    if labels:
        return labels[0].score > 0.5 and lower(labels[0].description) == lower(given_label)
    else:
        return False


