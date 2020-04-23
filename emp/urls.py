from .views import home, deleteEmp, updateEmp, addEmp
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('edit/<int:id>', updateEmp, name='updateEmp'),
    path('delete/<int:id>', deleteEmp, name='deleteEmp'),
    path('add', addEmp, name='addEmp'),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
