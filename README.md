# 8k Image Encryptor

Let's say you are in _Naustralia_ and you have a friend in _Scireland_. You need to send a secret message to your friend, but you cannot merely do this as your message can be easily picked up by the evil HinderSnatoofs, who want to read your message. So, electronically, this has been solved using encryption. Typically, your message would be converted to ciphertext using a unicode key and sent to your friend. Once the friend receives this, he uses that same key to decrypt the ciphertext to read the real message. However, I am changing this. I propose to you a new idea. (Or at least, I hope it's new, as I do not know if anyone else ever thought about this in history).

**Note: This is not really a project, as you can see there are only like two files. This is just introducing my idea and seeing ways of how you help the "HinderSnatoofs" find my message.**

## My idea
High resolution images have a lot of pixels. Especially 8k images, which can contain up to 33 million pixels! Each pixel has an rgb value that pixel leds emits the color of. Rgb values, in modern 64-bit computers, take up 3 bytes. With 3 bytes, you can store three UTF-8 characters, a byte each. So, my idea is that, in an image, you can replace two random pixels (to which you and your friend know the coordinates of), with the rgb value. Yes, that does not make sense, but let me explain.

My idea is to first take the three characters of the message, convert each character into a byte-worth binary string, then convert each binary string into an unsigned integer worth a byte, which means it is 0-255. That is exactly the value for RGB quanitities. So, replace the rgb values of the pixel with each unsigned integer. In an image full of 33 million pixels, it would be really hard to find the anomaly, especially if it blends in to its background. To figure the anomaly pixel out using brute force, it would take a really long time, unless quantum computer, of course.

## How to use
Run the `encrypt.py` file first, then the `decrypt.py` file. Basically, encrypt.py is you fron Naustralia and decrypt.py is your friend from Scireland. This may take up to a minute, as high revolution images are involved.

## Challenge
The challenge I throw out to all of you: I know my design can be malviolently decrypted by the "HinderSnatoofs". I just do not how, but that is the challenge for you. Let me know if you thought of an algorithm to crack my design. It does not need to be really efficient, but it also does not need to be such that the "HinderSnatoofs" require 5 IBM supercomputers to crack my little message.

**This is just an analogy and a fun, small project to show the importance and greatness of cryptography. My idea is not literally a foolproof cryptographic technique**
**Technically, my technique would be really hard to solve unless you have a quantum computer with enough perfect qubits, but I am not even close to being experienced in cryptography**
