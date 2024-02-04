
from tutorials import views 
from django.contrib import admin
from django.urls import re_path

"""django.conf.urls.url() was deprecated in Django 3.0, and is removed in Django 4+.
The easiest fix is to replace url() with re_path(). re_path uses regexes like url, so you only have to update the import and replace url with re_path.
"""

urlpatterns = [ 
    re_path(r'^api/tutorials$', views.tutorial_list),
    re_path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    re_path(r'^api/tutorials/published$', views.tutorial_list_published)
]