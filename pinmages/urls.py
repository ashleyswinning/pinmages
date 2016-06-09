"""pinmages URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^tagsdescription', views.tagsdescription),
    url(r'^tags', views.tags),
    url(r'^search', views.search),
    url(r'^gridedit', views.gridedit),
    url(r'^grid', views.grid),
    url(r'^viewgrid', views.viewgrid),
    url(r'^imageinfo', views.imageinformation),
    url(r'^imageedit', views.imageedit),
    url(r'^image/(?P<id>\d+)/download', views.download_image),
    url(r'^image', views.image)
]
