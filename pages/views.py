from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse
from django import forms
from django.shortcuts import render, redirect

# def homePageView(request):
#     return HttpResponse("Hello World!")
class HomePageView(TemplateView):
    template_name="pages/home.html"

class AboutPageView(TemplateView):
    template_name='pages/about.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us", 
            "description": "This is an about page... ",
            "author": "Developed by: Manuela Caro",
        })
        return context
    
class ContactPageView(TemplateView):
    template_name='pages/contact.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context.update({
            "title": "Contact - Online Store",
            "subtitle": "Contact", 
            "email": "email123@email.com",
            "address": "Av 63 sur. #56-13",
            "phone": "+1 234 56 78 90",
        })
        return context
    
class Product: 
    products = [ 
        {"id":"1", "name":"TV", "description":"Best TV", "price":500}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":200}, 
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":99}, 
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":80} 
    ] 

    
class ProductIndexView(View): 
    template_name = 'products/index.html' 
    
    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] = "List of products" 
        viewData["products"] = Product.products 
        
        return render(request, self.template_name, viewData) 
    
class ProductShowView(View): 
    template_name = 'products/show.html' 
    
    def get(self, request, id): 
        product = next((p for p in Product.products if p["id"] == str(id)), None)
        if not product:
            return HttpResponseRedirect(reverse('home'))

        viewData = {} 
        product = Product.products[int(id)-1] 
        viewData["title"] = product["name"] + " - Online Store" 
        viewData["subtitle"] = product["name"] + " - Product information" 
        viewData["product"] = product 

        
        
        return render(request, self.template_name, viewData)
    
class ProductForm(forms.Form): 
    name = forms.CharField(required=True) 
    price = forms.FloatField(required=True) 

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("The price must be greater than zero.")
        return price

class ProductCreateView(View): 
    template_name = 'products/create.html' 
    
    def get(self, request): 
        form = ProductForm() 
        viewData = {} 
        viewData["title"] = "Create product" 
        viewData["form"] = form 
        return render(request, self.template_name, viewData) 
        
    
    def post(self, request): 
        form = ProductForm(request.POST) 
        if form.is_valid(): 
            return render(request, "products/product_created.html") 
            
        
        else: 
            viewData = {} 
            viewData["title"] = "Create product" 
            viewData["form"] = form 
            return render(request, self.template_name, viewData)
        
    
        