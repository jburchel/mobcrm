from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm

@login_required
def contact_list(request):
    contact_list = Contact.objects.all().order_by('-last_contact')
    paginator = Paginator(contact_list, 25)  # Show 25 contacts per page

    page_number = request.GET.get('page')
    contacts = paginator.get_page(page_number)

    context = {
        'contacts': contacts,
    }
    return render(request, 'contacts/contact_list.html', context)

@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('contacts:contact_detail', pk=contact.pk)
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})

@login_required
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save()
            return redirect('contacts:contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {'form': form})

@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contacts:contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})