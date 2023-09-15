
from django.urls import include, path
from .models import Kanvass
from .views import KanvassListView, KanvassDetailView, KanvassUpdateView, KanvassCreateView

urlpatterns = [
    path("list/", KanvassListView.as_view(), name='kanvass_list'),
    path("create/<int:pk>/", KanvassCreateView.as_view(), name='kanvass_create'),
    path("detail/<int:pk>/", KanvassDetailView.as_view(), name='kanvass_details'),
    path("update/<int:pk>/", KanvassUpdateView.as_view(), name='kanvass_update'),
]