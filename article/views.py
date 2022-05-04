from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
from .forms import ArticleForms,Article
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
 
def addarticle(request):
    form = ArticleForms(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request,"Ekleme başarılı...")
        return redirect("index")
    else:
 
        return render(request,"addarticle.html",{"form":form})

def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    return render(request,"dashboard.html",{"articles":articles})

def detail(request,id):
    # article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)
    return render(request,"detail.html",{"article":article})