from PIL import Image as Image
from PIL import Image as PIL_Image
import requests, os, json, spotipy, datetime
import pprint as pprint
from base64 import b64decode, b64encode
import urllib, zlib, array


stamp =str(datetime.datetime.now().time()).replace('.', '_').replace(':', '_')
orig_img_path = '/home/xilinx/jupyter_notebooks/HackFiles/webcam' +stamp +'.jpg'

!fswebcam  --no-banner --save {orig_img_path} -d /dev/video0 2> /dev/null

img = PIL_Image.open(orig_img_path, 'r')
print(orig_img_path)

from pynq.drivers import Audio
pAudio = Audio()


# Make a get request to get the latest position of the international space station from the opennotify api.
#response = requests.get("https://face.p.mashape.com/faces/group")

# Print the status code of the response.
#print(response.status_code)

# These code snippets use an open-source library. http://unirest.io/python

fkit = bytearray()
with open('webcam'+stamp +'.jpg', "rb") as f:
    byte = f.read(1)
        #while byte:
	    # Do stuff with byte.
	        fkit += f.read(1)


		print('webcam'+stamp +'.jpg')
		response = requests.post("https://face.p.mashape.com/faces/detect?api_key=762aff98c5f0486d8fc33d810f222ee9&api_secret=32d7d1ed807b46c3b0a0f14936403e63",
		  headers={
		      "X-Mashape-Key": "3gehPV4vp8mshJmY9bfJsDfwmg2Gp12PKO7jsnt4UGF3EMyazF",
		          "Content-Type": "application/x-www-form-urlencoded",
			      "Accept": "application/json"
			        },
				  params={
				      "attributes": "mood, age, gender",
				          "detector": "Aggressive"},
					    files = {"file": 
					               ('image', fkit)
						                  #decoded_data#new_image_handle#Image.open(orig_img_path, 'rb')#raw_image_data
								            }
									        
										)
										print(response.text)
										json_obj = json.loads(response.text)
										img
										json_obj

