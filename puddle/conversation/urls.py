from django.urls import path

from .views import new_conversation, inbox, detail

app_name = "conversation"

urlpatterns = [
    path('new/<int:item_pk>/', new_conversation, name="new"),
    path('inbox/', inbox, name="inbox"),
    path('<int:pk>/', detail, name="detail"),
]
