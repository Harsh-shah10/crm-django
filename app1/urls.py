from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.homepage,name='homepage'),
    # path('login/',views.user_login,name='login'), # for email validn
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.user_register,name='register'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)