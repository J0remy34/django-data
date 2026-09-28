from django.shortcuts import render

# Create your views here.
def index(request):
    productos =[
        {'id': 1, 'nombre': 'Producto 1', 'descripcion': 'Descripcion del producto 1', 'precio': 10.99, 'stock': 5},
        {'id': 2, 'nombre': 'Producto 2', 'descripcion': 'Descripcion del producto 2', 'precio': 109.99, 'stock': 10},
        {'id': 3, 'nombre': 'Producto 3', 'descripcion': 'Descripcion del producto 3', 'precio': 5.99, 'stock': 15},
    ]
    return render(request, 'inicio/default.html', {'productos': productos})