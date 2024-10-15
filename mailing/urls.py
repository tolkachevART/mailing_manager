from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import HomePageView, MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, \
    MailingDeleteView, ContactsPageView, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView

app_name = MailingConfig.name



urlpatterns = [

    path("", HomePageView.as_view(), name="home"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("mailing_list/", MailingListView.as_view(), name="mailing_list"),
    path('mailing/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('create-mailing/', MailingCreateView.as_view(), name='mailing_create'),
    path("mailing_edit/<int:pk>/", MailingUpdateView.as_view(), name="mailing_edit"),
    path('delete-mailing/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),

    path("client_list/", ClientListView.as_view(), name="client_list"),
    path("client_create/", ClientCreateView.as_view(), name="client_create"),
    path("client_edit/<int:pk>/", ClientUpdateView.as_view(), name="client_edit"),
    path("client_delete/<int:pk>/", ClientDeleteView.as_view(), name="client_delete"),

    path("message_list/", MessageListView.as_view(), name="message_list"),
    path("message/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("message_create/", MessageCreateView.as_view(), name="message_create"),
    path("message_edit/<int:pk>/", MessageUpdateView.as_view(), name="message_edit"),
    path("message_delete/<int:pk>/", MessageDeleteView.as_view(), name="message_delete"),
]
