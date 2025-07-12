from django import forms
from elder_services.models import sub_services

class SubserviceForm(forms.ModelForm):
    class Meta:
        model = sub_services
        fields = ('subservice_name','subservice_id','price','image','service_id')

    def __init__(self,*args,**kwargs):
        super(SubserviceForm,self).__init__(*args,**kwargs)
        self.fields['subservice_name'].label="Subservice Name"    
        self.fields['subservice_id'].label="Subservice ID"
        self.fields['service_id'].label="Service"
        self.fields['price'].label="Price"
        self.fields['image'].label="Image"