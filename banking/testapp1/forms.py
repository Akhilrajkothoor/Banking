from django import forms
from testapp1.models import Banking,District,Branch

class BankingCreationForm(forms.ModelForm):
    class Meta:
        model= Banking
        fields='__all__'

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'district':forms.Select(attrs={'class':'form-control'}),
            'branch':forms.Select(attrs={'class':'form-control'}),
            'date_of_birth':forms.DateInput(attrs={'class':'form-control'}),
            'mobile' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'account_type' : forms.Select(attrs={'class':'form-control'}),
            'service_required' : forms.Select(attrs={'class':'form-control'}),
                     }


    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)
        self.fields['branch'].queryset=Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError,TypeError):
                pass

        elif self.instance.pk:
            self.fields['branch'].queryset= self.instance.district.branch_set.order_by('name')

