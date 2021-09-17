from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from hello.forms import *
from hello.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, ListView
from django.db.models import Q 
import logging

logger = logging.getLogger(__name__)

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Paperclip
    template_name = 'main/search_results.html'  
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Paperclip.objects.filter(
            Q(title__icontains=query) | Q(abstract__icontains=query)
        )
        return object_list


# Create your views here.
def index(request):
    form = AuthenticationForm()
    context = {"form": form}
    return render(request, "index.html", context)

def about(request):
    return render(request, "main/about.html")

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})    

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("index")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def faq(request):
    return render(request, "main/faq.html")

def privacy(request):
    return render(request, "main/privacy-policy.html")

def paperclip(request):
    username = request.user.get_username()
    # print(username)
    if request.method == 'POST':
        form = AddPaperForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            paperclip.objects.create(address=address)
            return render(request, "check-in.html", {"user": username, "form": form, "success": "Clock In Successfully!"})
    else:
        form = AddPaperForm()

    return render(request, "check-in.html", {"user": username, "form": form})


def add_guest(request):
    username = request.session.get('user', '')
    if request.method == 'POST':
        form = AddGuestForm(request.POST)

        if form.is_valid():
            event = form.cleaned_data['event']
            realname = form.cleaned_data['realname']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            sign = form.cleaned_data['sign']
            # if sign is True:
            #     sign = 1
            # else:
            #     sign = 0

            Guest.objects.create(event=event, realname=realname,
                                 phone=phone, email=email, sign=sign)
            return render(request, "add-guest.html", {"user": username, "form": form, "success": "Add Guest Successfully"})

    else:
        form = AddGuestForm()

    return render(request, "add-guest.html", {"user": username, "form": form})


def account(request):
    # query_results = Event.objects.all()
    # return render(request, "main/account.html",{'query_results':query_results})
    return render(request, "main/account.html")

def paperclips(request):
    paperclips = Paperclip.objects.all()
    return render(request, 'components/paperclips.html', {'paperclips':paperclips})

def paperclip_detail(request, paperclip_id):
    try:
        paperclip = Paperclip.objects.get(id= paperclip_id)
    except Paperclip.DoesNotExist:
        raise Http404('paperclip not found')
    return render(request, 'components/paperclip_detail.html', {'paperclip':paperclip,})
    # return HttpResponse(f'<p> paperclip_detail view with id {paperclip_id}</p>')

def add_paperclip(request):
	return add_item(request, AddPaperForm)

def display_paperclips(request):
    context = Paperclip.objects.all()
    context = {
		'items': items,
		'header': 'paperclip'
	}
    return render(request, 'components/paperclips.html',context)


def add_item(request, cls):
	if request.method == 'POST':
		form = cls(request.POST)

		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		form = cls()
		return render(request, 'add_new.html', {'form': form})

def display_blogs(request):
    context = {}
    return render(request, 'blog/index.html',context)

def get_pages(totalpage=1,current_page=1):
    """
    example: get_pages(10,1) result=[1,2,3,4,5]
    example: get_pages(10,9) result=[6,7,8,9,10]
    页码个数由WEB_DISPLAY_PAGE设定
    """
    WEB_DISPLAY_PAGE = 5
    front_offset = int(WEB_DISPLAY_PAGE / 2)
    if WEB_DISPLAY_PAGE % 2 == 1:
        behind_offset=front_offset
    else:
        behind_offset=front_offset -1

    if totalpage < WEB_DISPLAY_PAGE:
        return list(range(1,totalpage+1))
    elif current_page<=front_offset:
        return list(range(1,WEB_DISPLAY_PAGE+1))
    elif current_page>=totalpage-behind_offset:
        start_page=totalpage-WEB_DISPLAY_PAGE+1
        return list(range(start_page,totalpage+1))
    else:
        start_page=current_page-front_offset
        end_page=current_page+behind_offset
        return list(range(start_page,end_page+1))

if __name__ == '__main__':
    res=get_pages(10,1)
    print(res)

def page_demo(request):
    articles=Paperclip.objects.all()
    paginator_obj=Paginator(articles,5) #每页5条
    # print(paginator_obj.page_range)

    request_page_num=request.GET.get('page',1)
    # print(request_page_num)
    page_obj=paginator_obj.page(request_page_num)

    total_page_number=paginator_obj.num_pages
    print(total_page_number)
    page_list=get_pages(int(total_page_number),int(request_page_num))

    return render(request,'page_demo.html',{'page_obj':page_obj,'page_list':page_list})