from django.urls import path
from fake_data.views import generate_fake_data

urlpatterns = [
    path('', generate_fake_data, name='fakeData'),
    path('generate-fake-data/', generate_fake_data, name='generate_fake_data'),
]
