from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^books/$', views.BookListView.as_view(), name='books'),
	url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
	url(r'^authors/$', views.authorListView.as_view(), name='authors'),
	url(r'^authors/(?P<pk>\d+)$', views.authorDetailView.as_view(), name='author-detail'),
]

urlpatterns += [   
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),

]
