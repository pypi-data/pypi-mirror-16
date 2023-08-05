# -*- coding: utf-8 -*-
# ++ This file `__init__.py.py` is generated at 4/1/16 6:07 PM ++
from django.http import HttpResponse
from django.views.generic import TemplateView

__author__ = "Md Nazrul Islam<connect2nazrul@gmail.com>"


class IndexView(TemplateView):
    template_name = "hacs/index.html"


class AboutView(TemplateView):
    template_name = "hacs/about.html"
