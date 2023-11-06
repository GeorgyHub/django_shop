from django.shortcuts import render, get_object_or_404
from .models import Items, Categories, Brands

# Create your views here.
def homepage(request):
    items = Items.objects.all()
    categories = Categories.objects.all()
    brands = Brands.objects.all()
    return render(request, 'shop/index.html', {"title": "Интернет-магазин", 
                                               "items": items,
                                               "categories": categories,
                                               "brands": brands})

def itempage(request, item_id):
    item = get_object_or_404(Items, pk=item_id)
    items = Items.objects.all()
    categories = Categories.objects.all()
    brands = Brands.objects.all()
    return render(request, 'shop/item.html', {"title": "Интернет-магазин", 
                                              "items": items,
                                              "item": item, 
                                              "categories": categories, 
                                              "brands": brands})