from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from matchapp.models import MatchModel
from humanapp.models import HumanModel
from matchapp.serializer import MatchModelSerializer
from humanapp.serializers import HumanModelSerializer


# Create your views here.

class MatchView(ListModelMixin, GenericAPIView, CreateModelMixin):
    queryset = MatchModel.objects.all()
    serializer_class = MatchModelSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            human = get_object_or_404(HumanModel, pk=kwargs['pk'])
            match = get_object_or_404(MatchModel, first_name=human.first_name,
                                      second_name=human.second_name,
                                      age=human.age,
                                      gender=human.gender)
            human_serializer = HumanModelSerializer(instance=human)
            match_serializer = MatchModelSerializer(instance=match)
            return Response({"matches": {'human': human_serializer.data,
                                         'match': match_serializer.data}})
        elif 'pk' in request.data:
            human = get_object_or_404(HumanModel, pk=request.data['pk'])
            match = get_object_or_404(MatchModel, first_name=human.first_name,
                                      second_name=human.second_name,
                                      age=human.age,
                                      gender=human.gender)
            human_serializer = HumanModelSerializer(instance=human)
            match_serializer = MatchModelSerializer(instance=match)
            return Response({"matches": {'human': human_serializer.data,
                                         'match': match_serializer.data}})
        matches = MatchModel.objects.all()
        humans = []
        for match in matches:
            human = get_object_or_404(HumanModel, first_name=match.first_name,
                                      second_name=match.second_name,
                                      age=match.age,
                                      gender=match.gender)
            humans.append(human)
        match_serializer = MatchModelSerializer(matches, many=True)
        human_serializer = HumanModelSerializer(humans, many=True)
        return Response({'humans': human_serializer.data,
                         'matches': match_serializer.data})
