from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = "index.html"
    
class BlogView(TemplateView):
    template_name = "blog.html"
    
class AboutView(TemplateView):
    template_name = "about.html"
    
class ContactView(TemplateView):
    template_name = "contact.html"