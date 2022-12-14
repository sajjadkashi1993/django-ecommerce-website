from .models import Category

def categories(request):
    categories = Category.objects.filter(is_navbar=True)
    return {'categories':categories}