from django.shortcuts import render
from .models import product
from django.http import HttpResponse
from .serializers import ProductSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .permissions import IsAdminorReadOnly

def input(request):
    return render(request,'input.html')
def insert(request):
    pid1=int(request.GET['t1'])
    pname1=request.GET['t2']
    pcost1=float(request.GET['t3'])
    f=product(pid=pid1,pname=pname1,pcost=pcost1)
    f.save()
    return render(request,'links.html')
def display(request):
    recs=product.objects.all()
    return render(request,'display.html',{'records':recs})
class ProductList(generics.ListAPIView):
    queryset = product.objects.all()
    serializer_class=ProductSerializer
    permission_classes = (IsAdminorReadOnly,)

class ProductList1(generics.RetrieveUpdateDestroyAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminorReadOnly,)





# Create your views here.
