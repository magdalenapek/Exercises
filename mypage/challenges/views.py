from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges={
    'january': "No meat for entire month",
    "february": "Workout four time in week", 
    "march": "Eat more fruits", 
    "april": "Walk for at least 20 minutes every day",
    "may": "Learn Django for at least 20 minutes every day",
    "june": "No meat for entire month",
    "july": "Workout four time in week", 
    "august": "Walk for at least 20 minutes every day",
    "september": "Learn Django for at least 20 minutes every day",
    "october": "Eat more fruits", 
    "november": "No meat for entire month",
    "december": "No challenges:)"

}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_months = month.capitalize()
        month_path = reverse("month-challenge", args = [month])
        list_items += f"<li><a href =\"{month_path}\">{capitalized_months}</a></li>"

        #"<li><a href ="...">January</a></li><li><a href ="...">February</a></li>"
        response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)



def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

