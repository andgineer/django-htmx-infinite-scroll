"""Tests for the BookPage model."""

from django.test import TestCase

from django_htmx_infinite_scroll.models import BookPage


class BookPageModelTest(TestCase):
    """Test cases for the BookPage model."""

    def test_book_page_creation(self) -> None:
        """Test creating a BookPage instance."""
        page = BookPage.objects.create(number=1, content="Test content")
        self.assertEqual(page.number, 1)
        self.assertEqual(page.content, "Test content")
        self.assertEqual(str(page), "1")

    def test_book_page_ordering(self) -> None:
        """Test that BookPage instances are ordered by number."""
        BookPage.objects.create(number=3, content="Third page")
        BookPage.objects.create(number=1, content="First page")
        BookPage.objects.create(number=2, content="Second page")

        pages = list(BookPage.objects.all())
        self.assertEqual(pages[0].number, 1)
        self.assertEqual(pages[1].number, 2)
        self.assertEqual(pages[2].number, 3)

    def test_book_page_str_representation(self) -> None:
        """Test the string representation of BookPage."""
        page = BookPage.objects.create(number=42, content="Answer to everything")
        self.assertEqual(str(page), "42")
