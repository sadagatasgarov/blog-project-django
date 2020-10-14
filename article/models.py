from django.db import models
from ckeditor.fields import RichTextField

# 1 Create your models here. //python manage.py startapp article//


class Article(models.Model):
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Yaratilma tarihi")
    article_file = models.FileField(
        blank=True, null=True, verbose_name="Makaleye  fotograf ekeyin")

    def __str__(self):
        return self.title
   
    class Meta:
        ordering = ('-created_date',)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="isim")
    comment_content = models.CharField(max_length=50, verbose_name="yorum")
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Yaratilma tarihi")
    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ('-created_date',)
