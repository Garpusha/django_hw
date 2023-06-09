from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import MY_DATA
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse("bus_stations"))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    paginator = Paginator(MY_DATA, 5)
    page_no = request.GET.get("page", 1)
    page = paginator.get_page(page_no)
    context = {
            'bus_stations': page,
            'page': page,
    }
    return render(request, "stations/index.html", context)

