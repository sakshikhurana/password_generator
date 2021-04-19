from django.shortcuts import render
import uuid
import string, random
# Create your views here.

def random_string_generator(upper_case, length, numbers, special):
    char = string.ascii_lowercase
    if upper_case:
        char += string.ascii_uppercase
    if numbers:
        char += string.digits
    if special:
        char += string.punctuation
    return ''.join(random.choice(char) for _ in range(int(length)))

def password_generated_view(request):
    upper_case = request.GET.get('upperCase', None)
    length = request.GET.get('length', None)
    numbers = request.GET.get('numbers', None)
    special = request.GET.get('special', None)
    password = random_string_generator(upper_case, length, numbers, special)
    return render(request, 'generator/generated.html', {'password': password})


def home_view(request):
    return render(request, 'generator/home.html')
