from django.shortcuts import render, HttpResponseRedirect
from django.db.models import F
from .models import *

# Create your views here.


def index(request):
    request.session['id']=2
    allcomp = ComparisonTbl.objects.all()
    return render(request, "index.html", {'allcomp':allcomp})


def comparison(request, comparison_id):
    comparison = ComparisonTbl.objects.get(ComparisonId=comparison_id)
    user = UserTbl.objects.get(UserId=request.session['id'])
    if request.method == 'POST':
        if 'Vote1' in request.POST:
            ComparisonTbl.objects.filter(ComparisonId=comparison_id).update(Vote1=F('Vote1') + 1)
            return HttpResponseRedirect("/mycomparison/comparison/" + comparison_id + "/")
        elif 'Vote2' in request.POST:
            ComparisonTbl.objects.filter(ComparisonId=comparison_id).update(Vote2=F('Vote2') + 1)
            return HttpResponseRedirect("/mycomparison/comparison/" + comparison_id + "/")
        elif 'Comment' in request.POST:
            text_box_value = request.POST['commenttext']
            comm = CommentTbl(UserId=user, ComparisonId=comparison, Comments=text_box_value)
            comm.save()
            return HttpResponseRedirect("/mycomparison/comparison/"+comparison_id+"/")

    comment = CommentTbl.objects.filter(ComparisonId=comparison_id)
    return render(request, "comparison.html",{'comparison': comparison, 'user': user, 'comment':comment})

