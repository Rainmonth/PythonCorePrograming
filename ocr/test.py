import pytesseract
from PIL import Image
# path = "test.jpg"
# im = Image.open(path)
# im = im.convert('L')
# im.save("result.jpg")
path2 = "result.jpg"
path3 = "test3.jpg"
im2 = Image.open(path3)

print(pytesseract.image_to_string(im2.convert("L"), lang='chi_sim'))
# pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
# text = pytesseract.image_to_string(Image.open('E://figures/other/poems.jpg'))


# print(text)
