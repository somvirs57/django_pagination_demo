from django.shortcuts import render
from .models import Entry
from django.core.paginator import Paginator
from django.views.generic import ListView
# Create your views here.

# def entryListing(request):
#     entry_list = Entry.objects.all()
#     paginator = Paginator(entry_list, 3)

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     return render(request, 'home.html', {'page_obj':page_obj,'entries':entry_list})

class EntryListView(ListView):
    model = Entry
    paginate_by = 2
    template_name = 'home.html'