from django.views.decorators.cache import cache_page

EXCLUDE_URLS = ['blog/create/', 'blog/edit/']

class CacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if not any(request.path.startswith(url) for url in EXCLUDE_URLS):
            response = cache_page(60 * 15)(self.get_response)(request)
        return response