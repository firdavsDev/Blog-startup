from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
# users view
from users import views as user_view
#auth
from django.contrib.auth import views as auth_views
#rasmning url path olish uchun
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('_admin/', admin.site.urls), #admin
    #Login/logout/register - urls
    path('rigester/',user_view.rigester,name='rigester'), 
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/logout.html'),name='logout'),
    #blog
    path('', include('blog.urls')), #blog uchun
    path('profile/',user_view.profile, name='profile'),
    #Password reset
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'),name='password_reset_complete'),
    #social
    path('oauth/', include('social_django.urls', namespace='social')),

    #API
    path('api/', include('BlogAPI.urls')), #blogAPI uchun

    # URl shorter
    path('', include('shorter.urls')),
    #translate
    path('', include('tarjimon.urls')),
    #ToDo
    path('', include('todo.urls')),

    #cv 
    path('cv/',TemplateView.as_view(template_name='cv.html'), name ='cv'),
    path('site/', include('portofolia.urls')),
]
#Debug = True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)