from django.shortcuts import render
from django.http import JsonResponse
from .models import PhotovoltaicPanel
from django.contrib.admin.views.decorators import staff_member_required
import redis
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in

# Redis setup
SERVER_IP = '127.0.0.1'
SERVER_PORT = 6379
PASSWORD = ''
DB = 0

client = redis.StrictRedis(
        host=SERVER_IP, 
        port=SERVER_PORT, 
        password=PASSWORD,
        db=DB,
        charset="utf-8", 
        decode_responses=True
    )

def energy_produced_consumed(request):
    #function that returns the total of energy produced and consumed in the last day, in a Json format.
    response = []
    daily_report = PhotovoltaicPanel.objects.filter().order_by("-date")
    for day in daily_report:
        response.append(
            {
                "produced_energy_in_watt": day.produced_energy,
                "consumed_energy_in_watt": day.consumed_energy,
            }
        )
    return JsonResponse(response[0])

def show_data(request):
    data = PhotovoltaicPanel.objects.filter().order_by("-date")
    return render (request, 'core/homepage.html', {"data":data})

@staff_member_required
def show_totals(request):
    panels = PhotovoltaicPanel.objects.all()
    total_produced = 0
    total_consumed = 0
    for p in panels:
        total_produced+=p.produced_energy
        total_consumed+=p.consumed_energy
    context = {
        "total_produced": total_produced,
        "total_consumed": total_consumed
    }
    return render (request, 'core/totals.html', context)

@receiver(user_logged_in)
def get_client_ip(sender, user, request, **kwargs):
    different_ip = False
    username = request.user.username
    last_ip = client.get(username)
    current_ip = request.META['REMOTE_ADDR']
    if last_ip is None:
        client.set(username, current_ip)
    elif current_ip != last_ip:
        client.set(username, current_ip)
        different_ip = True
    print(f"is_ip_different: {different_ip}")
    print(f"current: {current_ip}, last: {last_ip}")
    return different_ip