from django.shortcuts import render
from django.views import View
from django.contrib import messages

from .models import Donation, Institution, Category
# Create your views here.


class LandingPageView(View):
    template_name = 'app1/index.html'

    def get(self, request, *args, **kwargs):

        donations = Donation.objects.all()
        count_quantity = 0
        count_institution = 0

        for donation in donations:
            count_quantity += donation.quantity

            # ile jest wspartych instytucji? - nie istotnie czy różnych czy tych samych
            count_institution += 1


        # count_quantity = 9
        # count_institution = 5
        ctx = {
            'count_quantity': count_quantity,
            'count_institution': count_institution,
        }
        return render(request, self.template_name, ctx)


class AddDonationView(View):
    template_name = 'app1/form.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        return render(request, self.template_name, ctx)


class LoginView(View):
    template_name = 'app1/login.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        return render(request, self.template_name, ctx)


class RegisterView(View):
    template_name = 'app1/register.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        return render(request, template_name, ctx)
