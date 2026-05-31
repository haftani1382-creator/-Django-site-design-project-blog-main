from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator
from .models import Post
from django.db.models import Q

def index(request):
# گرفتن اطلاعات پست ها
    posts_list = Post.objects.order_by('-post_date').filter(is_published = True)

# ساخت paginator
    paginator = Paginator(posts_list , 6)   
    page = request.GET.get('page')
    paged_post_list = paginator.get_page(page)     

    context = {
        'posts' : paged_post_list
    }

    return render(request , 'posts/posts.html', context)

def post(request , post_id:int):
    post = get_object_or_404(Post , pk=post_id)

    context = {
        'post' : post
     }
        
    return render(request , 'posts/post.html' , context)

def search(request):
    posts = Post.objects.order_by('-post_date').filter(is_published = True)

    if 'search_text' in request.GET:
        search_text = request.GET['search_text']

        if search_text:
            posts = posts.filter(Q(title__icontains = search_text) 
                                 | Q(text__icontains = search_text)
                                 | Q(blogger__name__icontains = search_text) ) # پارامتر سرچ را براساس تایتل و غیره فیلتر کردیم

    context = {
        'posts': posts
    }        

    return render(request , 'posts/search.html' , context)
