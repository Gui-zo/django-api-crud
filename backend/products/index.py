from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product


@register(Product)
class ProductIndex(AlgoliaIndex):
    # should_index = 'is_public'  # Should this go into algolia search or not
    fields = [
        'title',
        'body',
        'price',
        'user',
        'public',
        'path',
        'endpoint'
    ]
    
    settings = {
        'searchableAttributes': ['title', 'body'],
        'attributesForFaceting': ['user', 'public']
    }

    tags = 'get_tags_list'

# admin.site.register(Product, ProductModelAdmin)