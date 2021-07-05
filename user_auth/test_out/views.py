from django.contrib.auth import authenticate
import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


@csrf_exempt
def post(request):
    data = json.loads(request.body)
    username = data.get("username")
    if User.objects.filter(username=username):
        return HttpResponse("record duplication warning", status=200)
    first_name = data.get("name")
    email = data.get("email")
    if User.objects.filter(email=email):
        return HttpResponse("record duplication warning", status=200)
    password = data.get("password")
    date_joined = data.get("Date")
    new_user = User.objects.create_user(username=username, first_name=first_name, email=email, password=password,
                                        date_joined=date_joined)
    new_user.save()
    return HttpResponse("complete", status=200)


def login_response(request):
    data = json.loads(request.body)
    usr_name = data.get("username")
    usr_password = data.get("password")
    temp = authenticate(username=usr_name, password=usr_password)
    if temp is None:
        return JsonResponse({"message":"user not found"}, status=200)
    data = {"message": "success"}
    return JsonResponse(data, status=200)
