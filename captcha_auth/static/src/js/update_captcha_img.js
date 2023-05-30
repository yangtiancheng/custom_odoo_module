odoo.define('captcha_auth.get_captcha_path', function(require) {
    'use strict';

    var ajax = require('web.ajax');

    function GetCaptchaImgPath() {
        // 调用Odoo控制器并获取图像的路径
        ajax.jsonRpc('/captcha_auth/get_captcha_path', 'call', {})
            .then(function(img_path, captcha_str) {
                // 更新<img>的src属性
                var imageElement = document.getElementsByClassName("captcha_image");
                imageElement.src = img_path;
            });
    }
        function get_captcha_path(){
                    datas = ajax.jsonRpc('/captcha_auth/get_captcha_path', 'call',  {}).then(function(datas) {
                            self.$('#captcha_image').attr('src', datas['img_path']);
                    });
                };
    return GetCaptchaImgPath;
});
