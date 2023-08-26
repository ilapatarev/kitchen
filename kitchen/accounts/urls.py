from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

	path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
	path('', views.HomeView.as_view(), name='home'),
	path('logout/', views.user_logout, name='logout'),
	path('password_reset/', auth_views.PasswordResetView.as_view(
		template_name='registration/password_reset_form.html',
		email_template_name='registration/password_reset_email.html',
		subject_template_name='registration/password_reset_subject.txt'
	), name='password_reset'),

	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
		template_name='registration/password_reset_done.html'
	), name='password_reset_done'),

	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
		template_name='registration/password_reset_confirm.html'
	), name='password_reset_confirm'),

	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
		template_name='registration/password_reset_complete.html'
	), name='password_reset_complete'),
	path('profile/', views.profile, name='profile'),
	path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)