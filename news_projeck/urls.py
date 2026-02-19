from django.urls import path
from .views import (
    home_page_view,
    news_list,
    news_detail,
    contact_us,
    about_us,
    page_404
)

urlpatterns = [

    path('', home_page_view, name='home_page_view'),

    path('news/', news_list, name='news_list'),
    path('news/<int:id>/', news_detail, name='news_detail'),
    path('contact/', contact_us, name='contact_us'),
    path('about/', about_us, name='about'),
    path('404/', page_404, name='404'),
]