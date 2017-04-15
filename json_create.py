#!/usr/bin/env python2
import os
import json



file = open("data/example.json", "w")
img_folder = "data/images/"
ant_folder = "data/annotations/"

data = {}

data["labels"] = []
data["labels"].append("road(background)")
data["labels"].append("sky")
data["labels"].append("building")
data["labels"].append("people")
data["labels"].append("tree")
data["labels"].append("bikes")
data["labels"].append("cars")

data["imageURLs"] = []





for filename in os.listdir(img_folder):
    if filename.endswith(".jpg"): 
        data["imageURLs"].append(img_folder + filename)

data["annotationURLs"] = []


for filename in os.listdir(img_folder):
    path = ant_folder + "seg_" + filename.split('.')[0] + ".png"
    print(path)
    if os.path.isfile(path):
        data["annotationURLs"].append(path)
    else:
        data["annotationURLs"].append(ant_folder + "default.png")


json.dump(data, file, indent=4)
file.close()
