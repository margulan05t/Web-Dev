from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Company,Vacancy
from .serializers import CompanySerializer,VacancySerializer
from rest_framework import status

@api_view(['GET'])

def companies_list(request):
    if request.method =='GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies,many = True)
        return Response(serializer.data)

@api_view(['GET'])    
def company_detail(request,id):
    try:
        company = Company.objects.get(pk = id)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method =='GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    

@api_view(['GET'])
def company_vacancies(request,id):
    try:
        company =Company.objects.get(pk = id)

    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method =='GET':
        vacancies = company.vacancies.all()

        serializer = VacancySerializer(vacancies, many =True )

        return Response(serializer.data)
    
@api_view(['GET'])
def vacancies_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(pk=id)
    except Vacancy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

@api_view(['GET'])
def top_vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)