# -*- coding: utf-8 -*-
from PIL import Image



#Input two images
front = Image.open("images/front.jpg")
back = Image.open("images/back.jpg")

#convert the image to black and white
front_L = front.convert('L')
back_L = back.convert('L')

# front_L.save("images/front_L.png")
# back_L.save("images/back_L.png")

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
		if item > threshold:
			newData.append((255,255,255,0))
		else:
			newData.append((0,0,0,255))
	return newData

def deleteBackPixel(data,threshold):
	newData = []
	for item in data:
		if item < threshold:
			newData.append((255,255,255,0))
		else:
			newData.append((255,255,255,255))
	return newData

def imageBlending(front,back):
	newData = []
	for index,item in enumerate(front):
		if front[index] == (255,255,255,0) and back[index] == (255,255,255,0):
			newData.append((255,255,255,0))
		if front[index] != (255,255,255,0) and back[index] == (255,255,255,0):
			newData.append((0,0,0,128))
		if front[index] == (255,255,255,0) and back[index] != (255,255,255,0):
			newData.append((255,255,255,128))
		if front[index] != (255,255,255,0) and back[index] != (255,255,255,0):
			newData.append((128,128,128,255))
	return newData



frontData = deleteFrontPixel(front_L,200)
front_RGBA.putdata(frontData)
front_RGBA.save("images/img.png")

backData = deleteBackPixel(back_L,200)
back_RGBA.putdata(backData)
back_RGBA.save("images/img2.png")


front = front_RGBA.getdata()
back = back_RGBA.getdata()
img = imageBlending(front,back)
front_RGBA.putdata(img)
front_RGBA.save("images/img3.png")



# img = Image.blend(front_RGBA,back_RGBA,0.2)
# img.save("images/img3.png")

#print("\nsuccess.\n")
# if __name__ == '__main__':