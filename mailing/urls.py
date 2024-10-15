from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import HomePageView, MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, \
    MailingDeleteView

app_name = MailingConfig.name

urlpatterns = [

    path("", HomePageView.as_view(), name="home"),
    path("mailing_list/", MailingListView.as_view(), name="mailing_list"),
    path('mailing/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('create-mailing/', MailingCreateView.as_view(), name='mailing_create'),
    path("mailing_edit/<int:pk>/", MailingUpdateView.as_view(), name="mailing_edit"),
    path('delete-mailing/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
]
