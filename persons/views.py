from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def main_page(request):
    """Отображение главной страницы."""
    all: int = len(User.objects.all())
    return render(request, 'mane_page.html', {'all': all})
