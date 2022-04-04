from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def lotto(reqeust):
    
    return render(reqeust, 'lotto.html')