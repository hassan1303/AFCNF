from django.shortcuts import redirect, render
from django.contrib import messages
from farmers.models import WaterUsage
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from openpyxl import Workbook
from django.http import HttpResponse





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
    # Example check
    if WaterUsage > 1000:
        messages.warning(request, "⚠️ High water usage detected. Consider drip irrigation.")
    messages.success(request, "✅ Data submitted successfully.")
    return redirect('dashboard')