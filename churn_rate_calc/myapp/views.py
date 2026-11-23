from django.shortcuts import render
def churn_rate(request):
    initialcustomer = float(request.POST.get('IC', '0'))
    presentcustomer = float(request.POST.get('PC', '0'))
    if request.method == 'POST' and presentcustomer!=0:
    
        Rate= ((initialcustomer-presentcustomer)*100)/initialcustomer  
        Churn_Rate=f"{Rate}%"
        print("Initial Customer =",initialcustomer )
        print("Present Customer =",presentcustomer)
        print("Churn_Rate =",Churn_Rate)
        return render(request, 'myapp/home.html',{'initialcustomer': initialcustomer, 'presentcustomer': presentcustomer, 'Churn_Rate': Churn_Rate})
    elif request.method == 'POST' and presentcustomer == 0:

        Churn_Rate='Cant Divide By 0'
        print("Initial Customer =",initialcustomer )
        print("Present Customer =",presentcustomer)
        print("Churn_Rate =",Churn_Rate)
        return render(request, 'myapp/home.html',{'initialcustomer': initialcustomer, 'presentcustomer': presentcustomer, 'Churn_Rate': Churn_Rate})
    else:
        Churn_Rate=0
        return render(request, 'myapp/home.html',{'initialcustomer': initialcustomer, 'presentcustomer': presentcustomer, 'Churn_Rate': Churn_Rate})
