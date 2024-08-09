from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST   
from django.db import transaction 
from .models import Contact, Church, Prospect, NonProspectInd 
from .forms import ContactForm, ChurchForm, ProspectForm, NonProspectIndForm

# CONTACT VIEWS

@login_required
def contact_list(request):
    contacts = Contact.objects.all()
    churches = Church.objects.all()
    prospects = Prospect.objects.all()
    non_prospects = NonProspectInd.objects.all()

    all_contacts = list(contacts) + list(churches) + list(prospects) + list(non_prospects)
    
    print(f"Number of contacts: {len(all_contacts)}")
    print(f"Contacts: {len(contacts)}, Churches: {len(churches)}, Prospects: {len(prospects)}, Non-Prospects: {len(non_prospects)}")

    paginator = Paginator(all_contacts, 10)  # Show 10 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'contacts': page_obj,
        'page_obj': page_obj,
    }
    return render(request, 'contacts/contact_list.html', context)

@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    
    print(f"Contact type: {contact.type}")  # Debug print
    
    contact_types = {
        'church': (Church, 'churches/church_detail.html', 'church'),
        'prospect': (Prospect, 'prospects/prospect_detail.html', 'prospect'),
        'non_prospect_individual': (NonProspectInd, 'non_prospect_ind/non_prospect_detail.html', 'non_prospect'),
    }
    
    if contact.type.lower() in contact_types:
        model, template, context_name = contact_types[contact.type.lower()]
        try:
            specific_contact = model.objects.get(contact_ptr_id=contact.id)
            return render(request, template, {context_name: specific_contact})
        except model.DoesNotExist:
            print(f"Failed to find {model.__name__} with contact_ptr_id={contact.id}")  # Debug print
            raise Http404(f"{model.__name__} not found")
    else:
        print(f"Unknown contact type: {contact.type}")  # Debug print
        raise Http404("Unknown contact type")

@login_required
def contact_create(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        contact_type = request.POST.get('type')
        
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.type = contact_type
            contact.save()
            
            if contact_type == 'church':
                church_form = ChurchForm(request.POST)
                if church_form.is_valid():
                    church = church_form.save(commit=False)
                    church.contact_ptr = contact
                    church.save()
            elif contact_type == 'prospect':
                prospect_form = ProspectForm(request.POST)
                if prospect_form.is_valid():
                    prospect = prospect_form.save(commit=False)
                    prospect.contact_ptr = contact
                    prospect.save()
                    # Update the contact object to point to the prospect
                    contact.prospect = prospect
                    contact.save()
            elif contact_type == 'non_prospect_individual':
                non_prospect_form = NonProspectIndForm(request.POST)
                if non_prospect_form.is_valid():
                    non_prospect = non_prospect_form.save(commit=False)
                    non_prospect.contact_ptr = contact
                    non_prospect.save()
            
            print(f"Created contact of type: {contact.type}")  # Debug print
            return redirect('contacts:contact_list')
        else:
            print(f"Contact form errors: {contact_form.errors}")  # Debug print
    else:
        contact_form = ContactForm()
        church_form = ChurchForm()
        prospect_form = ProspectForm()
        non_prospect_form = NonProspectIndForm()
    
    return render(request, 'contacts/contact_form.html', {
        'contact_form': contact_form,
        'church_form': church_form,
        'prospect_form': prospect_form,
        'non_prospect_form': non_prospect_form,
    })

@login_required
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, request.FILES, instance=contact)
        
        if contact.type == 'church':
            specific_form = ChurchForm(request.POST, request.FILES, instance=contact.church)
        elif contact.type == 'prospect':
            specific_form = ProspectForm(request.POST, request.FILES, instance=contact.prospect)
        elif contact.type == 'non_prospect_individual':
            specific_form = NonProspectIndForm(request.POST, request.FILES, instance=contact.nonprospectind)
        else:
            specific_form = None

        if contact_form.is_valid() and (specific_form is None or specific_form.is_valid()):
            contact = contact_form.save()
            if specific_form:
                specific_form.save()
            return redirect('contacts:contact_detail', pk=contact.pk)
    else:
        contact_form = ContactForm(instance=contact)
        
        if contact.type == 'church':
            specific_form = ChurchForm(instance=contact.church)
        elif contact.type == 'prospect':
            specific_form = ProspectForm(instance=contact.prospect)
        elif contact.type == 'non_prospect_individual':
            specific_form = NonProspectIndForm(instance=contact.nonprospectind)
        else:
            specific_form = None
    
    return render(request, 'contacts/contact_form.html', {
        'contact_form': contact_form,
        'specific_form': specific_form,
        'contact': contact
    })

@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact_type = contact.get_type_display()
        contact.delete()
        messages.success(request, f'{contact_type} has been deleted successfully.')
        return redirect('contacts:contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})

# CHURCH VIEWS

def church_list(request):
    churches = Church.objects.all()
    paginator = Paginator(churches, 10)  # Show 10 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'churches/church_list.html', {'churches': page_obj})

def church_detail(request, pk):
    church = get_object_or_404(Church, pk=pk)
    return render(request, 'churches/church_detail.html', {'churches': church})

# PROSPECT VIEWS

def prospect_list(request):
    prospects = Prospect.objects.all()
    paginator = Paginator(prospects, 10)  # Show 10 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'prospects/prospect_list.html', {'prospects': page_obj})

def prospect_detail(request, pk):
    prospect = get_object_or_404(Prospect, pk=pk)
    return render(request, 'prospects/prospect_detail.html', {'prospect': prospect})

# NON-PROSPECT INDIVIDUAL VIEWS

def non_prospect_list(request):
    non_prospects = NonProspectInd.objects.all()
    paginator = Paginator(non_prospects, 10)  # Show 10 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'non_prospect_ind/non_prospect_list.html', {'nonprospects': page_obj})

def non_prospect_detail(request, pk):
    non_prospect = get_object_or_404(NonProspectInd, pk=pk)
    return render(request, 'non_prospect_ind/non_prospect_detail.html', {'non_prospect': non_prospect})
