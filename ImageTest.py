from PIL import Image, ImageDraw
import random


height,width =1000,1000
img = Image.new( 'RGB', (width,height), "white")
draw = ImageDraw.Draw(img)

for i in range(20):
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	sizeExp = random.randint(1,8)
	size = pow(2,sizeExp)
	x = random.randint(0,1000)
	y= random.randint(0,1000)
	#draw.rectangle( (100,100,200,200), fill=(100,100,100), width=10)
	if (x+size) <1000 and (y+size)<1000:
		draw.rectangle( (x,y,x+size,y+size), fill=(r,g,b,10), width=sizeExp)

for i in range(200):
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	sizeExp = random.randint(1,8)
	size = pow(2,sizeExp)
	x = random.randint(0,1000)
	y= random.randint(0,1000)
	#draw.rectangle( (100,100,200,200), fill=(100,100,100), width=10)
	if (x+size) <1000 and (y+size)<1000:
		draw.rectangle( (x,y,x+size,y+size), outline=(r,g,b), width=sizeExp)
		

img.save("Test.jpg")

