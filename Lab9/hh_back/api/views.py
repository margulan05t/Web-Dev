from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views import View
from .models import Company, Vacancy

class CompanyListView(View):
    def get(self, request):
        companies = list(Company.objects.values())
        return JsonResponse(companies, safe=False)

class CompanyDetailView(View):
    def get(self, request, id):
        try:
            company = Company.objects.values().get(id=id)
            return JsonResponse(company)
        except Company.DoesNotExist:
            return JsonResponse({'error': 'Company not found'}, status=404)

class CompanyVacanciesView(View):
    def get(self, request, id):
        vacancies = list(Vacancy.objects.filter(company_id=id).values())
        return JsonResponse(vacancies, safe=False)

class VacancyListView(View):
    def get(self, request):
        vacancies = list(Vacancy.objects.values())
        return JsonResponse(vacancies, safe=False)

class VacancyDetailView(View):
    def get(self, request, id):
        try:
            vacancy = Vacancy.objects.values().get(id=id)
            return JsonResponse(vacancy)
        except Vacancy.DoesNotExist:
            return JsonResponse({'error': 'Vacancy not found'}, status=404)

class TopTenVacanciesView(View):
    def get(self, request):
        vacancies = list(Vacancy.objects.order_by('-salary').values()[:10])
        return JsonResponse(vacancies, safe=False)
