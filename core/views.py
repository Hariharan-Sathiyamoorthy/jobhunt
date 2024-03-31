from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Whishlist,Applied,Interview,Offer,Rejected
from .forms import WhishlistForm,AppliedForm,InterviewForm,OfferForm,RejectedForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.db import models
import calendar

@login_required(login_url='/users/login')
def getDashboard(request):
    whishlist = Whishlist.objects.filter(created_by=request.user)
    applied = Applied.objects.filter(created_by=request.user)
    interview = Interview.objects.filter(created_by=request.user)
    offer = Offer.objects.filter(created_by=request.user)
    rejected = Rejected.objects.filter(created_by=request.user)
    # get count of all models
    whishlist_count = whishlist.count()
    applied_count = applied.count()
    interview_count = interview.count()
    offer_count = offer.count()
    rejected_count = rejected.count()
    labels = [whishlist_count,applied_count,interview_count,offer_count,rejected_count]
    labels_json = json.dumps(labels, cls=DjangoJSONEncoder)
    # get month data and count for Applied and Rejected models
    applied_month = applied.values('created_at__month').annotate(count=models.Count('created_at__month'))
    rejected_month = rejected.values('created_at__month').annotate(count=models.Count('created_at__month'))
    count_applied_month = json.dumps([0,0]+[x['count'] for x in applied_month], cls=DjangoJSONEncoder)
    count_rejected_month = json.dumps([0,0]+[x['count'] for x in rejected_month], cls=DjangoJSONEncoder)

    context = {
        'whishlist':whishlist.order_by('-created_at')[:3],
        'applied':applied.order_by('-created_at')[:3],
        'interview':interview.order_by('-created_at')[:3],
        'offer':offer.order_by('-created_at')[:3],
        'rejected':rejected.order_by('-created_at')[:3],
        "labels_json":labels_json,
        "count_applied_month":count_applied_month,
        "count_rejected_month":count_rejected_month,
        'whishlist_count':whishlist_count,
        'applied_count':applied_count,
        'interview_count':interview_count,
        'offer_count':offer_count,
        'rejected_count':rejected_count
    }
    
    return render(request, 'Dashboard.html', context)


# Create your views here.
@login_required(login_url='/users/login')
def getIndexes(request,page):
    print(type(page))
    print(page == 'whishlist')
    if page == 'whishlist':
        whsihlists = Whishlist.objects.filter(created_by=request.user)
        return render(request, 'Whislist/Index.html', {'whsihlists':whsihlists})
    elif page == 'applied':
        applieds = Applied.objects.filter(created_by=request.user)
        return render(request, 'Applied/Index.html', {'applieds':applieds})
    elif page == 'interview':
        interviews = Interview.objects.filter(created_by=request.user)
        return render(request, 'Interview/Index.html', {'interviews':interviews})
    elif page == 'offer':
        offers = Offer.objects.filter(created_by=request.user)
        return render(request, 'Offer/Index.html', {'offers':offers})
    elif page == 'rejected':
        rejecteds = Rejected.objects.filter(created_by=request.user)
        return render(request, 'Rejected/Index.html', {'rejecteds':rejecteds})
    else:
        return HttpResponse('Page not found', status=404)
    
@login_required(login_url='/users/login')
def createJobs(request,page):
    user = User.objects.get(id=request.user.id)
    if page == 'whishlist':
        form = WhishlistForm()
        if request.method == 'POST':
            form = WhishlistForm(request.POST)
            if form.is_valid():
                whishlist = form.save(commit=False)
                whishlist.created_by = user
                whishlist.save()
                return redirect('core:whsihlist')
            else:
                print(form.errors)
                for field in form.errors:
                    form[field].field.widget.attrs['class'] += ' is-invalid'
        return render(request, 'Create.html', {'form':form, 'title':'Create Whishlist','button':'Create'})
    elif page == 'applied':
        form = AppliedForm()
        if request.method == 'POST':
            form = AppliedForm(request.POST)
            if form.is_valid():
                applied = form.save(commit=False)
                applied.created_by = user
                applied.save()
                return redirect('core:applied')
            else:
                print(form.errors)
                for field in form.errors:
                    form[field].field.widget.attrs['class'] += ' is-invalid'
        return render(request, 'Create.html', {'form':form, 'title':'Create Applied','button':'Create'})
    elif page == 'interview':
        form = InterviewForm()
        if request.method == 'POST':
            form = InterviewForm(request.POST)
            if form.is_valid():
                interview = form.save(commit=False)
                interview.created_by = user
                interview.save()
                return redirect('core:interview')
            else:
                print(form.errors)
                for field in form.errors:
                    form[field].field.widget.attrs['class'] += ' is-invalid'
        return render(request, 'Create.html', {'form':form, 'title':'Create Interview','button':'Create'})
    elif page == 'offer':
        form = OfferForm()
        if request.method == 'POST':
            form = OfferForm(request.POST)
            if form.is_valid():
                offer = form.save(commit=False)
                offer.created_by = user
                offer.save()
                return redirect('core:offer')
            else:
                print(form.errors)
                for field in form.errors:
                    form[field].field.widget.attrs['class'] += ' is-invalid'
        return render(request, 'Create.html', {'form':form, 'title':'Create Offer','button':'Create'})
    elif page == 'rejected':
        form = RejectedForm()
        if request.method == 'POST':
            form = RejectedForm(request.POST)
            if form.is_valid():
                rejected = form.save(commit=False)
                rejected.created_by = user
                rejected.save()
                return redirect('core:rejected')
            else:
                print(form.errors)
                for field in form.errors:
                    form[field].field.widget.attrs['class'] += ' is-invalid'
        return render(request, 'Create.html', {'form':form, 'title':'Create Rejected','button':'Create'})
    else:
        return HttpResponse('Page not found', status=404)

