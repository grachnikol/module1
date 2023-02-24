from django.shortcuts import render
from django.http import HttpResponse


# Поздравляю, это ваш первый контроллер, который может, принять запрос, и отдать ответ с текстом, больше ничего
def main(request):
    return HttpResponse("Page for login")
