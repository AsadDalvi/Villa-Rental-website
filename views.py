from django.shortcuts import render

def homerentalweb(request):
    TypeofHome=""
    Rentduration=""
    BHK=""
    TotalRent =""
    try:
        if request.POST.get('Rentduration')!=0:
            if request.method == "POST":
                TypeofHome = eval(request.POST.get('TypeofHome'))
                Rentduration = eval(request.POST.get('Rentduration'))
                BHK = eval(request.POST.get('BHK'))
                TotalRent  = TypeofHome * Rentduration
                TotalRent += TotalRent * BHK
    except:
        if request.POST.get('Rentduration') == "":
            TotalRent = ""
        else:
            TotalRent = "Check Input"
    return render(request,'homerentalweb.html',{'TotalRent':TotalRent})
