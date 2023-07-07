from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from django.conf import include,urls    
# from django.conf import admin   
from Backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_user/', views.create_user, name='create_user'),
    path('login/', views.login, name='login'),
    path('show_users/', views.show_users, name='show_users'),
    path('create_news_article/', views.create_news_article, name='create_news_article'),
    path('show_10_articles/', views.show_10_news_articles, name='show_10_articles'),
    path('show_all_articles/', views.show_all_news_articles, name='show_all_articles'),
    path('show_category_articles/', views.show_news_articles_by_category, name='show_category_articles'),
    path('trending/', views.trending, name='trending'),
    path('article/', views.single_article, name='article'),
    path('create_category/',views.create_category,name='create_category'),
    path('show_category/',views.show_category,name='show_category'),
    path('create_author/',views.create_author,name='create_author'),
    path('show_author/',views.show_author,name='show_author'),
    path('import_data/',views.import_data,name='import_data'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
