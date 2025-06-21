from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/')  # Changed from '/index' to '/'
def table_detail(request, table_number):
    table = get_object_or_404(Table, number=table_number)
    return render(request, 'table_detail.html', {'table': table})