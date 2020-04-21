from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from humanapp.forms import HumanModelForm
from humanapp.models import HumanModel
from django.core.paginator import Paginator
from humanapp.serializers import HumanSerializer, HumanModelSerializer
from matchapp.models import MatchModel

# Create your views here.


def create_model(request):
    if request.method == 'POST':
        form = HumanModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return JsonResponse({'200': 'OK'})
    form = HumanModelForm()
    humans = HumanModel.objects.all()
    paginator = Paginator(humans, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'humanapp/human.html', {'form': form,
                                                   'page_obj': page_obj
                                                   })

def explore(request, pk):
    if request.method == 'GET':
        human = get_object_or_404(HumanModel, pk=pk)
        return render(request, 'humanapp/explore.html', {'human': human})


def edit(request, pk):
    if request.method == 'POST':
        form = HumanModelForm(request.POST, request.FILES, instance=pk)
        if form.is_valid():
            form.save()
            return JsonResponse({'200': 'OK'})
        else:
            return JsonResponse({'400': 'Invalid'})
    form = HumanModelForm(instance=pk)
    return render(request, 'humanapp/edit.html', {'form': form})


class HumanView(ListModelMixin, GenericAPIView, CreateModelMixin):

    queryset = HumanModel.objects.all()
    serializer_class = HumanModelSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            human = get_object_or_404(HumanModel, pk=kwargs['pk'])
            serializer = HumanModelSerializer(instance=human)
            return Response({"human": serializer.data})
        elif 'pk' in request.data:
            human = get_object_or_404(HumanModel, pk=request.data['pk'])
            serializer = HumanModelSerializer(instance=human)
            return Response({"human": serializer.data})
        print(request.data)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        MatchModel.objects.create(first_name=request.data['first_name'],
                                  second_name=request.data['second_name'],
                                  age=request.data['age'],
                                  gender=request.data['gender'])
        print(request.data)
        return self.create(request)

    def put(self, request, *args, **kwargs):
        human = get_object_or_404(HumanModel, pk=kwargs['pk'])
        data = request.data.get('human')
        serializer = HumanSerializer(instance=human, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            human = serializer.save()
            return Response({'success': f'Human object {human.first_name} updated'})

    def delete(self, request, pk):
        human = get_object_or_404(HumanModel, pk=pk)
        human.delete()
        return Response({'message': f'Human object {human.first_name} has been deleted'}, status=204)