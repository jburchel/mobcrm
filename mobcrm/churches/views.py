from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Church

@login_required
def church_detail(request, pk):
    church = get_object_or_404(Church, pk=pk)
    return render(request, 'churches/church_detail.html', {'church': church})

@login_required
def church_delete(request, pk):
    church = get_object_or_404(Church, pk=pk)
    if request.method == 'POST':
        church.delete()
        messages.success(request, 'Church deleted successfully.')
        return redirect('contacts:church_list')
    return render(request, 'churches/church_confirm_delete.html', {'church': church})