#!/usr/bin/python3
import cgi
import os

upload_dir = "myupload/"

print("Content-Type: text/plain")
print()

try:
    form = cgi.FieldStorage()
    image_file = form['image']

    if image_file.filename:
        filename = os.path.basename(image_file.filename)  # Use the original filename
        filepath = os.path.join(upload_dir, filename)

        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        with open(filepath, 'wb') as f:
            f.write(image_file.file.read())
        print("Image uploaded successfully")
    else:
        print("No image file received")
except Exception as e:
    print("An error occurred:", str(e))

