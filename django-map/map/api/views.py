from rest_framework import generics

from map.models import Problem
from .serializers import PointsSerializer, SavePointSerializer

class PointsView(generics.ListAPIView):
    serializer_class = PointsSerializer
    queryset = Problem.objects.all()

class SavePointView(generics.CreateAPIView):
    serializer_class = SavePointSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    