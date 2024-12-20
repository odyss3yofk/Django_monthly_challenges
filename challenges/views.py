from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "we eat veggies",
    "february": "we go to walk",
    "march": "we code an hour everyday",
    "april": "we exercise",
    "may": "lets game",
    "june": "music makes the way",
    "july": "yayyyy summer",
    "august": "summers ending",
    "september": "coming of fall",
    "october": "the winter arc starts",
    "november": "falllllll",
    "december": "end of a year"
}
# Create your views here.


def index(request):

    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()

        month_path = reverse("month-challenge", args=[month])

        list_items += f"<li><a href=\"{month_path}\">{
            capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challengenum(request, month):

    months = list(monthly_challenges.keys())

    if month > len(months) or month <= 0:

        return HttpResponseNotFound("month doesn't exist")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"

        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h2>error 404</h2>")
