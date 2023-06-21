from django.urls import path
from measurement.views import SensorsView, SensorView, SensorUpdate, AddMeasurement

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path("sensors/", SensorsView.as_view()),
    path("sensorupdate/<pk>/", SensorUpdate.as_view()),
    path("sensors/<pk>/", SensorView.as_view()),
    path("measurements/", AddMeasurement.as_view()),
]
