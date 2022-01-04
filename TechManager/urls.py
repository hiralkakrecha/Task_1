from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from TechManager import views as tech_views

import TechManager

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('TechManager/', include("TechManager.urls")),
    path('blogview/',tech_views.BlogView.as_view(), name="blogview"),
]
