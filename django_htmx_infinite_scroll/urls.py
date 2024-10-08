"""URLs for DjangoHtmxInfiniteScroll app."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.book, name="book"),
    path("book-page", views.book_page, name="book-page"),
]
