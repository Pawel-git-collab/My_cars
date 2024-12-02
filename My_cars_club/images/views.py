import csv
import io
import xml
from io import BytesIO
from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404

from .models import Car, Video
from .forms import CarForm, SearchCarForm, VideoForm, CSVUploadForm
from .serializers import CarSerializer, XMLSerializer
from django.shortcuts import redirect
from PIL import Image
import json
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import xml.etree.ElementTree as ET
from rest_framework import generics
from rest_framework import routers, serializers, viewsets
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
import pandas as pd


def home(request):
    template = "home.html"
    queryset = Car.objects.all()
    videos = Video.objects.all()
    context = {
        "object_list": queryset,
        'videos': videos,
    }
    return render(request, template, context)


def resize_image(image_car, size=(310, 160)):
    img = Image.open(image_car)

    img = img.resize(size, Image.ANTIALIAS)

    img_io = BytesIO()
    img.save(img_io, format='JPEG')

    return ContentFile(img_io.getvalue(), name=image_car.name)


def new_car(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            image_upload = form.save(commit=False)

            image_upload.image_car = resize_image(request.FILES['image_car'])

            image_upload.save()
            return redirect('home')
    else:
        form = CarForm()
    return render(request, 'new_car.html', {'form': form})


def car_edit(request, car_id):
    car = Car.objects.get(pk=car_id)
    form = CarForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'update_car.html', {'car': car, 'form': form})


def car_delete(request, car_id):
    car = Car.objects.get(pk=car_id)
    car.delete()
    return redirect('home')


def edit_and_delete_car(request):
    template = "edit_and_delete_car.html"
    queryset = Car.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template, context)


def search_car(request):
    form = SearchCarForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchCarForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Car.objects.filter(id__icontains=query) | Car.objects.filter(
                cars__icontains=query)

    return render(request, 'search_car.html', {'query': query, 'form': form, 'results': results})


def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})


def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})


def import_json_file(request):
    if request.method == 'POST' and request.FILES['json_file']:
        json_file = request.FILES['json_file']
        data = json.load(json_file)
        for item in data:
            car = Car(
                cars=item['cars'],
                speed=item['speed'],
                price=item['price'],
                mileage=item['mileage'],
                created=item['created'],
                image_car=item['image_car'],
            )
            car.save()
        return render(request, 'success.html')
    return render(request, 'import_json.html')


def upload_xml(request):
    if request.method == 'POST' and request.FILES['xml_file']:
        xml_file = request.FILES['xml_file']

        tree = ET.parse(xml_file)
        root = tree.getroot()

        for elem in root:
            cars = elem.find('cars').text
            speed = elem.find('speed').text
            price = elem.find('price').text
            mileage = elem.find('mileage').text
            created = elem.find('created').text
            image_car = elem.find('image_car').text
            # Save each car to the database
            Car.objects.create(cars=cars, speed=speed, price=price, mileage=mileage, created=created,
                               image_car=image_car)

        return render(request, 'success_xml.html')

    return render(request, 'upload_xml.html')


def upload_csv(request):
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']

            data = pd.read_csv(csv_file)

            for _, row in data.iterrows():
                Car.objects.create(
                    cars=row['cars'],
                    speed=row['speed'],
                    price=row['price'],
                    mileage=row['mileage'],
                    image_car=row['image_car']
                )

            return render(request, 'success_csv.html')
    else:
        form = CSVUploadForm()

    return render(request, 'upload_csv.html', {'form': form})


class JsonCarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class XMLCarViewSet(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = XMLSerializer
    parser_classes = (XMLParser,)
    renderer_classes = (XMLRenderer,)


def export_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    writer = csv.writer(response)

    writer.writerow(['cars', 'speed', 'price', 'mileage', 'image_car'])

    for obj in Car.objects.all():
        writer.writerow([obj.cars, obj.speed, obj.price, obj.mileage, obj.image_car])

    return response
