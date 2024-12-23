from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# from django.template.loader import render_to_string
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
    "december": None
}
# Create your views here.


def index(request):

    months = list(monthly_challenges.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()

    #     month_path = reverse("month-challenge", args=[month])

    #     list_items += f"<li><a href=\"{month_path}\">{
    #         capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    return render(request, "challenges/index.html", {"months": monthly_challenges, })


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

        return render(request, "challenges/challenge.html", {"text": challenge_text, "month_name": month})
       # response_data = render_to_string("challenges/challenge.html")

        # return HttpResponse(response_data)
    except:
        raise Http404()
