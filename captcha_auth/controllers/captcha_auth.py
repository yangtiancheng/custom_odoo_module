# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.tools.translate import _

import logging
import werkzeug

from odoo import http, _
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.addons.web.controllers.main import ensure_db, Home
from odoo.addons.web_settings_dashboard.controllers.main import WebSettingsDashboard as Dashboard
from odoo.exceptions import UserError
from odoo.http import request

_logger = logging.getLogger(__name__)

class CaptchaAuthController(Home):

    @http.route('/captcha_auth/get_captcha_path', auth='none', type='json')
    def get_captcha_path(self):
        captcha_obj = request.env['captcha.auth']
        captcha_data = captcha_obj.sudo().get_new_captcha_auth()
        request.session['captcha_code'] = captcha_data['captcha_value']
        return captcha_data

    @http.route()
    def web_login(self, *args, **kw):
        ensure_db()
        if kw.get('captcha', False) and kw.get('captcha', 'False1').lower() != request.session.get('captcha_code', 'False2').lower():
            request.params.update({'error': _("验证码错误，请重新登录！")})
            response = request.render('web.login', request.params.copy())
            response.headers['X-Frame-Options'] = 'DENY'
            return response
        response = super(CaptchaAuthController, self).web_login(*args, **kw)
        return response