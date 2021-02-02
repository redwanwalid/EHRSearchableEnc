# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here. It will auto give you the page, you will
#find it once you login as an django admin in the admin console page.

from .models import Article
from .models import StaffInfo
from .models import PatientInfo

admin.site.register(Article)
admin.site.register(StaffInfo)
admin.site.register(PatientInfo)