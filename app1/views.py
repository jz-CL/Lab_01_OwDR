from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View

from .models import Donation, Institution, Category
from .forms import RegisterUserForm
# Create your views here.

User = get_user_model()

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

        #  Dynamiczne ładowanie instytucji
        institutions = Institution.objects.filter(type=1)
        list_institutons = []

        for institution in institutions:

            name = institution.name
            description = institution.description
            category = ''
            institution_get = Institution.objects.get(pk=institution.pk)

            for _ in institution_get.categories.all():
                category += str(_) + ', '

            category = category[0: len(category)-2]
            list_institutons.append({'name': name, 'description': description, 'category': category})

        # breakpoint()
        organisations = Institution.objects.filter(type=2)
        list_organisations = []
        for organisation in organisations:

            name = organisation.name
            description = organisation.description
            category = ''
            organisation_get = Institution.objects.get(pk=organisation.pk)

            for _ in organisation_get.categories.all():
                category += str(_) + ', '

            category = category[0: len(category) - 2]
            list_organisations.append({'name': name, 'description': description, 'category': category})

        local_organisations = Institution.objects.filter(type=3)
        list_local_organisations = []
        for local_organisation in local_organisations:

            name = local_organisation.name
            description = local_organisation.description
            category = ''
            local_organisation_get = Institution.objects.get(pk=local_organisation.pk)

            for _ in local_organisation_get.categories.all():
                category += str(_) + ', '

            category = category[0: len(category) - 2]
            list_local_organisations.append({'name': name, 'description': description, 'category': category})

        ctx = {
            'count_quantity': count_quantity,
            'count_institution': count_institution,
            'list_institutons': list_institutons,
            'list_organisations': list_organisations,
            'list_local_organisations': list_local_organisations,
        }
        return render(request, self.template_name, ctx)


class AddDonationView(View):
    template_name = 'app1/form.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        return render(request, self.template_name, ctx)


class LoginView(View):
    form_class = LoginUserForm
    template_name = 'app1/login.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        return render(request, self.template_name, ctx)


class RegisterView(View):
    form_class = RegisterUserForm
    template_name = 'app1/register.html'

    def get(self, request, *args, **kwargs):

        ctx = {
            'form': self.form_class(),

        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            # zapisz dane użytkownika
            User.objects.create_user(
                email=cd['email'],
                password=cd['password'],  # make_password
                first_name=cd['name'],
                last_name=cd['surname']
            )


            return redirect('login')
        ctx = {

            }
        return render(request, self.template_name, ctx)

