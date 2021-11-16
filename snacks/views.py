from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
                                    ListView,
                                    DetailView,
                                    DeleteView,
                                    CreateView,
                                    UpdateView)
from .models import Snack                                    
# Create your views here.
class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack
    context_object_name = "snack_list"
    

class SnackListDetail(DetailView):
    template_name = "snack_detail.html"
    model = Snack
    context_object_name = "snack_object"    


class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["title","purchaser","description"]
 

class SnackUpdatView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ["title","purchaser","description"]

class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_view")

