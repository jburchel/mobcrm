from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST    
from .models import Contact, Church, Prospect, NonProspectInd 
from .forms import ContactForm, ChurchForm, ProspectForm, NonProspectIndForm

@login_required
def contact_list(request):
    contacts = Contact.objects.all()  # Make sure this is a queryset, not a function
    paginator = Paginator(contacts, 10)  # Show 10 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'contacts': page_obj}
    return render(request, 'contacts/contact_list.html', context)

@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    
    contact_types = {
        'CHURCH': (Church, 'churches/church_detail.html', 'church'),
        'PROSPECT': (Prospect, 'prospects/prospect_detail.html', 'prospect'),
        'NON_PROSPECT': (NonProspectInd, 'non_prospect_ind/non_prospect_detail.html', 'non_prospect'),
    }
    
    if contact.contact_type in contact_types:
        model, template, context_name = contact_types[contact.contact_type]
        specific_contact = get_object_or_404(model, contact_ptr_id=contact.id)
        return render(request, template, {context_name: specific_contact})
    else:
        raise Http404("Unknown contact type")

@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        church_form = ChurchForm(request.POST, request.FILES)
        prospect_form = ProspectForm(request.POST, request.FILES)
        non_prospect_form = NonProspectIndForm(request.POST, request.FILES)
        
        if form.is_valid():
            contact = form.save(commit=False)
            if contact.type == 'CHURCH' and church_form.is_valid():
                church = church_form.save(commit=False)
                church.contact_ptr = contact
                church.save()
            elif contact.type == 'PROSPECT' and prospect_form.is_valid():
                prospect = prospect_form.save(commit=False)
                prospect.contact_ptr = contact
                prospect.save()
            elif contact.type == 'NON_PROSPECT' and non_prospect_form.is_valid():
                non_prospect = non_prospect_form.save(commit=False)
                non_prospect.contact_ptr = contact
                non_prospect.save()
            
            contact.save()
            return redirect('contacts:contact_detail', pk=contact.pk)
    else:
        form = ContactForm()
        church_form = ChurchForm()
        prospect_form = ProspectForm()
        non_prospect_form = NonProspectIndForm()
    
    return render(request, 'contacts/contact_form.html', {
        'form': form,
        'church_form': church_form,
        'prospect_form': prospect_form,
        'non_prospect_form': non_prospect_form,
    })

@login_required
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        church_form = ChurchForm(request.POST, instance=getattr(contact, 'church', None))
        prospect_form = ProspectForm(request.POST, instance=getattr(contact, 'prospect', None))
        non_prospect_form = NonProspectIndForm(request.POST, instance=getattr(contact, 'nonprospectind', None))
        
        if form.is_valid():
            contact = form.save(commit=False)
            if contact.type == 'CHURCH' and church_form.is_valid():
                church = church_form.save(commit=False)
                church.contact_ptr = contact
                church.save()
            elif contact.type == 'PROSPECT' and prospect_form.is_valid():
                prospect = prospect_form.save(commit=False)
                prospect.contact_ptr = contact
                prospect.save()
            elif contact.type == 'NON_PROSPECT' and non_prospect_form.is_valid():
                non_prospect = non_prospect_form.save(commit=False)
                non_prospect.contact_ptr = contact
                non_prospect.save()
            
            contact.save()
            return redirect('contacts:contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
        church_form = ChurchForm(instance=getattr(contact, 'church', None))
        prospect_form = ProspectForm(instance=getattr(contact, 'prospect', None))
        non_prospect_form = NonProspectIndForm(instance=getattr(contact, 'nonprospectind', None))
        
    return render(request, 'contacts/contact_form.html', {
        'form': form,
        'church_form': church_form,
        'prospect_form': prospect_form,
        'non_prospect_form': non_prospect_form,
    })

@login_required
@require_POST
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contacts:contact_list')

def church_list(request):
    churches = Church.objects.all()
    paginator = Paginator(churches, 10)  # Show 10 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'churches/church_list.html', {'churches': page_obj})

def church_detail(request, pk):
    church = get_object_or_404(Church, pk=pk)
    return render(request, 'churches/church_detail.html', {'churches': church})

@login_required
def church_create(request):
    if request.method == 'POST':
        form = ChurchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:church_list')
    else:
        church_form = ChurchForm()
    return render(request, 'contacts/contact_form.html', {            
        'church_form': church_form,
    })

@login_required
def church_delete(request, pk):
    church = get_object_or_404(Church, pk=pk)
    if request.method == 'POST':
        church.delete()
        messages.success(request, 'Church deleted successfully.')
        return redirect('contacts:church_list')
    return render(request, 'churches/church_confirm_delete.html', {'church': church})

def prospect_list(request):
    prospects = Prospect.objects.all()
    paginator = Paginator(prospects, 10)  # Show 10 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'prospects/prospect_list.html', {'prospects': page_obj})

def prospect_detail(request, pk):
    prospect = get_object_or_404(Prospect, pk=pk)
    return render(request, 'prospects/prospect_detail.html', {'prospect': prospect})

@login_required
def prospect_create(request):
    if request.method == 'POST':
        form = ProspectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:prospect_list')
    else:
        form = ProspectForm()
    return render(request, 'prospects/prospect_form.html', {'form': form})

@login_required
def prospect_delete(request, pk):
    prospect = get_object_or_404(Church, pk=pk)
    if request.method == 'POST':
        prospect.delete()
        messages.success(request, 'Prospct deleted successfully.')
        return redirect('contacts:prospect_list')
    return render(request, 'prospcects/prospect_confirm_delete.html', {'prospect': prospect})

def non_prospect_list(request):
    non_prospects = NonProspectInd.objects.all()
    paginator = Paginator(non_prospects, 10)  # Show 10 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'non_prospect_ind/non_prospect_list.html', {'nonprospects': page_obj})

def non_prospect_detail(request, pk):
    non_prospect = get_object_or_404(NonProspectInd, pk=pk)
    return render(request, 'non_prospect_ind/non_prospect_detail.html', {'non_prospect': non_prospect})

@login_required
def non_prospect_create(request):
    if request.method == 'POST':
        form = NonProspectIndForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:non_prospect_list')
    else:
        form = NonProspectIndForm()
    return render(request, 'non_prospect_ind/non_prospect_form.html', {'form': form})

@login_required
def non_prospect_delete(request, pk):
    non_prospect = get_object_or_404(Church, pk=pk)
    if request.method == 'POST':
        non_prospect.delete()
        messages.success(request, 'Contact deleted successfully.')
        return redirect('contacts:non_prospect_list')
    return render(request, 'non_prospect_ind/non_prospect_confirm_delete.html', {'non_prospect': non_prospect})