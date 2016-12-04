# -*- coding: utf-8 -*-
from __future__ import division
from PIL import Image
from PIL import ImageEnhance


def brightnessHandle():
	back = Image.open("images/back.jpg")
	brightness = ImageEnhance.Brightness(back)
	brightValue = input("输入亮度值（0.1～1.0）：")
	bright_img = brightness.enhance(brightValue)
	bright_img.save("images/dusk.png")

brightnessHandle()

#Input two images
front = Image.open("images/bright.png")
back = Image.open("images/dusk.png")

#covert to 'L' mode
front_L = front.convert('L')
back_L = back.convert('L')

front_RGBA = front.convert('RGBA')
back_RGBA = back.convert('RGBA')

front_L = front_L.getdata()
back_L = back_L.getdata()

#frontHandle函数将front layer中大于阀值的转换成白色透明像素，小于阀值的转为RGBA模式，这两个handle函数主要作用为将灰度模式转为RGBA模式
def frontHandle(data,threshold):
	newData = []
	for item in data:
		if item > threshold:
			newData.append((255,255,255,0))
		else:
			newData.append((item,item,item,255))
	return newData

def backHandle(data):
	newData = []
	for item in data:
		newData.append((item,item,item,255))
	return newData

def imageBlending(front,back):
	newData = []
	for index,item in enumerate(front):
		#core code！⬇️
		frontG = front[index][0]
		backG = back[index][0]
		dstAlpha = round(1 - (frontG - backG)/256, 3)
		dstRGB = int(backG/dstAlpha)
		dstAlpha = 255-(frontG - backG)
		newData.append((dstRGB,dstRGB,dstRGB,dstAlpha))
	return newData

threshold = input("请输入阀值（128～255）：")
frontData = frontHandle(front_L,threshold)
front_RGBA.putdata(frontData)
front_RGBA.save("images/img.png")

backData = backHandle(back_L)
back_RGBA.putdata(backData)
back_RGBA.save("images/img2.png")

front = front_RGBA.getdata()
back = back_RGBA.getdata()
img = imageBlending(front,back)
front_RGBA.putdata(img)
front_RGBA.save("images/img3.png")


print("success.\n")
# if __name__ == '__main__':
