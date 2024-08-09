from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Church

@login_required
def church_detail(request, pk):
    church = get_object_or_404(Church, pk=pk)
    return render(request, 'churches/church_detail.html', {'church': church})
