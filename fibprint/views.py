
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.
class MyView(TemplateView):
    template_name = "home.html"

    def printFibonacciNumbers(n):
        fiblist = []
        f1 = 0
        f2 = 1
        if (n < 1):
            return
        print(f1)
        fiblist.append(f1)
        for x in range(1, n):
            print(f2)
            fiblist.append(f2)
            next = f1 + f2
            f1 = f2
            f2 = next
        return fiblist

    def get(self,request):
        x=10
        print(x)
        

        num = int(request.GET.get('number',0))
        fiblist= MyView.printFibonacciNumbers(num)
        print(fiblist)
        return HttpResponse(fiblist)
  