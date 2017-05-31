from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    request.session['id']=1
    allcomp = ComparisonTbl.objects.all()
    return render(request, "index.html", {'allcomp':allcomp})


def comparison(request, comparison_id):
    if request.method == 'POST':
        if 'Vote1' in request.POST:
            print "I voted 1"
        elif 'Vote2' in request.POST:
            print "I voted 2"
    comparison=ComparisonTbl.objects.get(ComparisonId=comparison_id)
    user=UserTbl.objects.get(UserId=request.session['id'])
    comment = CommentTbl.objects.filter(ComparisonId=comparison_id)
    print comment
    return render(request, "comparison.html",{'comparison': comparison, 'user': user, 'comment':comment})

