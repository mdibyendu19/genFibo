from django.shortcuts import render
from django.template.response import TemplateResponse

from . import utils

# Create your views here.

def index(request):
	context_data = {}
	return TemplateResponse(request, 'home.html', context_data)


def generate(request):
	num = request.POST['fib_num']
	result = utils.generateFib(num)
	return TemplateResponse(request, 'generate.html', {'result': result})