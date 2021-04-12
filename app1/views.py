from django.shortcuts import render
from django.views import View
from django.contrib import messages

# Create your views here.


class LandingPageView(View):
    template_name = 'app1/index.html'

    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)


class AddDonationView(View):
    template_name = 'app1/form.html'

    def get(self, request):
        ctx = {}
        return render(request, template_name, ctx)


class LoginView(View):
    template_name = 'app1/login.html'

    def get(self, request):
        ctx = {}
        return render(request, template_name, ctx)


class RegisterView(View):
    template_name = 'app1/register.html'

    def get(self, request):
        ctx = {}
        return render(request, template_name, ctx)
