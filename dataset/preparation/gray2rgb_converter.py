import cv2
import numpy as np
from pathlib import Path as pw

a = pw(r"./A")
aa = list(filter(pw.is_file, a.glob("**/*")))

for f in aa:
    img = cv2.imread(str(f), cv2.IMREAD_UNCHANGED)
    if img.ndim == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    cv2.imwrite(f"./A_/{f.name}", img)
