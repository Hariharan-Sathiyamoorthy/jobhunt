from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Whishlist,Applied,Interview,Offer,Rejected
from .forms import WhishlistForm,AppliedForm,InterviewForm,OfferForm,RejectedForm
from django.contrib.auth.models import User

def getDashboard(request):
    whishlist = Whishlist.objects.filter(created_by=request.user)
    applied = Applied.objects.filter(created_by=request.user)
    interview = Interview.objects.filter(created_by=request.user)
    offer = Offer.objects.filter(created_by=request.user)
    rejected = Rejected.objects.filter(created_by=request.user)
    return render(request, 'Dashboard.html',{'whishlist':whishlist,'applied':applied,'interview':interview,'offer':offer,'rejected':rejected})


# Create your views here.

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
        return render(request, 'Whislist/Create.html', {'form':form, 'title':'Create Whishlist','button':'Create'})
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
        return render(request, 'Applied/Create.html', {'form':form, 'title':'Create Applied','button':'Create'})
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
        return render(request, 'Interview/Create.html', {'form':form, 'title':'Create Interview','button':'Create'})
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
        return render(request, 'Offer/Create.html', {'form':form, 'title':'Create Offer','button':'Create'})
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
        return render(request, 'Rejected/Create.html', {'form':form, 'title':'Create Rejected','button':'Create'})
    else:
        return HttpResponse('Page not found', status=404)

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
        return render(request, 'Whislist/Create.html', {'form':form, 'title':'Update Whishlist','button':'Update'})
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
        return render(request, 'Applied/Create.html', {'form':form, 'title':'Update Applied','button':'Update'})
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
        return render(request, 'Interview/Create.html', {'form':form, 'title':'Update Interview','button':'Update'})
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
        return render(request, 'Offer/Create.html', {'form':form, 'title':'Update Offer','button':'Update'})
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
        return render(request, 'Rejected/Create.html', {'form':form, 'title':'Update Rejected','button':'Update'})
    else:
        return HttpResponse('Page not found', status=404)

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

