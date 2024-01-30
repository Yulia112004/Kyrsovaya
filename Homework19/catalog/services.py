from django.core.cache import cache

from catalog.models import Category


def get_categories():
    categories = cache.get('categories')

    if categories is None:
        categories = Category.objects.all()

        cache.set('categories', categories, 3600)

    return categories