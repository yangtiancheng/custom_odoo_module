odoo.define("new_page", function (require) {
    'use strict';

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var session = require('web.session');
    var ControlPanelMixin = require('web.ControlPanelMixin');

    var QWeb = core.qweb;

    var one_new_page = AbstractAction.extend(ControlPanelMixin, {
        template: 'new_page_template',
    });
    core.action_registry.add('new_page', one_new_page);
    return one_new_page;
});