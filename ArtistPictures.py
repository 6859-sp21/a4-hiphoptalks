import os
import glob
import csv
import json
from PIL import Image

basewidth = 50

artists = []
with open("rapper_names.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        artists.append(row[0])

with open("rappers.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Artists","Pictures"])
    for artist in artists:
        # Resize Images
        img = Image.open(os.getcwd() + "/artistsPictures/" + artist + ".png")
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save(os.getcwd() + "/artistsPictures/" + artist + "_resized.png", optimize = True, quality = 1)

        # Write image file names
        writer.writerow([artist, "/artistsPictures/" + artist + "_resized.png"])
