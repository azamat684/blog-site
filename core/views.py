from django.shortcuts import render
from .models import BlogPost
from collections import defaultdict

def blog_home(request):
    template_name = 'blog.html'
    # Get all published posts ordered by creation date
    posts = BlogPost.objects.filter(status='published').order_by('-created_at')
    
    # Group posts by year
    grouped_posts = defaultdict(list)
    for post in posts:
        year = post.created_at.year
        grouped_posts[year].append(post)
    
    # Pass grouped posts to the template
    return render(request, 'blog.html', {'posts': grouped_posts})
