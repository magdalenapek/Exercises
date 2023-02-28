from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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



def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")

