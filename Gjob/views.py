from django.shortcuts import render, HttpResponse, redirect
from Gjob.models import GovJobPost, BookPost1 , BookPost2 , BookPost3
from django.contrib import messages



# Create your views here.
def Gjob(request):
    allGovJobPost = GovJobPost.objects.all().order_by('-created_on')
    allBookPost1 = BookPost1.objects.all()
    allBookPost2 = BookPost2.objects.all()
    allBookPost3 = BookPost3.objects.all()
    context = {'allGovJobPost':allGovJobPost, 'allBookPost1':allBookPost1, 'allBookPost2':allBookPost2, 'allBookPost3':allBookPost3}
    return render(request, 'Gjob/GjobHome.html', context)

def gsearch(request):
    gquery =request.GET['gquery']
    if len(gquery)>50:
        allGovJobPost = GovJobPost.objects.none()
    else:
        allGovJobPost = GovJobPost.objects.filter(category__icontains=gquery)
        # allFinanceNewsPostContent = FinanceNewsPost.objects.filter(content__icontains=query)
        # allFinanceNewsPost = allFinanceNewsPostTitle.union(allFinanceNewsPostContent)

    if allGovJobPost.count()== 0:
        messages.warning(request, "No search result found. Please refine your query.")
    params = {'allGovJobPost': allGovJobPost, 'gquery':gquery}
    return render(request, 'Gjob/gsearch.html', params)
    
def GjobPost(request,slug):
    gjobpost = GovJobPost.objects.filter(slug=slug).first()
    gjobpost.views = gjobpost.views + 1
    gjobpost.save()
    context = {'gjobpost':gjobpost}
    return render(request, 'Gjob/GjobPost.html', context)
