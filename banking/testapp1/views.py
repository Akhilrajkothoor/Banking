from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .forms import BankingCreationForm
from .models import Branch
from testapp1.models import District
# Create your views here.
def create_view(request):
    form = BankingCreationForm()
    if request.method == 'POST':
        form = BankingCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')
    return render(request,'home.html',{'form':form})

def load_branchs(request):
    district_id=request.GET.get('district_id')
    branchs= Branch.objects.filter(district_id=district_id).all()
    return render(request,'branch_drowdown_list_options.html',{'branchs':branchs})