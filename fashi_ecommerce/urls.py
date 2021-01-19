from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('accounts/',include('UserRegistration.urls')),
    path('shop/',include('shop.urls')),
    path('blog/',include('blog.urls')),
    path('order/',include('order.urls')),
    path('payment/',include('payment.urls')),
    path('contact/',include('contact.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)