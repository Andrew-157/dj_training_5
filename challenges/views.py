from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.urls import reverse

monthly_challenges = {
    'january': 'Eat no meat for an entire month!',
    'february': 'Read a new book each week!',
    'march': 'Learn a new language for 30 minutes a day!',
    'april': 'Run 5 kilometers three times a week!',
    'may': 'Practice yoga for 30 minutes every day!',
    'june': 'Cook a new recipe every day!',
    'july': 'Write a journal entry every day!',
    'august': 'Explore a new hiking trail each weekend!',
    'september': 'Complete a daily drawing challenge!',
    'october': 'Try a new workout routine every week!',
    'november': 'Learn to play a new musical instrument!',
    'december': None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {'months': months})


def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse:
    challenges = monthly_challenges
    if month not in challenges:
        raise Http404()

    context = {'month': month,
               'challenge': challenges[month]}
    return render(request, 'challenges/challenge.html', context)


def monthly_challenge_by_number(request: HttpRequest, month: int) -> HttpResponse:
    if month not in range(1, 13):
        return HttpResponseBadRequest(f"<b>400</b> - No month with number: {month}")
    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]
    return HttpResponseRedirect(reverse('challenges:str-month-challenge',
                                        kwargs={'month': redirect_month}))
