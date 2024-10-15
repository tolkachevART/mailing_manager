from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from mailing.forms import ClientForm, MessageForm
from mailing.models import Mailing, Client, Message


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


class ContactsPageView(TemplateView):
    template_name = "mailing/contacts.html"


class ClientListView(ListView):
    model = Client
    template_name = 'clients/client_list.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('mailing:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('mailing:client_list')



class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'clients/client_confirm_delete.html'
    success_url = reverse_lazy('mailing:client_list')


class MessageListView(ListView):
    model = Message
    template_name = 'messages/message_list.html'


class MessageDetailView(DetailView):
    model = Message
    template_name = 'messages/message_detail.html'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'messages/message_form.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'messages/message_form.html'
    success_url = reverse_lazy('mailing:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'messages/message_confirm_delete.html'
    success_url = reverse_lazy('mailing:message_list')
