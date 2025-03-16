from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404
from django.shortcuts import render
import sqlite3
from datetime import datetime, timedelta
import json

from api.config import get_db_path
from api.models import Leaderboard, UserProfile, League

database_path = get_db_path()


def generate_leaderboard_row(counter, user, value):
    return {"place": counter, "username": user, "value": value}


def reviews(request):
    data = []

    for counter, leaderboard in enumerate(Leaderboard.objects.all().order_by("-cards_today"), start=1):
        data.append(generate_leaderboard_row(counter, leaderboard.user, leaderboard.cards_today))
    return render(request, "reviews.html", {"data": data})


def time(request):
    data = []

    for counter, leaderboard in enumerate(Leaderboard.objects.all().order_by("-time_today"), start=1):
        data.append(generate_leaderboard_row(counter, leaderboard.user, leaderboard.time_today))
    return render(request, "time.html", {"data": data})


def streak(request):
    data = []
    for counter, leaderboard in enumerate(Leaderboard.objects.all().order_by("-streak"), start=1):
        data.append(generate_leaderboard_row(counter, leaderboard.user, leaderboard.streak))
    return render(request, "streak.html", {"data": data})


def retention(request):
    data = []
    for counter, leaderboard in enumerate(Leaderboard.objects.all().order_by("-retention"), start=1):
        data.append(generate_leaderboard_row(counter, leaderboard.user, leaderboard.retention))
    return render(request, "retention.html", {"data": data})


def user(request, username):
    if not User.objects.filter(username=username).exists():
        raise Http404("User does not exist")

    auth_user = User.objects.get(username=username)

    if not UserProfile.objects.filter(user=auth_user).exists():
        raise Http404("User does not exist")

    user_data = UserProfile.objects.get(user=auth_user)
    leaderboard = None
    country = user_data.country
    groups = ["-"]

    if Leaderboard.objects.filter(user=user_data.user).exists():
        leaderboard = Leaderboard.objects.get(user=user_data.user)
    if user_data.country == "Country" or "":
        country = "-"
    if user_data.groups:
        groups = user_data.groups

    if leaderboard is None:
        data = [{"username": username,
                 "cards": 0,
                 "streak": 0,
                 "time": 0,
                 "retention": 0,
                 "month": 0,
                 "country": country,
                 "subject": ', '.join(groups),
                 "league": user_data.league}]
    else:
        data = [{"username": username,
                 "cards": leaderboard.cards_today,
                 "streak": leaderboard.streak,
                 "time": leaderboard.time_today,
                 "retention": leaderboard.retention,
                 "month": leaderboard.cards_month,
                 "country": country,
                 "subject": ', '.join(groups),
                 "league": user_data.league}]
    return render(request, "user.html", {"data": data})


def render_league(league_name: str, request: WSGIRequest):
    data = []
    for counter, league in enumerate(League.objects.all().order_by("-xp"), start=1):
        if UserProfile.objects.filter(user=league.user).exists():
            user_profile = UserProfile.objects.get(user=league.user)
            if user_profile.league == league_name and league.xp != 0:
                data.append({"place": counter,
                             "username": user_profile.user.username,
                             "xp": league.xp,
                             "time": league.time_spent,
                             "reviews": league.cards,
                             "retention": league.retention,
                             "days_learned": league.days_studied, })
    return render(request, "leagues.html", {"data": data})


def alpha(request):
    return render_league("Alpha", request)

def beta(request):
    return render_league("Beta", request)

def gamma(request):
    return render_league("Gamma", request)


def delta(request):
    return render_league("Delta", request)


def privacy(request):
    return render(request, "privacy.html")
