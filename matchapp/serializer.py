from rest_framework.serializers import ModelSerializer
from matchapp.models import MatchModel


class MatchModelSerializer(ModelSerializer):
    class Meta:
        model = MatchModel
        fields = ['id', 'first_name', 'second_name', 'age', 'gender']
