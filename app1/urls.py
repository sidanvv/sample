from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='main'),
    path('student/',views.student,name='student'),
    path('teacher/',views.teacher,name='teacher'),
    path('details/',views.details,name='details'),
    path('contact/',views.contact,name='contact'),
    path('form/',views.user_form_view,name='user_form'),
    path('success/',views.sucess_view,name='success'),
    path('contact_details/',views.contact_details),
    path('contact2/',views.contact2,name='contact2'),
    path('employform/',views.employee_form_view,name='employform'),
    path('employlist/',views.employlist,name='employlist'),
    path('delete/<int:id>',views.emp_detele,name='emp_delete'),
    path('edit/<int:id>',views.emp_edit,name='emp_edit'),
    path('update/<int:id>',views.emp_update_form,name='emp_update'),
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('userlogin/',views.user_login,name='userlogin')






]
