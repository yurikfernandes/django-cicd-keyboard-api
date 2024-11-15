from django.shortcuts import render

from keyboards.models import Keyboard, KEYBOARDS_CATEGORIES

def homepage(request):
    keyboards = Keyboard.objects.all().order_by('-overall_rating')[:5]
    keyboards_dict = []
    for keyboard in keyboards:
        keyboards_dict.append(keyboard.get_keyboard_dict())

    return render(
        request, 'homepage.html', {'keyboards': keyboards_dict}
    )

def keyboard_list(request):
    keyboards = Keyboard.objects.all()
    return render(
        request, 'keyboard_list.html', {'keyboards': keyboards}
    )
