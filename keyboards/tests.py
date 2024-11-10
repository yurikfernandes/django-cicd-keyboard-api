# tests.py
import pytest

from django.test import TestCase
from keyboards.models import Keyboard, KeyboardEvaluation

@pytest.mark.django_db()
class TestKeyboardModel(TestCase):
    def test_keyboard_creation(self):
        keyboard = Keyboard.objects.create(
            name="Test Keyboard", description="This is a test keyboard", category="Stage Piano")
        self.assertEqual(keyboard.name, "Test Keyboard")
        self.assertEqual(keyboard.description, "This is a test keyboard")

    def test_keyboard_str_representation(self):
        keyboard = Keyboard.objects.create(
            name="Test Keyboard", description="This is a test keyboard", category="Stage Piano")
        self.assertEqual(str(keyboard), f"{keyboard.name} - {keyboard.category}")
