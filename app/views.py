from django.http import HttpResponse
import csv

from app.models import UserCsv

def upload_csv(request):
    #key is for example 'csv' or 'csv_file' into request.FILES[]
    if request.method == 'POST' and request.FILES['csv']:
        csv_file = request.FILES['csv']
        decoded_file = csv_file.read().decode('utf-8')
        csv_data = csv.reader(decoded_file.splitlines(), delimiter=';')
        next(csv_data)
        
        for row in csv_data:
            firstname = row[0]
            lastname = row[1]
            email = row[2]
            user = UserCsv(firstname=firstname, lastname=lastname, email=email)
            user.save()
        
        return HttpResponse('CSV file uploaded successfully')
    
    return HttpResponse('Method not allowed')
