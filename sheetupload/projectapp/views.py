from django.shortcuts import render
from django.http import HttpResponse
from .resources import PersonResource
from tablib import Dataset
from .models import Person


def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="merged.csv"'
    return response


def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES.getlist('myfile')
        for person in new_persons: 
            imported_data = dataset.load(person.read(), format='xlsx')

            for data in imported_data:
                value = Person(
                    data[0],
                    data[1],
                    data[2],
                    data[3]
                )
                value.save()



    return render(request, 'projectapp/input.html')