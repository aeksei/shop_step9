from django.urls import path
from .views import *



urlpatterns = [
    path('', IndexView.as_view()),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<int:page_id>', ShopView.as_view()),    
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('wishlist/pic/', lambda request: redirect("https://picsum.photos/100"), name='wishlist-pic')
]
 