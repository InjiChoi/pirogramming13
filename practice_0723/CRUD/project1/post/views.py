from django.shortcuts import render, redirect
from django.urls import reverse

from . import models

# Create your views here.
def main(request):
    return render(request, 'post/main.html')

def post_list(request):
    all_posts = models.Post.objects.all()
    # all_posts는 Post모델로 만들어진 Post 객체가 리스트로 담긴다.
    ctx = {
        "posts":all_posts
        #나중에 템플릿에 posts라고 쓰면 all_posts를 가져와서 쓴다
    }
    return render(request, 'post/post_list.html', ctx)

def post_detail(request, pk1):
    post1 = models.Post.objects.get(pk=pk1)
    ctx = {
        "post":post1
    }
    return render(request, 'post/post_detail.html', ctx)

def post_create(request):
    if request.method == 'POST':
        new_Post = models.Post.objects.create(
            title = request.POST.get("tit"),
            writer = request.POST.get('wri'),
            content = request.POST.get("con"),
        )

        new_pk = new_Post.pk
        address = '/post/post_list/'+str(new_pk)+'/'
        #return redirect(address)
        return redirect(reverse('post:post_d', kwargs={'pk1':new_pk}))
    # get 요청 처리
    else:
        return render(request, 'post/post_create.html')