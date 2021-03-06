from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from . import views
#from django.contrib.auth import views as auth_views#
#from django.urls import reverse_lazy

app_name = 'login'
urlpatterns = [
    path('', views.home, name='home'),
    #path('login/',views.mylogin, name='login'),
    path('register/',views.register, name='register'),
    #path('change_password/',views.change_password, name='change_password'),
    #path('logout/',views.mylogout, name='logout'),
    #path('send/',views.send, name='send'),

    #path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    #path('change/',auth_views.PasswordChangeView.as_view(template_name='password_change_form.html',success_url = reverse_lazy('login:password_change_done')), name='password_change'),
    #path('change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),   
    #path('reset/',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html',email_template_name = 'password_reset_email.html',success_url = reverse_lazy('login:password_reset_complete')),name='password_reset'),
    #path('reset/done',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),    
    #url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',success_url = reverse_lazy('login:password_reset_complete')),name='password_reset_confirm'),
    #path('reset/confirm/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),

    path('login/',views.MyLoginView.as_view(), name='login'),
    path('logout/',views.MyLogoutView.as_view(), name='logout'),
    path('change/',views.MyPasswordChangeView.as_view(), name='password_change'),
    path('change/done/',views.MyPasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),   
    path('reset/',views.MyPasswordResetView.as_view(),name='password_reset'),
    path('reset/done',views.MyPasswordResetDoneView.as_view(),name='password_reset_done'),    
    url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.MyPasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/confirm/done/',views.MyPasswordResetCompleteView.as_view(),name='password_reset_complete'),



]