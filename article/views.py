from django.shortcuts import render,redirect,get_object_or_404
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,"index.html")
# Create your views here.
def about(request):
    return render(request,"about.html")

def articles(request):
    anahtar = request.GET.get("anahtar")
    selected_category = request.GET.get('category')
    
    articles = Article.objects.all()

    if anahtar:
        articles = articles.filter(title__icontains=anahtar)

    if selected_category and selected_category != 'Hepsi':
        articles = articles.filter(category=selected_category)

    return render(request, "articles.html", {"articles": articles})

@login_required
def dashboard(request):
    articles=Article.objects.filter(author=request.user)
    form=ArticleForm
    context={
        "articles":articles,
        "form":form
    }
    return render(request,"dashboard.html",context)
@login_required
def addarticle(request):
    form=ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False)#sadece form.save() yaparak kayıt işlemi gerçekleşebilir fakat bu formdan alınan bilgide yazar bilgisi olduğu için ve biz makalede sadece başlık ve içerik bilgisi istediğimizi için hata ile karşılaşırız 
        article.author=request.user
        article.save()
        messages.success(request,"Makale başarıyla oluşturuldu")
        return redirect("index")
    
    return render(request,"addarticle.html",{"form":form} )

def dashboard_detail(request,id):
    article=Article.objects.filter(id=id).first
    article=get_object_or_404(Article,id=id)#1
    comments = article.comments.all()#1 ve 2 numaralı kodlar yorumları göstermek için yazıldı
    return render(request,"detail.html",{'article':article,'comments':comments})
@login_required
def update(request,id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)  # Formu ilgili makale ile doldurun

        if form.is_valid():
            form.save()  # Makaleyi güncelleyin
            messages.success(request,"Makale başarıyla güncelleştirildi.")
            return redirect("dashboard")  # Güncelleme işlemi başarılıysa detay sayfasına yönlendirin
            
    else:
        form = ArticleForm(instance=article)  # GET isteği için formu hangi başlıkla ve içerikle olduğu şekilde doldurun

    return render(request, "update.html", {"form": form, "article": article})
@login_required
def delete(request,id):
    article = get_object_or_404(Article, id= id)
    article.delete()
    return redirect('dashboard')
def comment(request,id):
    article = get_object_or_404(Article, id=id)
    
    if request.method == "POST":
        author = request.POST.get("author")
        content = request.POST.get("content")

        newComment = Comment(author  = author, content = content)

        newComment.title = article

        newComment.save()
    return redirect("detail",id=id)


def article_list(request):
   pass




   