@login_required(login_url='/users/login')
def updateJobs(request,page,id):
    user = User.objects.get(id=request.user.id)
    if page == 'whishlist':
        whsihlist = Whishlist.objects.get(id=id)
        form = WhishlistForm(instance=whsihlist)
        if request.method == 'POST':
            form = WhishlistForm(request.POST, instance=whsihlist)
            if form.is_valid():
                if form.cleaned_data.get('move_to_applied') == True:
                    whsihlist.moveToApplied()
                    whsihlist.delete()
                else:
                    form.save()
                return redirect('core:whsihlist')
            else:
                print(form.errors)
                for field in form.errors:
                    form[field].field.widget.attrs['class'] += ' is-invalid'
        return render(request, 'Create.html', {'form':form, 'title':'Update Whishlist','button':'Update'})
    elif page == 'applied':
        applied = Applied.objects.get(id=id)
        form = AppliedForm(instance=applied)
        if request.method == 'POST':
            form = AppliedForm(request.POST, instance=applied)
            if form.is_valid():
                if form.cleaned_data.get('move_to_rejected') == True:
                    applied.moveToRejected()
                    applied.delete()
                elif form.cleaned_data.get('move_to_interview') == True:
                    applied.moveToInterview()
                    applied.delete()
                else:
                    form.save()
                return redirect('core:applied')
            else:
                print(form.errors)
                for field in form.errors:
                    form[field].field.widget.attrs['class'] += ' is-invalid'
        return render(request, 'Create.html', {'form':form, 'title':'Update Applied','button':'Update'})
    elif page == 'interview':
        interview = Interview.objects.get(id=id)
        form = InterviewForm(instance=interview)
        if request.method == 'POST':
            form = InterviewForm(request.POST, instance=interview)
            if form.is_valid():
                if form.cleaned_data.get('move_to_offer') == True:
                    interview.moveToOffer()
                    interview.delete()
                elif form.cleaned_data.get('move_to_rejected') == True:
                    interview.moveToRejected()
                    interview.delete()
                else:
                    form.save()
                return redirect('core:interview')
            else:
                print(form.errors)
                for field in form.errors:
                    form[field].field.widget.attrs['class'] += ' is-invalid'
        return render(request, 'Create.html', {'form':form, 'title':'Update Interview','button':'Update'})
    elif page == 'offer':
        offer = Offer.objects.get(id=id)
        form = OfferForm(instance=offer)
        if request.method == 'POST':
            form = OfferForm(request.POST, instance=offer)
            if form.is_valid():
                form.save()
                return redirect('core:offer')
            else:
                print(form.errors)
                for field in form.errors:
                    form[field].field.widget.attrs['class'] += ' is-invalid'
        return render(request, 'Create.html', {'form':form, 'title':'Update Offer','button':'Update'})
    elif page == 'rejected':
        rejected = Rejected.objects.get(id=id)
        form = RejectedForm(instance=rejected)
        if request.method == 'POST':
            form = RejectedForm(request.POST, instance=rejected)
            if form.is_valid():
                form.save()
                return redirect('core:rejected')
            else:
                print(form.errors)
                for field in form.errors:
                    form[field].field.widget.attrs['class'] += ' is-invalid'
        return render(request, 'Create.html', {'form':form, 'title':'Update Rejected','button':'Update'})
    else:
        return HttpResponse('Page not found', status=404)

@login_required(login_url='/users/login')
def viewJobItem(request,id,page):
    if page == 'whishlist':
        whsihlist = Whishlist.objects.get(id=id)
        return render(request, 'View.html', {'view':whsihlist,"name":"Whishlist"})
    elif page == 'applied':
        applied = Applied.objects.get(id=id)
        return render(request, 'View.html', {'view':applied,"name":"Applied"})
    elif page == 'interview':
        interview = Interview.objects.get(id=id)
        return render(request, 'View.html', {'view':interview,"name":"Interview"})
    elif page == 'offer':
        offer = Offer.objects.get(id=id)
        return render(request, 'View.html', {'view':offer,"name":"Offer"})
    elif page == 'rejected':
        rejected = Rejected.objects.get(id=id)
        return render(request, 'View.html', {'view':rejected,"name":"Rejected"})
    else:
        return HttpResponse('Page not found', status=404)

@login_required(login_url='/users/login')
def deleteJobs(request,page,id):
    if page == 'whishlist':
        whsihlist = Whishlist.objects.get(id=id)
        whsihlist.delete()
        return redirect('core:whsihlist')
    elif page == 'applied':
        applied = Applied.objects.get(id=id)
        applied.delete()
        return redirect('core:applied')
    elif page == 'interview':
        interview = Interview.objects.get(id=id)
        interview.delete()
        return redirect('core:interview')
    elif page == 'offer':
        offer = Offer.objects.get(id=id)
        offer.delete()
        return redirect('core:offer')
    elif page == 'rejected':
        rejected = Rejected.objects.get(id=id)
        rejected.delete()
        return redirect('core:rejected')
    else:
        return HttpResponse('Page not found', status=404)

