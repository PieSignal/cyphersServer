"""CyphersChat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import cyphers.views
import cyphers.api
import home.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api', include('cyphers.api')),
    path('api/', cyphers.api.api, name='api'),
    path('', home.views.index),
    path('index', home.views.index),
    path('Tables', home.views.table),
    path('detail', home.views.detail),
    path('blank', home.views.blank),
    path('404', home.views._404),
    path('#', home.views.index),
    path('search', home.views.search),
    path('api/todayCyphers', cyphers.api.todayCyphers),
    path('api/UserID/name=<name>', cyphers.api.getUserID),
    path('api/charRank/char=<charname>', cyphers.api.charRank),
    path('api/userInfo/name=<name>', cyphers.api.getUserInfo),
    path('api/allRanking/<args>', cyphers.api.allRanking),
    path('api/allRanking', cyphers.api.allRank),
    path('api/rating/<args>', cyphers.api.rating),
]
