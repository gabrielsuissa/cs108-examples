# path: django/mini_amazon/apps.py
# author: gsuissa@bu.edu
# This page register mini_amazon as a Django App, it is initialised when using the 
# python manage.py startapp command, there is only one app used in mini_amazon (of the same name)

from django.apps import AppConfig


class MiniAmazonConfig(AppConfig):
    name = 'mini_amazon'
