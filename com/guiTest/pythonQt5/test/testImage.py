from PIL import Image

img = Image.open("../QFlowLayout/cache/covergif/123.gif")
# img = Image.open("../QFlowLayout/cache/coverimg/IMG_20180729_110141.jpg")

print (img.size)
print (img.size[0])
print (img.size[1])
print (img.format)