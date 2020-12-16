import cv2
import numpy as np
from pathlib import Path as pw

a = pw(r"./C_HED")
aa = list(filter(pw.is_file, a.glob("**/*")))

b = pw(r"./C_Paintings")
bb = list(filter(pw.is_file, b.glob("**/*")))

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3)) # dilation

for i, j in zip(aa, bb):
    img_a = cv2.imread(str(i), cv2.IMREAD_UNCHANGED)
    img_b = cv2.imread(str(j), cv2.IMREAD_UNCHANGED)
    img_a = img_a.astype(np.uint32)
    img_b = img_b.astype(np.uint32)
    img = img_a + img_b
    img = img.astype(np.float32)
    img = (img / 510) * 255
    img = img.round().astype(np.uint8)
    img[img > 200] = 255
    img[img < 255] = 0
    img = cv2.dilate(img, kernel)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    cv2.imwrite(f"./C/{i.name[: -4]}.jpg", img)
