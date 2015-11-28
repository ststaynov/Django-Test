from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^grades/', include('grades.urls', namespace="grades")),
    url(r'^admin/', include(admin.site.urls)),
]
