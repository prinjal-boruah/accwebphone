from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *

# def upload_pic(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             model_pic = PostImage(cover=form.cleaned_data['cover'])
#             model_pic.save()
#             return redirect('broadcast')
#         else:
#         	return HttpResponse(" not uploaded")