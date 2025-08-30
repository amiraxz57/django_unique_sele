from django.shortcuts import render , HttpResponse , get_object_or_404 
from apps.product.models import product_Models , article_Model
from django.http import JsonResponse ,Http404
from apps.product.forms import edit_Form

# Create your views here.

def product_Views (request):
    products = product_Models.objects.all()
    return render (request , 'product.html' , {'products':products})


def search_ajax (request):
    query = request.GET.get('q' , '')
    results = []

    if query :

        articles = article_Model.objects.filter(title__icontains=query)

        results = [article.title for article in articles] 
        return JsonResponse({'results':results})
    
def base (request):
    return render(request , 'base.html')

def edit_view (request , id):
        form = edit_Form
        if request.method == 'POST':
             if form.is_valid():
                  form.save()
                  
        try :
             product =get_object_or_404 (product_Models ,  id=id)
             return render(request , 'edit.html' , {'product':product})
        except Exception as eror:
             raise Http404('این به جایی نمیرسه خوشگل')


            