from django.shortcuts import render
from .models import Food
from .models import Consumed
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home(request):
    import requests
    import json
    user = request.user
    if request.method == 'POST':
      if 'Search' in request.POST:
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url+query, headers = {'X-Api-Key': 'EwTuQy5KMYy9Ei9dL9gYYA==5aQ0iZ36YBVAPCwN'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
            try:
              consume = Consumed.objects.filter(user = user)
            except:
              consume = None
            if consume:
              consume = Consumed.objects.get(user=user)
              consume.save()
            else:
              consume =  Consumed.objects.create(user=user)
            consumed_foods = consume.foods.all()
            print(consumed_foods)
        except Exception as e:
            api = "opps there was an error"
            print(e)
        return render(request, 'home.html',{'api':api, 'consumed_foods':consumed_foods})
      elif 'Add' in request.POST:
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url+query, headers = {'X-Api-Key': 'EwTuQy5KMYy9Ei9dL9gYYA==5aQ0iZ36YBVAPCwN'})
        try:
            api2 = json.loads(api_request.content)
            print(api_request.content)
            try:
              consume = Consumed.objects.filter(user = user)
            except:
              consume = None
            if consume:
              consume = Consumed.objects.get(user=user)
              consume.save()
              print(2)
            else:
              consume = Consumed.objects.create(user=user)
              consume.save()
            foodie = Food.objects.create(name = api2[0]["name"], calories = api2[0]["calories"], carbs = api2[0]["carbohydrates_total_g"], fats = api2[0]["fat_total_g"], protein = api2[0]["protein_g"], food_consumed = consume)
            consumed_foods = consume.foods.all()
        except Exception as e:
            api2 = "opps there was an error"
            print(e)
        return render(request, 'home.html',{'api2':api2, 'consumed_foods':consumed_foods})
    else:
      try:
        consume = Consumed.objects.filter(user = user)
      except:
        consume = None
      if consume:
        consume = Consumed.objects.get(user=user)
        consume.save()
      else:
        consume =  Consumed.objects.create(user=user)
        consume.save()
      consumed_foods = consume.foods.all()
      return render(request, 'home.html',{'consumed_foods':consumed_foods})

def delete(request, id):
  food_delete = Food.objects.get(id=id)
  food_delete.delete()
  return HttpResponseRedirect(reverse('home'))

