from django.shortcuts import render, HttpResponse, redirect
from Index.models import Contact, IndexValue, StockDetails, IndexPageStockContact, IndexJobPost, IndexNewsPost, IndexOtherPosts, StockOfTheWeek, StockOfTheMonth, HighRiskHighReturn, BookStore, NewsPic
from django.contrib import messages
from FinanceNews.models import FinanceNewsPost

# Create your views here.

def Index(request):
    allIndexValue = IndexValue.objects.all().order_by('-created_on')
    allStockDetails = StockDetails.objects.all().order_by('-created_on')
    allIndexJobPost = IndexJobPost.objects.all().order_by('-created_on')
    allIndexNewsPost = IndexNewsPost.objects.all().order_by('-created_on')
    allIndexOtherPosts = IndexOtherPosts.objects.all().order_by('-created_on')
    allBookStore = BookStore.objects.all().order_by('-created_on')
    allNewsPic = NewsPic.objects.all()
    context = {'allIndexValue': allIndexValue, 'allStockDetails':allStockDetails, 'allIndexJobPost':allIndexJobPost, 'allIndexNewsPost':allIndexNewsPost, 'allIndexOtherPosts':allIndexOtherPosts, 'allBookStore':allBookStore, 'allNewsPic':allNewsPic}
    if request.method =='POST':
        username = request.POST['username']
        useremail =request.POST['useremail']
        userphone =request.POST['userphone']
        # print(username,useremail,userphone)

        if len(username)<2 or len(useremail)<4 or len(userphone)<10 :
            messages.warning(request, "Please , Fill the form details correctly.")
        else:
            stockcontact = IndexPageStockContact(username=username, useremail=useremail, userphone=userphone)
            stockcontact.save()
            messages.success(request, "Great, Your message has been successfully sent. You will start getting recommendations now onwards.")

    return render(request, 'Index/index.html', context)

def about(request):
    return render(request, 'Index/about.html')

def contact(request):
    if request.method=='POST':
        name =request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<2:
            messages.warning(request, "Please , Fill the form details correctly.")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Thank you , Your message has been successfully sent.")
    return render(request, 'Index/contact.html')

def search(request):
    query =request.GET['query']
    if len(query)>50:
        allFinanceNewsPost = FinanceNewsPost.objects.none()
    else:
        allFinanceNewsPost = FinanceNewsPost.objects.filter(title__icontains=query)
        # allFinanceNewsPostContent = FinanceNewsPost.objects.filter(content__icontains=query)
        # allFinanceNewsPost = allFinanceNewsPostTitle.union(allFinanceNewsPostContent)

    if allFinanceNewsPost.count()== 0:
        messages.warning(request, "No search result found. Please refine your query.")
    params = {'allFinanceNewsPost': allFinanceNewsPost, 'query':query}
    return render(request, 'Index/search.html', params)

def sow(request):
    allStockOfTheWeek = StockOfTheWeek.objects.all().order_by('-created_on')
    context = {'allStockOfTheWeek':allStockOfTheWeek}
    return render(request, 'Index/sow.html', context)

def som(request):
    allStockOfTheMonth = StockOfTheMonth.objects.all().order_by('-created_on')
    context = {'allStockOfTheMonth':allStockOfTheMonth}
    return render(request, 'Index/som.html', context)

def hrhr(request):
    allHighRiskHighReturn = HighRiskHighReturn.objects.all().order_by('-created_on')
    context = {'allHighRiskHighReturn':allHighRiskHighReturn}
    return render(request, 'Index/hrhr.html', context)

def tnews(request, slug):
    trendpost = IndexNewsPost.objects.filter(slug=slug).first()
    context = {'trendpost':trendpost}
    return render(request, 'Index/tnews.html', context)


