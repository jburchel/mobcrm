from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
from .models import Prospect


@login_required
def prospect_list(request):
    prospects = Prospect.objects.all().order_by(('contact__last_name'), ('contact__first_name'))
    return render(request, 'prospects/prospect_list.html', {'prospects': prospects})

@login_required
def prospect_detail(request, prospect_id):
    prospect = get_object_or_404(Prospect, id=prospect_id)
    # recent_interactions = Interaction.objects.filter(contact=prospect).order_by('-date')[:5]
    
    context = {
        'prospect': prospect,
        # 'recent_interactions': recent_interactions,
    }
    return render(request, 'prospects/prospect_detail.html', context)

