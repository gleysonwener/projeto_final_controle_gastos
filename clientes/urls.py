from django.urls import path
from .views import persons_list, persons_new, persons_update, persons_delete

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', persons_list, name='person_list'), # read do crud
    path('new/', persons_new, name='person_new'), # create do crud
    path('update/<int:id>/', persons_update, name='person_update'), # update do crud
    path('delete/<int:id>/', persons_delete, name='person_delete'), # delete do crud
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)