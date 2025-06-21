import cv2
import numpy as np
import string
import os
import matplotlib.pyplot as plt

d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}
# Load the image
image_path = r"C:\Users\satya\Desktop\stegno\cover1.jpg"
x = cv2.imread(image_path)
xrgb = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
plt.imshow(xrgb)   # Show original image
plt.axis('off')
plt.show()
key = "123"
text = "secret"
x_enc = x.copy()   # Copy image to encrypt

# Encrypt using XOR and pixel modification
n, m, z = 0, 0, 0  
for i in range(len(text)):
    text_char = text[i]
    key_char = key[i % len(key)]
    org_val = x_enc[n, m, z]
    new_val = d[text_char] ^ d[key_char]  
    x_enc[n, m, z] = new_val
    z += 1
    if z == 3:
        z = 0
        m += 1
    if m == x_enc.shape[1]:
        m = 0
        n += 1
    if n == x_enc.shape[0]:
        raise Exception("Image is too small to hide this message.")
cv2.imwrite("encrypted_image.png", x_enc)
print("Encryption done. Encrypted image saved as 'encrypted_image.png'.")
x_new = cv2.imread("encrypted_image.png")

n, m, z = 0, 0, 0
decrypted_text = ""

for i in range(len(text)):
    key_char = key[i % len(key)]
    enc_val = x_new[n, m, z]
    dec_val = enc_val ^ d[key_char]
    decrypted_text += c[dec_val]
    z += 1
    if z == 3:
        z = 0
        m += 1
    if m == x_new.shape[1]:
        m = 0
        n += 1
print("Decrypted message:", decrypted_text)
