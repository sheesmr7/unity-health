from django.urls import path
from.import views


urlpatterns=[
    
    path('', views.home_page, name='home_page'),
    path('doctors.html', views.doctors, name='doctors'),
    path('contact.html', views.contacts, name='contacts'),
    path('blog.html', views.blogs, name='blogs'),
    path('blog-details.html', views.blog_details, name='blog_details'),
    path('about.html', views.about_us, name='about_us'),
    path('registration.html', views.registers, name='registers'),
    
]