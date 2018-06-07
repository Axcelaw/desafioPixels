file = pickAFile()
img = makePicture(file)
imgPixels = getPixels(img)
redPixels = 0

for pixel in imgPixels:
  redValue = getRed(pixel)
  greenValue = getGreen(pixel)
  blueValue = getBlue(pixel)
  
  if redValue == 255 and greenValue == 0 and blueValue == 0:
    redPixels += 1

print('Total de pixels vermelhos: ' + str(redPixels))