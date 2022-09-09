from multiprocessing import context
from django.shortcuts import render
# Create your views here.


def home(request):
    number1 = request.POST.get('number1')
    number2 =request.POST.get('number2')
    operator = request.POST.get('operator')
    # number1 = eval(number1)
    # number1 = eval(number2)
    result = ''

    try:
        if request.method =='POST':
            n1 = int(number1)
            n2 = int(number2)
            if operator =='+':
                result = n1+n2
            elif operator =='-':
                result = n1-n2
            elif operator =='*':
                result = n1*n2
            elif operator =='**':
                result = n1**n2
            elif operator =='/':
                result = n1/n2
            elif operator =='//':
                result = n1//n2
            elif operator =='%':
                result = n1%n2

    except:
        result = 'Wrong Opperator!Try Again.'
        print(result)
    return render(request,'home.html',{'result':result})