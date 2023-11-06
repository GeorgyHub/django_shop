from django.urls import path
from .views import homepage, itempage

urlpatterns = [
    path('', homepage, name="home"),
    path('item/<int:item_id>/', itempage, name="itempage"),
]