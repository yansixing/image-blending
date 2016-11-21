# -*- coding: utf-8 -*-  
from PIL import Image



#Input two images
front = Image.open("images/front.jpg")
back = Image.open("images/back.jpg")
mask = Image.open("images/mask2.png")

#convert the image to black and white
front_L = front.convert('L')
back_L = back.convert('L')


#get image size
# width = front_L.size[0]
# height = front_L.size[1]


#Allocate memory for images
# front_px = front_L.load()
# back_px = back_L.load()

front_RGBA = front.convert('RGBA')
back_RGBA = back.convert('RGBA')

# datas_RGBA = front_RGBA.getdata()
front_L = front_L.getdata()
back_L = back_L.getdata()

def deleteFrontPixel(data,threshold):
	newData = []
	for item in data:
		if item < threshold:
			newData.append((256,256,256,256))
		else:
			newData.append((0,0,0,0))
	return newData

def deleteBackPixel(data,threshold):
	newData = []
	for item in data:
		if item < threshold:
			newData.append((0,0,0,0))
		else:
			newData.append((256,256,256,256))
	return newData


frontData = deleteFrontPixel(front_L,224)
front_RGBA.putdata(frontData)
front_RGBA.save("images/img.png")

backData = deleteBackPixel(back_L,224)
back_RGBA.putdata(backData)
back_RGBA.save("images/img2.png")

img = Image.blend(front_RGBA,back_RGBA,0.2)
img.save("images/img3.png")
# if __name__ == '__main__':



