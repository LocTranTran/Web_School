from django.shortcuts import render # type: ignore
from datetime import datetime
from .models import Post
from django.shortcuts import render, get_object_or_404 # type: ignore
from django.shortcuts import render, redirect # type: ignore
from .forms import PostForm

posts = Post.objects.all()  # Lấy danh sách tất cả các bài viết
def base(request):
    return redirect('home')

def home(request):
    time = datetime.now()
    time_day = time.strftime('%A')
    context = {
        'time': time,
        'time_day': time_day,
        'posts':posts
    }
    return render(request, 'home.html', context)

def post_detail(request, post_id):
    posts = Post.objects.all()  # Lấy danh sách tất cả các bài viết
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post,'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create_post')  # Chuyển hướng đến trang hiển thị danh sách bài viết
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})



def introduce(request):
    
    context = {
        'posts':posts
    }
    return render(request, 'introduce.html', context)