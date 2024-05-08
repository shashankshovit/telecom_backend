import json

# from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Q

from .models import Customer, Plan

def index(request):
	return HttpResponse('Telecom Customer Management System is here.')

def list_plans(request):
	plans = Plan.objects.all().values()
	return JsonResponse(list(plans), safe=False)

def list_customers(request):
	customers = Customer.objects.all().values()
	return JsonResponse(list(customers), safe=False)

@csrf_exempt
def register(request):
	if not request.method == "POST":
		return HttpResponse('Invalid HTTP method.')
	body_unicode = request.body.decode('utf-8')
	body_data = json.loads(body_unicode)
	cs = Customer()
	cs.name=body_data['name']
	cs.dob=body_data['dob']
	cs.email=body_data['email']
	cs.aadhaar=body_data['aadhaar']
	cs.mob=body_data['mob']
	cs.reg_date=timezone.now()
	cs.save()
	return JsonResponse(body_data)

@csrf_exempt
def login(request):
	if not request.method == "POST":
		return HttpResponse('Invalid HTTP method.')
	body_unicode = request.body.decode('utf-8')
	body_data = json.loads(body_unicode)
	customer = Customer.objects.filter(email=body_data["email"]).values().first()
	return JsonResponse(customer)

@csrf_exempt
def purchase(request):
	if not request.method == "POST":
		return HttpResponse('Invalid HTTP method.')
	body_unicode = request.body.decode('utf-8')
	body_data = json.loads(body_unicode)
	cust = Customer.objects.filter(id=body_data["user_id"]).first()
	pl = Plan.objects.filter(id=body_data["plan_id"]).first()
	custpl = cust.plan.add(pl)
	plans = Plan.objects.filter(customer__id=body_data["user_id"]).values()
	return JsonResponse(list(plans), safe=False)

@csrf_exempt
def get_customer_plans(request):
	if not request.method == "POST":
		return HttpResponse('Invalid HTTP method.')
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	plans = Plan.objects.filter(customer__id=body["user_id"]).values()
	return JsonResponse(list(plans), safe=False)

@csrf_exempt
def view_other_plans(request):
	if not request.method == "POST":
		return HttpResponse('Invalid HTTP method.')
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	plans = Plan.objects.filter(~Q(customer__id=body["user_id"])).values()
	return JsonResponse(list(plans), safe=False)

@csrf_exempt
def modify_plan(request):
	if not request.method == "POST":
		return HttpResponse('Invalid HTTP method.')
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	existing_plan = Plan.objects.filter(customer__id=body["user_id"]).first()
	cus = Customer.objects.filter(id=body["user_id"]).first()
	cus.plan.remove(existing_plan)
	plqs = Plan.objects.filter(id=body["plan_id"])
	cus.plan.add(plqs.first())
	return JsonResponse(plqs.values().first())
