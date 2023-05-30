# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

from captcha.image import ImageCaptcha
import random
import string
import base64
import os


class CaptchaAuth(models.Model):
    _name = 'captcha.auth'

    @classmethod
    def get_new_captcha_auth(cls):
        image = ImageCaptcha(160, 60)  # 图片宽 160 高 60
        characters = string.digits + string.ascii_uppercase + string.ascii_lowercase  # 验证码组成，数字+大写字母+小写字母
        char_num = 4  # 验证码字符个数
        captcha_str = ''.join(random.sample(characters, char_num))
        img = image.generate_image(captcha_str)

        img_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), f"static/src/img/{captcha_str}.jpg")
        img.save(img_path)

        return {
            'img_path':f"captcha_auth/static/src/img/{captcha_str}.jpg",
            'captcha_value':captcha_str,
        }
