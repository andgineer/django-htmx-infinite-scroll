"""Tests for views in the DjangoHtmxInfiniteScroll app."""

from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse

from django_htmx_infinite_scroll.models import BookPage


class BookViewTest(TestCase):
    """Test cases for the book view."""

    def setUp(self) -> None:
        """Set up test data."""
        self.page = BookPage.objects.create(number=1, content="Test page content")

    def test_book_view_with_existing_page(self) -> None:
        """Test book view returns correct page."""
        response = self.client.get(reverse("book"), {"page-number": "1"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test page content")
        self.assertContains(response, "<h2")

    def test_book_view_defaults_to_page_1(self) -> None:
        """Test book view defaults to page 1 when no page number provided."""
        response = self.client.get(reverse("book"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test page content")

    def test_book_view_with_nonexistent_page(self) -> None:
        """Test book view with page that doesn't exist."""
        with self.assertRaises(BookPage.DoesNotExist):
            self.client.get(reverse("book"), {"page-number": "999"})


class BookPageViewTest(TestCase):
    """Test cases for the book_page view."""

    def setUp(self) -> None:
        """Set up test data."""
        self.page = BookPage.objects.create(number=1, content="Test page content")

    def test_book_page_view_with_existing_page(self) -> None:
        """Test book_page view returns correct partial HTML."""
        response = self.client.get(reverse("book-page"), {"page-number": "1"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test page content")
        self.assertContains(response, 'id="page-1"')

    def test_book_page_view_defaults_to_page_1(self) -> None:
        """Test book_page view defaults to page 1 when no page number provided."""
        response = self.client.get(reverse("book-page"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test page content")

    def test_book_page_view_with_nonexistent_page(self) -> None:
        """Test book_page view with page that doesn't exist."""
        response = self.client.get(reverse("book-page"), {"page-number": "999"})
        self.assertEqual(response.status_code, 500)
        self.assertContains(response, "error: Page 999 not found", status_code=500)

    def test_book_page_view_returns_http_response(self) -> None:
        """Test book_page view returns HttpResponse instance."""
        response = self.client.get(reverse("book-page"), {"page-number": "1"})
        self.assertIsInstance(response, HttpResponse)
