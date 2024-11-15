from django.contrib import admin

from .models import Keyboard, KeyboardFeature, KeyboardEvaluation

admin.site.register(Keyboard)
admin.site.register(KeyboardFeature)
admin.site.register(KeyboardEvaluation)
