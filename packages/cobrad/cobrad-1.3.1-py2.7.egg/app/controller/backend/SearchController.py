#!/usr/bin/env python2
# coding: utf-8
# file: SearchController.py

from flask import request, render_template, jsonify, redirect

from . import ADMIN_URL
from app import web
from app.CommonClass.ValidateClass import ValidateClass
from app.models import CobraLanguages, CobraVuls, CobraRules


__author__ = "lightless"
__email__ = "root@lightless.me"


# search_rules_bar
@web.route(ADMIN_URL + '/search_rules_bar', methods=['GET'])
def search_rules_bar():

    if not ValidateClass.check_login():
        return redirect(ADMIN_URL + '/index')

    languages = CobraLanguages.query.all()
    vuls = CobraVuls.query.all()

    data = {
        'languages': languages,
        'vuls': vuls,
    }

    return render_template('backend/index/search_rules_bar.html', data=data)


# search rules
@web.route(ADMIN_URL + '/search_rules', methods=['POST'])
def search_rules():

    if not ValidateClass.check_login():
        return redirect(ADMIN_URL + '/index')

    if request.method == 'POST':

        vc = ValidateClass(request, "language", "vul")
        ret, msg = vc.check_args()
        if not ret:
            return jsonify(tag="danger", msg=msg)

        rules = None

        if vc.vars.language == 'all' and vc.vars.vul == 'all':
            rules = CobraRules.query.all()
        elif vc.vars.language == 'all' and vc.vars.vul != 'all':
            rules = CobraRules.query.filter_by(vul_id=vc.vars.vul).all()
        elif vc.vars.language != 'all' and vc.vars.vul == 'all':
            rules = CobraRules.query.filter_by(language=vc.vars.language).all()
        elif vc.vars.language != 'all' and vc.vars.vul != 'all':
            rules = CobraRules.query.filter_by(language=vc.vars.language, vul_id=vc.vars.vul).all()
        else:
            return 'error!'

        cobra_vuls = CobraVuls.query.all()
        cobra_lang = CobraLanguages.query.all()
        all_vuls = {}
        all_language = {}
        for vul in cobra_vuls:
            all_vuls[vul.id] = vul.name
        for lang in cobra_lang:
            all_language[lang.id] = lang.language

        # replace id with real name
        for rule in rules:
            try:
                rule.vul_id = all_vuls[rule.vul_id]
            except KeyError:
                rule.vul_id = 'Unknown Type'
            try:
                rule.language = all_language[rule.language]
            except KeyError:
                rule.language = 'Unknown Language'

        data = {
            'rules': rules,
        }

        return render_template('backend/rule/rules.html', data=data)

