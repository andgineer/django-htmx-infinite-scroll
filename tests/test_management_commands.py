"""Tests for management commands."""

from django.core.management import call_command
from django.test import TestCase

from django_htmx_infinite_scroll.models import BookPage


class AddPagesCommandTest(TestCase):
    """Test cases for the add-pages management command."""

    def test_add_pages_command_creates_pages(self) -> None:
        """Test that the add-pages command creates BookPage instances."""
        initial_count = BookPage.objects.count()
        call_command("add-pages")
        final_count = BookPage.objects.count()
        self.assertEqual(final_count - initial_count, 100)

    def test_add_pages_command_with_existing_pages(self) -> None:
        """Test add-pages command appends pages after existing ones."""
        BookPage.objects.create(number=5, content="Existing page")
        call_command("add-pages")

        highest_page = BookPage.objects.latest("number")
        self.assertEqual(highest_page.number, 105)

        pages_with_content = BookPage.objects.filter(content__contains="Existing page")
        self.assertEqual(pages_with_content.count(), 1)

    def test_add_pages_command_generates_content(self) -> None:
        """Test that add-pages command generates non-empty content."""
        call_command("add-pages")
        pages = BookPage.objects.all()

        for page in pages:
            self.assertTrue(len(page.content) > 0)
            self.assertIsInstance(page.content, str)
