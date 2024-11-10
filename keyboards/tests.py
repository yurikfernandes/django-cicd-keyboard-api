# tests.py
import pytest

from django.test import TestCase
from keyboards.models import Keyboard, KeyboardEvaluation

@pytest.mark.django_db()
class TestKeyboardModel(TestCase):
    def test_keyboard_creation(self):
        keyboard = Keyboard.objects.create(name="Test Keyboard", description="This is a test keyboard")
        self.assertEqual(keyboard.name, "Test Keyboard")
        self.assertEqual(keyboard.description, "This is a test keyboard")

    def test_keyboard_str_representation(self):
        keyboard = Keyboard.objects.create(name="Test Keyboard", description="This is a test keyboard")
        self.assertEqual(str(keyboard), "Test Keyboard")

@pytest.mark.django_db()
class TestKeyboardEvaluationModel(TestCase):
    def test_keyboard_evaluation_creation(self):
        keyboard = Keyboard.objects.create(name="Test Keyboard", description="This is a test keyboard")
        evaluation = KeyboardEvaluation.objects.create(keyboard=keyboard)
        self.assertEqual(evaluation.keyboard, keyboard)

    def test_keyboard_evaluation_str_representation(self):
        keyboard = Keyboard.objects.create(name="Test Keyboard", description="This is a test keyboard")
        evaluation = KeyboardEvaluation.objects.create(keyboard=keyboard)
        self.assertEqual(str(evaluation), f"{keyboard.name} Evaluation")