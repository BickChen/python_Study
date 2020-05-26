import random, string, os
from captcha.image import ImageCaptcha
from PIL import Image
"""
使用 Python 生成类似于下图中的字母验证码图片
"""
def Verification_code_generation():
    ver_data = ''.join(random.sample(string.ascii_lowercase + string.digits, 4))
    captcha_image = Image.open(ImageCaptcha().generate(ver_data))
    path = './captcha_image'
    if not os.path.exists(path):
        os.makedirs(path)
    filename = ver_data + '.png'
    captcha_image.save(path + os.path.sep + filename)
    return ver_data

print(Verification_code_generation())
