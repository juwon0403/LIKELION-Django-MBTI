from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm


# Create your views here.

def home(request):
    return render(request, 'index.html')

def mbtitest(request):
    return render(request, 'mbtitest.html')

def mbtiresult(request):
    if request.method == 'POST':
        ei_value = request.POST.get('EI')
        sn_value = request.POST.get('SN')
        ft_value = request.POST.get('FT')
        jp_value = request.POST.get('JP')
        return render(request, 'mbtiresult.html', {'ei_value': ei_value , 'sn_value': sn_value ,'ft_value': ft_value ,'jp_value': jp_value  })
    

def new(request):
    return render(request, 'new.html')

def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

def formcreate(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'form_create.html', {'form' : form})


def modelformcreate(request):
    if request.method == 'POST':
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form' : form})




    

