from django.conf.urls import url
from .views import root
from .views import customer
from .views.customer import CustomerListView
from django.contrib.auth import views as auth_views

urlpatterns = [
	# root
	url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': 'core:login'}, name='logout'),
	url(r'^home/$', root.home, name='home'),

	# customer
	url(r'^customer/add/$', customer.add, name='add'),
	url(r'^customer/list/$', CustomerListView.as_view(), name='list'),
	url(r'^customer/edit/(?P<customer_id>[a-z\d]+)/?$', customer.edit, name='edit'),
	url(r'^customer/delete/(?P<customer_id>[a-z\d]+)/?$', customer.delete,name='delete'),
]