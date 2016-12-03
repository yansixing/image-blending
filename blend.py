# -*- coding: utf-8 -*-
from __future__ import division
from PIL import Image

#Input two images
front = Image.open("images/bright.png")
back = Image.open("images/dusk.png")

#convert the image to black and white
front_L = front.convert('L')
back_L = back.convert('L')

front_L.save("images/front_L.png")
back_L.save("images/back_L.png")

#get image size
# width = front_L.size[0]
# height = front_L.size[1]

front_RGBA = front.convert('RGBA')
back_RGBA = back.convert('RGBA')

front_L = front_L.getdata()
back_L = back_L.getdata()

def deleteFrontPixel(data,threshold):
	newData = []
	for item in data:
		if item > threshold:
			newData.append((255,255,255,0))
		else:
			newData.append((item,item,item,255))
	return newData

def deleteBackPixel(data,threshold):
	newData = []
	for item in data:
		newData.append((item,item,item,255))
	return newData

def imageBlending(front,back):
	newData = []
	for index,item in enumerate(front):
		frontG = front[index][0]
		backG = back[index][0]
		dstAlpha = round(1 - (frontG - backG)/256, 3)
		dstRGB = int(backG/dstAlpha)
		dstAlpha = 255-(frontG - backG)
		newData.append((dstRGB,dstRGB,dstRGB,dstAlpha))
	return newData



frontData = deleteFrontPixel(front_L,224)
front_RGBA.putdata(frontData)
front_RGBA.save("images/img.png")

backData = deleteBackPixel(back_L,224)
back_RGBA.putdata(backData)
back_RGBA.save("images/img2.png")

front = front_RGBA.getdata()
back = back_RGBA.getdata()
img = imageBlending(front,back)
front_RGBA.putdata(img)
front_RGBA.save("images/img3.png")



# img = Image.blend(front_RGBA,back_RGBA,0.2)
# img.save("images/img3.png")

print("\nsuccess.\n")
# if __name__ == '__main__':
