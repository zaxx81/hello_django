"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import math

def rootRouteHandler(request):
    response = HttpResponse('<h1>Welcome to my app!</h1>')
    return response

def rectangleArea(request, height, width):
    return HttpResponse(f"<h1>Rectangle Area is {int(height) * int(width)}</h1>")
    
def rectanglePerimeter(request, height, width):
    return HttpResponse(f"<h1>Rectangle Perimeter is {(2*int(height)) + (2*int(width))}</h1>")

def circleArea(request, radius):
    return HttpResponse(f"<h1>Circle Area is {math.pi*(radius**2)}</h1>")

def circleCircumference(request, radius):
    return HttpResponse(f"<h1>Circle Circumference is {2*math.pi*radius}</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rootRouteHandler),
    path('rectangle/area/<int:height>/<int:width>', rectangleArea),
    path('rectangle/perimeter/<int:height>/<int:width>', rectanglePerimeter),
    path('circle/area/<int:radius>', circleArea),
    path('circle/circumference/<int:radius>', circleCircumference)
]