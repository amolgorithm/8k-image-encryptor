from PIL import Image #importing Pillow for image reading


keys = {
	'x': 1049,
	'y': 430,
	'i': 3429,
	'j': 1574
}


images = ["ofcrypted01.png", "ofcrypted02.png", "ofcrypted03.png", "ofcrypted04.png", "ofcrypted05.png"]

print("Decrypting...")
print("Decrypted message:")

for i in range(len(images)):
	img = Image.open(r"./encrypted_images/{}".format(images[i]))
	pixels = img.load()
	img_width, img_height = img.size
	pixel_values = []


	for y in range(img_height):
		inner_list = []
		for x in range(img_width):
			inner_list.append(pixels[x, y])
		
		pixel_values.append(inner_list)


	char1, char2, char3 = pixel_values[keys['y']][keys['x']]
	char4, char5, char6 = pixel_values[keys['j']][keys['i']]

	print(char1.to_bytes((char1.bit_length() + 7) // 8, 'big').decode(), char2.to_bytes((char2.bit_length() + 7) // 8, 'big').decode(), char3.to_bytes((char3.bit_length() + 7) // 8, 'big').decode(),
	char4.to_bytes((char4.bit_length() + 7) // 8, 'big').decode(), char5.to_bytes((char5.bit_length() + 7) // 8, 'big').decode(), char6.to_bytes((char6.bit_length() + 7) // 8, 'big').decode(), sep="", end="")
