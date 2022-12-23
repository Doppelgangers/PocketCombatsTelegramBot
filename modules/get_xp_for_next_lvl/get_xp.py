import os
from typing import Tuple
import config
import cv2
import numpy as np
import pytesseract


class Action_xp_page:
    path_template = os.path.join(os.getcwd(), "modules", "get_xp_for_next_lvl", "templates")

    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = config.PATH_TESSERACT
        self.template = cv2.imread(os.path.join(self.path_template, "template.png"), 0)

    def find_xp_area(self, image) -> np.ndarray:
        """
        Находит фрагмент с xp персонажа и обрезает фото
        :param image:
        :return: image
        """
        result = cv2.matchTemplate(image, self.template, cv2.TM_CCOEFF_NORMED)
        location_of_matches = np.where(result >= 0.8)
        width_template, height_template = self.template.shape[::-1]

        for pt in zip(*location_of_matches[::-1]):
            # print(pt, (pt[0] + width_template, pt[1] + height_template))
            cv2.rectangle(image, pt, (pt[0] + width_template, pt[1] + height_template), (0, 0, 255), 2)
            cut_image = image[pt[1]:pt[1]+height_template, pt[0] + width_template:None]
            return cut_image

    @staticmethod
    def img_to_str(image: np.ndarray) -> str:
        img_number = cv2.resize(image, None, fx=4, fy=4)
        return pytesseract.image_to_string(img_number)

    @staticmethod
    def str_to_int(line: str) -> tuple[int, int]:
        line = line.replace(")", "")
        line = line.split("(")
        return int(line[0]), int(line[1])

    def get_xp(self, image_path) -> tuple[int, int] | None:
        my_img = cv2.imread(image_path, 0)
        img_xp = self.find_xp_area(my_img)

        # cv2.imshow('image', img_xp)
        # cv2.waitKey(0)

        str_xp = self.img_to_str(img_xp)
        # print(str_xp)
        now_xp, need_xp = self.str_to_int(str_xp)
        return now_xp, need_xp
