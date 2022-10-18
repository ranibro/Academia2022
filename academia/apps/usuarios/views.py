from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout


from .forms import SignInForm, SignUpForm

def signout(request):
    logout(request)
    return redirect("accounts:signin")


class SignUpView(View):
    """ User registration view """

    template_name = "cadastroCliente.html"
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("usuarios:login")
        context = {"form": forms}
        return render(request, self.template_name, context)

class SignInView(View):
    """ User registration view """

    template_name = "login/loginAdm.html"
    form_class = SignInForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data["email"]
            password = forms.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("funcionarios:clientes")
        context = {"form": forms}
        return render(request, self.template_name, context)
