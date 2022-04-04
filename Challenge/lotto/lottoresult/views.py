from django.shortcuts import render
import random
# Create your views here.
def result(reqeust):
    num = reqeust.GET.get('cnt')
    a=[[0]*6 for i in range(int(num))]
    for i in range (0, int(num)):
        for j in range (0, 6):
            a[i][j] = random.randint(1,46)

    return render(reqeust, 'result.html', {'Result' : a, 'Count' : num})