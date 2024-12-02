from django.views import View
from .models import Company
import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
# Create your views here.

class CompanyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        #Seccion para Buscar solo una Compañia
        if(id>0):
            company = list(Company.objects.filter(id=id).values())
            if len(company)>0:
                company = company[0]
                datos = {'message':'Success','companies':company}
            else:
                datos = {'message':'Companies Not Found'}
            return JsonResponse(datos)
        #Seccion para Listar Todas las Compañias
        else:
            companies = list(Company.objects.values())
            if len(companies)>0:
                datos = {'message':'Success','companies':companies}
            else:
                datos = {'message':'Companies Not Found'}
        return JsonResponse(datos)
    def post(self, request):
        jd = json.loads(request.body)
        Company.objects.create(name=jd['name'],website=jd['website'] ,foundation=jd['foundation'] )
        datos = {'message':'Success Register'}
        return JsonResponse(datos)
    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.foundation = jd['foundation']
            company.save()
            datos = {'message':'Success Company Update'}
        else:
            datos = {'message':'Companies Not Found'}
        return JsonResponse(datos)  
    def delete(self, request, id):
        company = list(Company.objects.filter(id=id).values())
        if len(company)>0:
            Company.objects.filter(id=id).delete()
            datos = {'message':'Success Company Delete'}
        else:
             datos = {'message':'Companies Not Found'}
        return JsonResponse(datos)
    