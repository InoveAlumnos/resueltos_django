from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Comic

# Create your views here.
@api_view(['POST'])
def create_comic_view(request):
    
    data = request.data
    
    marvel_id = data.get('marvel_id')
    title = data.get('title')
    stock_qty = data.get('stock_qty')
    description = data.get('description')
    price = data.get('price')
    picture = data.get('picture')

    comic = Comic.objects.create(marvel_id=marvel_id, title=title, stock_qty=stock_qty, description=description, price=price, picture=picture)

    comic_data = {
        'id': comic.id,
        'marvel_id': comic.marvel_id, 
        'title': comic.title, 
        'stock_qty':comic.stock_qty, 
        'description': comic.description, 
        'price':comic.price, 
        'picture':comic.picture
    }

    return Response({'comic': comic_data}, status=status.HTTP_201_CREATED)
    
