# I have created this file - Dipta
from django.http import HttpResponse


def index(request):
    return HttpResponse("Home")


def remove_punc(request):
    return HttpResponse("Remove Punctuation")


def cap_first(request):
    return HttpResponse("Capitalize")


def newlineremove(request):
    return HttpResponse("Remove New Line")


def spaceremove(request):
    return HttpResponse("Remove Space")


def charactercount(request):
    return HttpResponse("Count Characters")
