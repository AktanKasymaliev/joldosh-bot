from django.db import models
from rest_framework import serializers

from django.utils import timezone
from django.utils.datastructures import MultiValueDictKeyError

from map.models import Problem, ProblemImage

class ProblemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemImage
        fields = (
            "id", 
            "problem",
            "image",
            )

class SavePointSerializer(serializers.ModelSerializer):
    images = ProblemImageSerializer(many=True, required=False)

    class Meta:
        model = Problem
        fields = (
            "id", 
            "description", 
            "latitude",
            "longitude",
            "comment",
            "created_at",
            "images"
            )
    
    def create(self, validated_data):
        request = self.context.get("request")
        problem = Problem.objects.create(created_at=timezone.now, **validated_data)

        try:
            for image in request.data.pop('images'):
                created = ProblemImage.objects.create(image=image, problem=problem)
                problem.images.add(created)
        except (MultiValueDictKeyError, KeyError):
            pass
        return problem
            

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProblemImageSerializer(instance.images.all(), many=True).data
        return representation


class PointsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = (
            "id", 
            "description", 
            "latitude",
            "longitude",
            "comment",
            "created_at",
            )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProblemImageSerializer(instance.images.all(), many=True).data
        return representation