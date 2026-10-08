from django.shortcuts import render

def inicio(request):
    productos = [
        {"nombre": "Camiseta Dry-Fit", "categoria": "Camisetas", "precio": 89900, "icono": "👕"},
        {"nombre": "Short de Running", "categoria": "Shorts", "precio": 69900, "icono": "🩳"},
        {"nombre": "Tenis Deportivos", "categoria": "Calzado", "precio": 249900, "icono": "👟"},
        {"nombre": "Chaqueta Rompevientos", "categoria": "Chaquetas", "precio": 159900, "icono": "🧥"},
        {"nombre": "Gorra Deportiva", "categoria": "Accesorios", "precio": 49900, "icono": "🧢"},
        {"nombre": "Medias Pack x3", "categoria": "Accesorios", "precio": 29900, "icono": "🧦"},
    ]
    return render(request, "tienda/index.html", {"productos": productos})