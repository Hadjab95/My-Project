from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def category_summary(request):
    categories = Category.objects.all()
    return render(request, "category_summary.html", {"categories": categories})


def category(request, foo):
    # Replace Hyphens with Spaces
    foo = foo.replace("-", " ")
    # Grab the category from the url
    try:
        # Look Up The Category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(
            request, "category.html", {"products": products, "category": category}
        )
    except:
        messages.success(request, ("That category doesn't exist..."))
        return redirect("home")


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {"product": product})


def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


def about(request):
    return render(request, "about.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Do some shopping cart stuff
            # current_user = Profile.objects.get(user__id=request.user.id)
            # Get their saved cart from database
            # saved_cart = current_user.old_cart
            # Convert database string to python dictionary
            # if saved_cart:
            # Convert to dictionary using JSON
            # converted_cart = json.loads(saved_cart)
            # Add the loaded cart dictionary to our session
            # Get the cart
            # cart = Cart(request)
            # Loop thru the cart and add the items from the database
            # for key, value in converted_cart.items():
            # cart.db_add(product=key, quantity=value)

            messages.success(request, ("You are have been logged in!"))
            return redirect("home")
        else:
            messages.success(request, ("There was an error, please try again..."))
            return redirect("login")

    else:
        return render(request, "login.html", {})


def logout_user(request):
    logout(request)
    messages.success(
        request, ("You have been logged out...thank you for stopping by...")
    )
    return redirect("home")


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have registered successfully...Welcome!"))
            return redirect("home")
        else:
            messages.success(
                request,
                ("Whoops! There was a problem Registering, please try again..."),
            )
            return redirect("register")
    else:
        return render(request, "register.html", {"form": form})
