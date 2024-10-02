import cv2

# Read the image from file
image = cv2.imread('path_to_your_image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original image
cv2.imshow('Original Image', image)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
