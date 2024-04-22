from django.urls import path
from bot.views import ImageStoreView


urlpatterns = [
    path('message/', ImageStoreView.as_view(), name='image-store'),
]