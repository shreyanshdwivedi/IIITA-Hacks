from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from forms import RegisterForm, LoginForm
# Create your views here.


from .forms import ProductAddForm, ProductModelForm
from .models import Product, User

def create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        #print
        form.cleaned_data.get("publish")
        instance = form.save(commit=False)
        instance.sale_price = instance.price
        instance.save()
    template = "form.html"
    context = {
        "form": form,
        "submit_btn": "Create Product"
    }
    return render(request, template, context)


def update_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    form = ProductModelForm(rquest.POST or None, instance=product)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.sale_price = instance.price
        instance.save()
    template = "form.html"
    context = {
        "object": product,
        "form": form,
        "submit_btn": "Update Product"
    }
    return render(request, template, context)


def detail_slug_view(request, slug=None):
    product = Product.objects.get(slug=slug)
    try:
        product = get_object_or_404(Product, slug=slug)
    except Product.MultipleObjectsReturned:
        product = Product.objects.filter(slug=slug).order_by("-title").first()
    # print slug
    # product = 1
    template = "detail_view.html"
    context = {
        "object": product
    }
    return render(request, template, context)


def detail_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    template = "detail_view.html"
    context = {
        "object": product
    }
    return render(request, template, context)


def list_view(request):
    # list of items
    print
    request
    queryset = Product.objects.all()
    template = "list_view.html"
    context = {
        "queryset": queryset
    }
    return render(request, template, context)

def home_view(request):
    return render(request, "all_ads.html", {})

def form_view(request):
    return render(request, "ad_form.html", {})

# def login_view(request):
#     form = LoginForm()
#     if(request.method == "POST"):
#         username = request.POST["username"]
#         password = request.POST["password"]


def register(request):
    if(request.method == "POST"):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]

            if User.objects.filter(username=username).exists():
                return HttpResponse("Username already exists")
            elif User.objects.filter(email=email).exists():
                return HttpResponse("Email already registered")
            else:
                user = form.save()
                user = authenticate(username=user.username, password=user.password)
                login(request, user)
                return render(request, 'login.html', {})
        else:
            print form.errors
            return render(request, 'home.html', {'form':form})
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})


def login(request):
    if(request.method == "POST"):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                if password == user.password:
                    return render(request, 'home.html', {})
                else:
                    return HttpResponse("Password incorrect")
            else:
                return HttpResponse("Username does not exists!")
        else:
            return HttpResponse("Form invalid")
    else:
        form = LoginForm()
        return render(request, "login.html", {'form':form})

def ad_create(request):
    return render(request, "ad_form.html", {})




