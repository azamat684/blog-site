from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = "index.html"