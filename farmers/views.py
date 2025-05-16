from django.shortcuts import redirect, render
from django.contrib import messages
from farmers.models import WaterUsage


# Create your views here.





















def submit_data(request):
    # Example check
    if WaterUsage > 1000:
        messages.warning(request, "⚠️ High water usage detected. Consider drip irrigation.")
    messages.success(request, "✅ Data submitted successfully.")
    return redirect('dashboard')