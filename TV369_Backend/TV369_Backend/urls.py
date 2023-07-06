from django.urls import path

from Backend import views

urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    path('login/', views.login, name='login'),
    path('show_users/', views.show_users, name='show_users'),
    path('create_news_article/', views.create_news_article, name='create_news_article'),
    path('show_10_articles/', views.show_10_news_articles, name='show_10_articles'),
    path('show_all_articles/', views.show_all_news_articles, name='show_all_articles'),
    path('show_category_articles/', views.show_news_articles_by_category, name='show_category_articles'),
    path('trending/', views.trending, name='trending'),
    path('article/', views.single_article, name='article'),
]
