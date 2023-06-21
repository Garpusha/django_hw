# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer
from rest_framework.response import Response


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        Sensor(
            name=request.data["name"], description=request.data["description"]
        ).save()
        return Response("Post OK")


# @api_view(['PATCH'])
class SensorUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def delete(self, request, pk):
        Sensor(id=pk).delete()
        return Response("Delete OK")

    def patch(self, request, pk):
        Sensor(id=pk, description=request.data["description"]).save()
        return Response("Patch OK")


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class AddMeasurement(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        s_id = request.data["sensor"]
        sensor = Sensor.objects.get(id=s_id)
        Measurement(
            sensor=sensor, temperature=float(request.data["temperature"])
        ).save()
        return Response("Post OK")
