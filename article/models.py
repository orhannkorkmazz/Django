from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Article(models.Model): 
    author=models.ForeignKey ("auth.user",on_delete=models.CASCADE, verbose_name=('Yazar')) 
    title=models.CharField(max_length=50, verbose_name=('Başlık'))
    content=RichTextField( verbose_name=('İçerik'))
    category=models.CharField(max_length=50,verbose_name=('Tür'),default="")
    created_date=models.DateTimeField(auto_now_add=True, verbose_name=('Oluşturulma Tarihi'))
    image = models.FileField(blank=True,null=True,verbose_name=('Resim Yükle'))#her makalenin dosyası yüklenmek zorunda değil
    
    def __str__(self):
        return self.title
    CATEGORY_CHOICES = (
    ('Bilisim', 'Bilişim'),
    ('Eğitim', 'Eğitim'),
    ('Edebi', 'Edebi'),
    ('Gazete', 'Gazete'),
    # Diğer kategori seçeneklerini buraya ekleyin
)
   
class Comment(models.Model):
    title=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="makale",related_name="comments")
    author=models.CharField(max_length=50, verbose_name=('Yazan'))
    content=RichTextField(max_length=100,verbose_name=('İçerik'))
    created_date=models.DateTimeField(auto_now_add=True, verbose_name=('Oluşturulma Tarihi'))
    def __str__(self):
        return self.content
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_picture', null=True, blank=True)
    def __str__(self):
        return self.user.username
