import cv2
path = 'solar-system.jpg'
image = cv2.imread("solar-system.jpg")
cv2.putText(
    image,
    "Sun",
    (65, 60),
    cv2.FONT_HERSHEY_COMPLEX,
    2,
    (255, 255, 255))
cv2.putText(
    image,
    "Mercury",
    (110, 250),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255))
cv2.putText(
    image,
    "Venus",
    (188, 170),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255))
cv2.putText(
    image,
    "Earth",
    (288, 270),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255))
cv2.putText(
    image,
    "Mars",
    (379, 269),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255))
cv2.putText(
    image,
    "Jupiter",
    (569, 379),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255))
cv2.putText(
    image,
    "Saturn",
    (769, 329),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255))
cv2.putText(
    image,
    "Uranus",
    (969, 310),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255))
cv2.putText(
    image,
    "Neptune",
    (1100, 310),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255))
cv2.imshow("output", image)
cv2.waitKey(0)
cv2.imwrite("Output", image)
