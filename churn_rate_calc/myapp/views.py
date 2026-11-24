from django.shortcuts import render
def churn_rate(request):
        initialcustomer = float(request.POST.get('IC', '0'))
        presentcustomer = float(request.POST.get('PC', '0'))
        
    
        Rate= ((initialcustomer-presentcustomer)*100)/initialcustomer  if request.method == 'POST' else 0
        Churn_Rate=f"{Rate}%"
        print("Initial Customer =",initialcustomer )
        print("Present Customer =",presentcustomer)
        print("Churn_Rate =",Churn_Rate)
        return render(request, 'myapp/home.html',{'initialcustomer': initialcustomer, 'presentcustomer': presentcustomer, 'Churn_Rate': Churn_Rate})
