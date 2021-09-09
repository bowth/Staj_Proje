from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    
	path('', views.store, name="store"),
    path('page/<int:page>',views.store, name="store"),

    path('signup/', SignUpView.as_view(), name='signup'),
    
	path('sepet/', views.sepet, name="sepet"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/',views.processOrder, name="process_order"),
	path('contacts/',views.contacts, name="contacts"),
    path('search/',views.filter_store, name="search"),
    path('detail/<int:item_id>',views.detail_view, name="detail"),
	path('cartClear',views.cart_clear,name="sepet_clear")
	


]
