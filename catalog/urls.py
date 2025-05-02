from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),

    #views the details of that book specified by the pk
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]