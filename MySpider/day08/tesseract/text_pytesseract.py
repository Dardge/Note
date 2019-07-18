import pytesseract
# 标准库：图片处理
from PIL import Image

img = Image.open('u=3035392207,102688918&fm=27&gp=0.jpg')
result = pytesseract.image_to_string(img)

print(result)
