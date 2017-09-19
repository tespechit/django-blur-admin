# -*- coding: utf-8 -*-
from myapp import views
from rest_framework import routers
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'person', views.PersonViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
