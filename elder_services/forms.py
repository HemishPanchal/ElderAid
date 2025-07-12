from django import forms
from .models import services

class ServiceForm(forms.ModelForm):
    # def __init__(self,*args,**kwargs):
    #     super(CategoryForm,self).__init__(*args,**kwargs)
    #     self.fields['catname'].empty_label="Select Category"

    class Meta:
        model = services
        fields = ('service_name','service_id')

    def __init__(self,*args,**kwargs):
        super(ServiceForm,self).__init__(*args,**kwargs)
        self.fields['service_id'].label="Service ID"    
        self.fields['service_name'].label="Service Name"