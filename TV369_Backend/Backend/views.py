import re
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import User, NewsArticle
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import requests
from .get_csrf_token import extract_csrf_token
from django.http import JsonResponse

@csrf_exempt
def create_user(request):
    full_name = request.POST['full_name']
    username = request.POST['username']
    password = request.POST['password']
    
    User.objects.create(full_name=full_name, username=username, password=password)
    return JsonResponse({"result":'User created successfully!'})
    return render(request, 'create_user.html')
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username, password=password)
        if user:
            return JsonResponse({"result":'Login successful!'})
        else:
            return JsonResponse({"result":'Invalid username or password!'})
            
    return render(request, 'login.html')
@csrf_exempt
def show_users(request):
    users = User.objects.all()
    return render(request, 'show_users.html', {'users': users})

@csrf_exempt
def create_news_article(request):
    if request.method == 'POST':
        author = request.POST['author']
        title = request.POST['title']
        cover_image = request.FILES['cover_image']
        content = request.POST['content']
        categories = request.POST['categories']
        NewsArticle.objects.create(author=author, title=title, cover_image=cover_image, content=content, categories=categories)
        return JsonResponse({"result":'News article created successfully!'})
        # return HttpResponse('News article created successfully!')
    return render(request, 'create_news_article.html')
@csrf_exempt
def show_10_news_articles(request):
    news_articles = NewsArticle.objects.order_by('-created_at')[:10]

    # Serialize the model instance to JSON
    articles = serializers.serialize('json', news_articles)
    
    print(articles)
    return JsonResponse({"result":articles})


@csrf_exempt
def show_all_news_articles(request):
    news_articles = NewsArticle.objects.all()

    # Serialize the model instance to JSON
    articles = serializers.serialize('json', news_articles)
    
    # response = requests.get("http://localhost:8000/trending/")
    # csrf_token = extract_csrf_token(response)
    # print("token")
    # print(csrf_token)
    return JsonResponse({"result":articles})
    return render(request, 'show_news_articles.html', {'news_articles': news_articles})

@csrf_exempt
def show_news_articles_by_category(request, category):
    news_articles = NewsArticle.objects.filter(categories=category).order_by('-created_at')[:10]

    # Serialize the model instance to JSON
    articles = serializers.serialize('json', news_articles)
    
    return JsonResponse({"result":articles})

    return render(request, 'show_news_articles.html', {'news_articles': news_articles})

@csrf_exempt
def trending(request):
    news_articles = NewsArticle.objects.all.order_by('-created_at')[:10]
    articles = serializers.serialize('json', news_articles)
    return JsonResponse({"result":articles})
    return render(request, 'show_news_articles.html', {'news_articles': news_articles})

