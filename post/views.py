from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone

# Create your views here.




def main(request):
    blogs = Post.objects.all().order_by('-id') #모델로부터 객체의 목록을 전달, 쿼리셋
    return render(request, 'main.html', {'blogs': blogs})

def index(request):
    blogs = Post.objects #모델로부터 객체의 목록을 전달, 쿼리셋
    return render(request, 'index.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Post, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})

def new(request):
    if request.method=='POST':
        blog = Post()
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        try:
            blog.image = request.FILES['image']
        except:
            pass
        blog.save()
        return redirect('/post/main')
    else:
        return render(request, 'new.html')

def renew(request,blog_id):
    blog_r=get_object_or_404(Post,pk=blog_id)
    return render(request,'renew.html',{'blog':blog_r})

def update(request,blog_id):
    blog = get_object_or_404(Post,pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/post/detail/' + str(blog.id))

def delete(request,blog_id):
    blog_d=get_object_or_404(Post,pk=blog_id)
    blog_d.delete()
    return redirect('/post/main/')

def create(request):
    blog =  get_object_or_404(Post,pk=blog_id)
    blog.user=request.user
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/post/detail/' + str(blog.id))  


    
