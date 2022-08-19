from django.urls import path, include
from tickets import views
from tickets.models import LogIdeas



home_list_view = views.HomeListView.as_view(
    queryset=LogIdeas.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="tickets/home.html",
)

urlpatterns = [
    path('', home_list_view, name='home'),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('delete_item/<int:pk>', views.delete_item, name="delete_item"),
    path('edit_item/<int:pk>', views.edit_item, name="edit_item"),
]

