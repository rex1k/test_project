from humanapp.models import HumanModel
from django.forms import ModelForm, widgets


class HumanModelForm(ModelForm):

    class Meta:
        model = HumanModel
        genders = (('Male', 'M'),
                   ('Female', 'F'),
                   ('Beaver', 'B'))
        fields = ['avatar', 'first_name', 'second_name', 'age', 'gender']
        widgets = {'gender': widgets.RadioSelect(choices=genders)}
