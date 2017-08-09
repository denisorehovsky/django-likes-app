from django.conf.urls import include, url
from django.contrib import admin

# Register API
apipatterns = [
    url(r'^', include('tweets.api.urls')),
]

urlpatterns = [
    url(r'^api/v1/', include(apipatterns, namespace='api')),
    url(r'^admin/', admin.site.urls),
]
