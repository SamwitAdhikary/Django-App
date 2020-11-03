from django.shortcuts import render, HttpResponse

# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html')
    return HttpResponse('This is blog page')

def blogpost(request, slug):
    return HttpResponse(f'This is blog post of {slug}')