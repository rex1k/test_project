from rest_framework import serializers
from humanapp.models import HumanModel
from rest_framework.serializers import ModelSerializer


class HumanSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    first_name = serializers.CharField(max_length=40)
    second_name = serializers.CharField(max_length=40)
    age = serializers.IntegerField()
    gender = serializers.ChoiceField(choices=(('Male', 'M'), ('Female', 'F')))
    avatar = serializers.ImageField(use_url=True)

    def create(self, validated_data):
        return HumanModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.second_name = validated_data.get('second_name', instance.second_name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance


class HumanModelSerializer(ModelSerializer):
    class Meta:
        model = HumanModel
        fields = ['id', 'first_name', 'second_name', 'age', 'gender', 'avatar']
