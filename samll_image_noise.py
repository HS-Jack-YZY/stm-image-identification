import cv2
import numpy as np

# Load the image
image_path = "samples/small_image/small_image_02.jpg"
image = cv2.imread(image_path)

# Add noise to each pixel
noise = np.round(np.random.normal(0, 1, image.shape) * 50)
noisy_image = image + noise

# Save the noisy image
noisy_image_path = "samples/noisy_image/noisy_image_02.jpg"
cv2.imwrite(noisy_image_path, noisy_image)
