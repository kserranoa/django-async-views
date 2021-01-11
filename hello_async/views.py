from django.http import HttpResponse

async def index(request):
    return HttpResponse('Hello, this is async')
