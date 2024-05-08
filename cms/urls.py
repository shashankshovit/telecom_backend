from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("list_plans/", views.list_plans, name="list all plans"),
	path("list_customers/", views.list_customers, name="list all customers"),
	path("register/", views.register, name="register customer"),
	path("login/", views.login, name="customer login"),
	path("purchase/", views.purchase, name="plan purchase"),
	path("getplans/", views.get_customer_plans, name="fetch customer plans"),
	path("viewotherplans/", views.view_other_plans, name="fetch other plans than existing"),
	path("modifyplan/", views.modify_plan, name="modify plan"),
]