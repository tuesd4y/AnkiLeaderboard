from . import views, api3

from django.urls import path, re_path
from django.http import HttpResponse

app_name = "main"
urlpatterns = [
    re_path(
        r"^robots.txt",
        lambda x: HttpResponse("User-Agent: *\nDisallow: /", content_type="text/plain"),
        name="robots_file",
    ),
    # Website
    path("", views.reviews, name="reviews"),
    path("time/", views.time, name="time"),
    path("streak/", views.streak, name="streak"),
    path("retention/", views.retention, name="retention"),
    path(r"user/<username>/", views.user, name="user"),
    path("alpha/", views.alpha, name="alpha"),
    path("beta/", views.beta, name="beta"),
    path("gamma/", views.gamma, name="gamma"),
    path("delta/", views.delta, name="delta"),
    path("privacy/", views.privacy, name="privacy"),
    # API v3
    path("api/v3/signUp/", api3.signUp, name="signUp"),
    path("api/v3/logIn/", api3.logIn, name="logIn"),
    path("api/v3/deleteAccount/", api3.deleteAccount, name="deleteAccount"),
    path("api/v3/changeUsername/", api3.changeUsername, name="changeUsername"),
    # path('api/v3/resetPassword/', api3.resetPassword, name="resetPassword"),
    # path('api/v3/newPassword/<slug:token>', api3.newPassword, name="newPassword"),
    path("api/v3/groups/", api3.groups, name="groups"),
    path("api/v3/joinGroup/", api3.joinGroup, name="joinGroup"),
    path("api/v3/createGroup/", api3.createGroup, name="createGroup"),
    path("api/v3/leaveGroup/", api3.leaveGroup, name="leaveGroup"),
    path("api/v3/manageGroup/", api3.manageGroup, name="manageGroup"),
    path("api/v3/banUser/", api3.banUser, name="banUser"),
    path("api/v3/reportUser/", api3.reportUser, name="reportUser"),
    path("api/v3/setBio/", api3.setBio, name="setBio"),
    path("api/v3/getBio/", api3.getBio, name="getBio"),
    path("api/v3/getUserinfo/", api3.getUserinfo, name="getUserinfo"),
    path("api/v3/users/", api3.users, name="users"),
    path("api/v3/season/", api3.season, name="season"),
    path("api/v3/sync/", api3.sync, name="sync"),
]
