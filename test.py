import numpy as np
import cv2
import os



path = os.getcwd()

"""Начальное фото"""

path_main = os.path.join(path, "123.png")

img = cv2.imread(path_main)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

"""Шаблолн"""

path_template = os.path.join(path, "template.png")

img_template = cv2.imread(path_template)
template_gray = cv2.cvtColor(img_template, cv2.COLOR_BGR2GRAY)

"""Дейсвтия"""


def cut_image(image, x1, y1, x2, y2):
    return image[y1:y2, x1:x2]

def sort_firts(x):
    return x[0]

def find_xp_area(img_gray, template_image):
    result = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    location_of_matches = np.where(result >= 0.55)

    width_template, height_template = template_gray.shape[::-1]
    for pt in zip(*location_of_matches[::-1]):
        print(pt, (pt[0] + width_template, pt[1] + height_template))
        cv2.rectangle(img_gray, pt, (pt[0] + width_template, pt[1] + height_template), (0, 0, 255), 2)
        img_gray = img[pt[1]:pt[1]+height_template, pt[0] + width_template:None]
        break
    hsv = cv2.cvtColor(img_gray, cv2.COLOR_BGR2HSV)
    min, max = (0, 0, 0), (0, 0, 140)
    thresh = cv2.inRange(hsv, np.array(min), np.array(max))

    # Расширяем области
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 2))
    dilate = cv2.dilate(thresh, kernel, iterations=1)

    "Получаем контуры "
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    numberes = []

    if cnts:
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            numberes.append([x,cut_image(img_gray, x1=x, y1=y, x2=w+x, y2=h+y)])
            print(x, y, w+x, h+y)

        numberes.sort(key=sort_firts)

        cv2.imshow("123", img)
        cv2.waitKey()
        cv2.destroyWindow('123')
        cv2.imshow("123", img_gray)
        cv2.waitKey()
        cv2.destroyWindow('123')
        for key, iage in numberes:
            cv2.imshow("123", iage)
            cv2.waitKey()
            cv2.destroyWindow('123')


if __name__ == "__main__":
    cuted_img = find_xp_area(img_gray, template_gray)

