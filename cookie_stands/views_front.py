from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Cookie_stands


class Cookie_standsListView(LoginRequiredMixin, ListView):
    template_name = "Cookie_stands/Cookie_stands_list.html"
    model = Cookie_stands
    context_object_name = "Cookie_stands"


class Cookie_standsDetailView(LoginRequiredMixin, DetailView):
    template_name = "Cookie_stands/Cookie_stands_detail.html"
    model = Cookie_stands


class Cookie_standsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "Cookie_stands/Cookie_stands_update.html"
    model = Cookie_stands
    fields = "__all__"


class Cookie_standsCreateView(LoginRequiredMixin, CreateView):
    template_name = "Cookie_stands/Cookie_stands_create.html"
    model = Cookie_stands
    fields =  "__all__"


class Cookie_standsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "Cookie_stands/Cookie_stands_delete.html"
    model = Cookie_stands
    success_url = reverse_lazy("Cookie_stands_list")
