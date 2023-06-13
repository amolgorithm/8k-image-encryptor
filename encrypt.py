from PIL import Image #importing Pillow for image reading and writing
import numpy as np
import os



message = "A dog on a computer :-). LOL!!" #Message to send
keys = {
	'x': 1049,
	'y': 430,
	'i': 3429,
	'j': 1574
}


images = ["img01.jpg", "img02.jpg", "img03.jpg", "img04.jpg", "img05.jpg"]

for i in range(len(images)):
	print("In Progress: Image {}".format(i+1))
	
	img = Image.open(r"./encryption_images/{}".format(images[i]))
	pixels = img.load()
	img_width, img_height = img.size
	pixel_values = []


	for y in range(img_height):
		inner_list = []
		for x in range(img_width):
			inner_list.append(pixels[x, y])
		
		pixel_values.append(inner_list)


	message_bytearray = " ".join(format(ord(x), 'b') for x in message).split(" ")
	pixel_values[keys['y']][keys['x']] = (int(message_bytearray[i*6], 2), int(message_bytearray[i*6+1], 2), int(message_bytearray[i*6+2], 2))
	pixel_values[keys['j']][keys['i']] = (int(message_bytearray[i*6+3], 2), int(message_bytearray[i*6+4], 2), int(message_bytearray[i*6+5], 2))

	array = np.array(pixel_values, dtype=np.uint8)
	new_image = Image.fromarray(array)
	new_image.save("./encrypted_images/ofcrypted0{}.png".format(i+1))
	
	os.system('cls' if os.name == 'nt' else 'clear')
	print("Image {} Done!".format(i+1))
