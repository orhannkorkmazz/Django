from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
class Article(models.Model): 
    author=models.ForeignKey ("auth.user",on_delete=models.CASCADE, verbose_name=('Yazar')) 
    title=models.CharField(max_length=50, verbose_name=('Başlık'))
    content=RichTextField( verbose_name=('İçerik'))
    created_date=models.DateTimeField(auto_now_add=True, verbose_name=('Oluşturulma Tarihi'))
    image = models.FileField(blank=True,null=True,verbose_name=('Resim Yükle'))#her makalenin dosyası yüklenmek zorunda değil
    def __str__(self):
        return self.title
class Comment(models.Model):
    title=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="makale",related_name="comments")
    author=models.CharField(max_length=50, verbose_name=('Yazan'))
    content=RichTextField(max_length=100,verbose_name=('İçerik'))
    created_date=models.DateTimeField(auto_now_add=True, verbose_name=('Oluşturulma Tarihi'))
    def __str__(self):
        return self.content

