import cv2
# get the image location
img_location = 'D:\\'
filename = 'test.jpg'
#read in the image
img = cv2.imread(img_location+filename)
#convert
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#invert the image
inverted_gray_image = 255 - gray_image
#blur the image by gauss
blurred_img = cv2.GaussianBlur(inverted_gray_image,(21,21),0)
inverted_blurred_img = 255- blurred_img
pencil_sketch = cv2.divide(gray_image,inverted_blurred_img,scale=256.0)
#show image
cv2.imshow('Orgiginal Image', img)
cv2.imshow('New Image',pencil_sketch)
cv2.waitKey(0)