from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home' ),
    path('register/',views.register,name='register' ),
    path('login/',views.login_attemp,name='login' ),
    path('mailsent/',views.verify,name='mailsent' ),
    path('sendMail/',views.sendMail,name='sendMail' ),
    path('logout/',views.logout_attemp,name='logout' ),
    path('about/',views.about,name='about' ),
    path('contact/',views.contact,name='contact' ),
    # path('resend/<int:code1>',views.resend,name='resend' ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
