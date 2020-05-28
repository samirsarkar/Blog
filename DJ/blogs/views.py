from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'Samir',
        'title': 'Blog Post 1',
        'content': 'This is just a dummy post 1',
        'date_posted': 'May 28, 2020'
    },
    {
        'author': 'Sankar',
        'title': 'Blog Post 2',
        'content': 'This is just a dummy post 2',
        'date_posted': 'May 29, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogs/home.html', context=context)


def about(request):
    return render(request, 'blogs/about.html', {'title': 'About'})
