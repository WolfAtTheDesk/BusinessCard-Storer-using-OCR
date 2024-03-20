"""
This file describes methods used for OCR operations
Title: OCR
File location: OCR/Pages/OcrMethods.py
"""
#standard pkgs
import os
import re
import pandas as pd
from datetime import datetime

#drawing pkgs
import matplotlib.pyplot as plt

#OCR pkgs
import cv2
import easyocr

#init of easyocr
reader = easyocr.Reader(['en'])

def path_to_file(upload):
    return os.getcwd()+ "/Cards/" + upload.name

#saves uploaded file to OCR/Cards
def save_card(card):
    timestamp = datetime.now().strftime("%y%m%d-%H%M%S")
    filename, extension = os.path.splitext(card.name)
    path = os.path.join(f"Cards", f"{filename}_{timestamp}{extension}")
    with open(path, "wb") as f:
        f.write(card.getbuffer())
    return path

#uses cv2 and easyocr to read the text on an image, returns the image and a list of all the detected text along with its position
def ocr_run(path):
    image = cv2.imread(path)
    words = reader.readtext(path,width_ths = 0.8, paragraph=True,y_ths=0.1)

    return image, words

#previews the image with an overlay of the Recognized text
def image_preview(image,words):
    # unpack the bounding box
    for (boundbox, text) in words:
        (topleft, topright, bottomright, bottomleft) = boundbox
        topleft     = (int(topleft[0])    , int(topleft[1]))
        topright    = (int(topright[0])   , int(topright[1]))
        bottomright = (int(bottomright[0]), int(bottomright[1]))
        bottomleft  = (int(bottomleft[0]) , int(bottomleft[1]))
        cv2.rectangle(image,
                     topleft,
                     bottomright,
                     (20, 20, 200),
                     2)
        cv2.putText(image,
                    text,
                    (topleft[0], topleft[1] - 10),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.5,
                    (0, 255, 0),
                    1,
                     cv2.LINE_AA)
    # plt.rcParams['figure.figsize'] = (15,15)
    # plt.axis('off')
    plt.imshow(image)


#coneverts an image to raw numerical values per pixel
def img_to_pix(upload):
            file = path_to_file(upload)
            with open(file, 'rb') as file:
                RawData = file.read()
            return RawData


#finds relevant details within the
def get_data(words):
    NF="Not Identified"
    data = {
            "Name"        : [],
            "Designation" : [],
            "Company"     : [],
            "Phone"       : [],
            "Email"       : [],
            "Website"     : [],
            "Address"     : [],
            "Other"       : []
            }
    roles = "manager ceo engineer executive analyst counsuldant scientist"
    remainder = words.copy()

    for word in words:
        mail = re.search(r'\w+@+\w+[.]', word)
        phn = re.search(r'^\+?[\d\s-]{6,20}$', word)
        web = re.search('\w*[.]?\w*[.]+\w*', word)
        address =re.search('.*\s(st)+.*',word.lower())

        if mail is not None:
            data["Email"].append(word)
            remainder.remove(word)

        elif phn is not None:
            data["Phone"].append(word)
            remainder.remove(word)

        elif web is not None:
            data["Website"].append(word)
            remainder.remove(word)

        elif address is not None:
            data["Address"].append(word)
            remainder.remove(word)

        else:
            for part in word.lower().split():
                if part in roles:
                    data["Designation"].append(word)
                    remainder.remove(word)


    try:
        email = data.get('Email')[0]
        index_sep = email.index('@')
        pot_name = email[0:index_sep]
        pot_cname = email[index_sep+1:].split('.')[0]
        print(pot_cname)
        for word in remainder:

            if pot_cname.lower() in word.lower():
                data["Company"].append(word)
                remainder.remove(word)
            if pot_name.lower() in word.lower():
                data["Name"].append(word)
                remainder.remove(word)
    except Exception as e:
        print(e)



    if len(data["Name"]) == 0:
        print("ars")
        for word in remainder:
            name = re.search('^\w{4,}\s*', word)
            if name is not None:
                data["Name"].append(word)
                remainder.remove(word)
                break

    data['Other'].append(",".join(remainder))

    for key in data.keys():
        if len(data[key]) < 1:
            data[key].append(NF)
        if len(data[key]) > 1:
            data[key] = [",".join(data[key])]
    print(data)
    return data
