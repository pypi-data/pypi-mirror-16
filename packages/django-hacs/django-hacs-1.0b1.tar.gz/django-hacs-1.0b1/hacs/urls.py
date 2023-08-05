# -*- coding: utf-8 -*-
# ++ This file `urls.py` is generated at 3/18/16 3:49 PM ++
from django.conf.urls import url

from .views import IndexView
from .views import AboutView
from .views.admin import select2_contenttypes_view

__author__ = "Md Nazrul Islam<connect2nazrul@gmail.com>"

urlpatterns = [
    url(r'^$', name='index', view=IndexView.as_view()),
    url(r'^about/', name='about', view=AboutView.as_view()),
    url(r'^select2\-(?P<content_type>[a-z]+)\-list/$',
        name='select2_contenttypes_list', view=select2_contenttypes_view),
]

handler403 = "hacs.views.errors.permission_denied"
handler404 = "hacs.views.errors.page_not_found"
