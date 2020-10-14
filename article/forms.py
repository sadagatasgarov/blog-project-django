from django import forms
""" from django.forms import ModelForm
from myapp.models import Artile """
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'article_file']


""" # Creating a form to add an article.
 form = ArticleForm()

# Creating a form to change an existing article.
 article = Article.objects.get(pk=1)
 form = ArticleForm(instance=article)    
     """
