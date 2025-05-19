from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from farmers.models import WaterUsage
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from openpyxl import Workbook
from django.http import HttpResponse
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
def export_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.append(['Metric', 'Value'])
    ws.append(['CO2', 120.5])
    ws.append(['CH4', 25.3])
    ws.append(['N2O', 14.8])

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="report.xlsx"'
    wb.save(response)
    return response




def export_pdf(request):
    template = get_template('report_template.html')
    context = {'data': 'Your emission and water use data'}
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=response)
    return response



def submit_data(request):
    if WaterUsage > 1000:
        messages.warning(request, "⚠️ High water usage detected. Consider drip irrigation.")
    messages.success(request, "✅ Data submitted successfully.")
    return redirect('dashboard')

def dashboard(request):
    emissions = {
        'CO2': 120.5,
        'CH4': 25.3,
        'N2O': 14.8
    }
    water_usage = 1500 

    context = {
        'emissions': emissions,
        'water_usage': water_usage
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url="/login/")
def home(request):
    """
    Renders the home page.

    :param request: HTTP request.
    :return: Rendered home page with PDF documents.
    """
    return render(request, 'home.html')


def register(request):
    """
    Handles user registration.

    :param request: HTTP request.
    :return: Rendered registration page or redirects to registration page.
    """
    if request.method == 'POST':
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "username already Taken")
            return redirect("/register/")

        user_email = User.objects.filter(email=email)

        if user_email.exists():
            messages.info(request, "email already Taken")
            return redirect("/register/")

        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully")

        return redirect("/register/")
    return render(request, 'register.html')


def user_login(request):
    """
    Handles user login.

    :param request: HTTP request.
    :return: Redirects to the home page or shows an error message.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page or any other desired page
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'login.html')


def user_logout(request):
    """
    Handles user logout.

    :param request: HTTP request.
    :return: Redirects to the login page.
    """
    logout(request)
    return redirect('login')
