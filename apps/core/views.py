from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods     #  GET , POST برای محدود های متد های مجاز 
from django.db import transaction    # برای اجرای اتمیک عملیات دیتابیس همه یا هیج

from .models import (
    HeroSection,
)


def home_view(request):
    hero_section = HeroSection.objects.first()
    context = {
        'hero_section':hero_section,
    }
    return render(request, 'index.html', context)