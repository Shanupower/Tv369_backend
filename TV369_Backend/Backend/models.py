from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'  # Set the collection name explicitly

class NewsArticle(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='cover_images/')
    content = models.TextField()
    categories = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news_article'  # Set the collection name explicitly
