
# Create your views here.
from django.shortcuts import render,redirect
# from .forms import BankingCreationForm
# from bankapp1.models import Branch
# Create your views here.
# def create_view(request):
#     form = BankingCreationForm()
#     if request.method == 'POST':
#         form  = BankingCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('add')
#     return render(request,'home1.html',{'form':form})
#
# def load_branchs(request):
#     district_id=request.GET.get('district_id')
#     branchs= Branch.objects.filter(district_id=district_id).all()
#     return render(request,'branch_drowdown_list_options.html',{'branchs':branchs})

def demo(request):

   return render(request,"index.html")

def done(request):

   return render(request,"done.html")


