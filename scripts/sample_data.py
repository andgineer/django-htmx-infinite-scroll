"""Populate the database with sample data."""
from faker import Faker

from django_htmx_infinite_scroll.models import BookPage

fake = Faker()

for i in range(100):
    sentences = " ".join(fake.sentences(25))  # pylint: disable=invalid-name
    BookPage.objects.create(number=i + 1, content=sentences)  # pylint: disable=no-member