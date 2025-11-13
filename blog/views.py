from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError
from .models import Users
import json


def home_page(request):
    return render(request, "index.html")

def forgot(request):
    return render(request, "forgot.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        try:
            account = Users.objects.get(username=username)
            if check_password(password, account.password):
                return render(request, "main.html", {"user": account})
            else:
                return render(request, "index.html", {"error": "Xato parol!"})
        except Users.DoesNotExist:
            return render(request, "index.html", {"error": "Foydalanuvchi topilmadi!"})

    return render(request, "index.html")

@csrf_exempt
def api_login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            try:
                account = Users.objects.get(username=username)
                if check_password(password, account.password):
                    return JsonResponse({"success": True, "username": account.username})
                else:
                    return JsonResponse({"success": False, "error": "Xato parol!"}, status=400)
            except Users.DoesNotExist:
                return JsonResponse({"success": False, "error": "Foydalanuvchi topilmadi!"}, status=404)

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Faqat POST method ruxsat etilgan"}, status=405)


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        surname = request.POST.get("surname")  
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            Users.objects.create(
                username=username,
                surname=surname,
                email=email,
                password=make_password(password)
            )
            return redirect("blog:login")

        except IntegrityError:
            return render(request, "createAccaunt.html", {"error": "Bunday username yoki email allaqachon mavjud!"})

    return render(request, "createAccaunt.html")


@csrf_exempt
def api_signup(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            surname = data.get("surname")   
            email = data.get("email")
            password = data.get("password")

            if not username or not surname or not email or not password:
                return JsonResponse({"success": False, "error": "Majburiy maydonlar to'ldirilmagan!"}, status=400)

            if Users.objects.filter(username=username, surname=surname).exists():
                return JsonResponse({"success": False, "error": "Bu username + surname kombinatsiyasi allaqachon mavjud!"}, status=400)

            if Users.objects.filter(email=email).exists():
                return JsonResponse({"success": False, "error": "Bu email allaqachon mavjud!"}, status=400)

            account = Users.objects.create(
                username=username,
                surname=surname,
                email=email,
                password=make_password(password)
            )

            return JsonResponse({"success": True, "username": account.username})

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "JSON format xato!"}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Faqat POST method ruxsat etilgan"}, status=405)



def main(request):
    return render(request, "main.html")
