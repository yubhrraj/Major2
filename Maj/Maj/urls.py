from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.SimpleRouter()
# router.register(r'task', views.taskViewset)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post/', views.RecvDataRequest.as_view()),
    url(r'^$', views.kid_upload_view, name='form_kid')
    # url(r'^', include(router.urls)),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)