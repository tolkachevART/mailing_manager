from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from mailing.models import Mailing


class HomePageView(TemplateView):
    template_name = "mailing/home.html"


class MailingListView(ListView):
    model = Mailing
    paginate_by = 6

    def get_queryset(self):
        return Mailing.objects.all().order_by('-created_at')


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ['clients', 'message', 'periodicity', 'status']
    success_url = reverse_lazy('mailings:mailing_detail')
    template_name = 'mailing/mailing_form.html'

    def form_valid(self, form):
        mailing = form.save()
        return redirect('mailing:mailing_detail', mailing.pk)


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ['clients', 'message', 'periodicity', 'status']
    template_name = 'mailing/mailing_form.html'

    def get_success_url(self):
        return reverse('mailing:mailing_detail', kwargs={'pk': self.object.pk})


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')
