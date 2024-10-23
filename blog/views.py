from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    return render(request, 'home.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Save the post to the database
            return redirect('home')  # Redirect to the home page after submission
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})