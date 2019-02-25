from django.core.paginator import Paginator
from django.db.models.functions import Extract
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic, View
from .forms import PostForm, ExpenseForm, LeaveForm, AnnouncementForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import CustomUser

from .models import Post, Announcement, Document


def birthdaylist(request):
    if(request.user.is_authenticated):

        users=CustomUser.objects.annotate(
           birth_date_month=Extract('birth_date', 'month'),
           birth_date_day=Extract('birth_date', 'day')
        ).order_by('birth_date_month', 'birth_date_day').all()

        Months={
            1:'January',
            2: 'February',
            3:'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December',
        }
        context={
            'users':users,
            'month':Months
        }
        return render(request,'dashboard/birthdaylist.html',context=context)
    else:
        return redirect('login')


def profile(request):
    if request.user.is_authenticated:
            return render(request,'dashboard/profile/profile.html')
    else:
        return redirect('login')

def home(request):
    announces = Announcement.objects.order_by('-created_date').all()
    paginator = Paginator(announces, 3)
    page = request.GET.get('page')
    announces = paginator.get_page(page)



    if(request.user.is_authenticated):
        context={
            'announcements' : announces,
        }
        return render(request,'dashboard/home.html',context=context)
    else:
        return redirect('login')


def new_posts(request):
    if request.method== 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()

            return redirect('dashboard:posts')
    else:
        if (request.user.is_authenticated):

            form = PostForm()
            return render(request, 'dashboard/post/new_post.html', {'form': form})
        else:
            return redirect('login')


def PostLists(request):

    exp = Post.objects.order_by('-date').all()
    paginator = Paginator(exp, 3)
    page = request.GET.get('page')
    exp = paginator.get_page(page)
    context = {
        'object_list': exp
    }
    if (request.user.is_authenticated):
        return render(request, 'dashboard/post/postlist.html', context=context)
    else:
        return redirect('login')


def approval(request):
    leaves = request.user.leaveapplication_set.all().order_by('-created_date')
    paginator = Paginator(leaves, 3)
    page = request.GET.get('page')
    leaves = paginator.get_page(page)
    context = {
        'leaves': leaves,
    }
    if request.user.is_authenticated:
        return render(request, 'dashboard/leaves/approval.html', context=context)
    else:
        return redirect('home')


def applyleave(request):
    if request.method== 'POST':
        form =  LeaveForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('dashboard:approval')
    else:
        if request.user.is_authenticated:
            form = LeaveForm()
            return render(request, 'dashboard/leaves/applyleave.html', {'form': form})
        else:
            return redirect('login')



class PostDelete(UserPassesTestMixin,generic.DeleteView):

    model = Post
    raise_exception = True
    template_name = 'dashboard/post/post_delete.html'
    success_url = reverse_lazy('dashboard:posts')
    def test_func(self):
        self.object=self.get_object()
        return self.object.author == self.request.user


def expenseapproval(request):
    expenses = request.user.expenseapplication_set.all().order_by('-created_date')
    paginator = Paginator(expenses, 3)
    page = request.GET.get('page')
    expenses = paginator.get_page(page)
    context = {
        'expenses': expenses,
    }
    if (request.user.is_authenticated):
        return render(request, 'dashboard/expenses/expenseapproval.html', context=context)
    else:
        return redirect('home')




def applyexpense(request):
    if request.method== 'POST':

        form = ExpenseForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('dashboard:expenseapproval')
        else:
            return HttpResponse('Somethings Fishy')
    else:
        if (request.user.is_authenticated):
            form = ExpenseForm()
            return render(request, 'dashboard/expenses/applyexpense.html', {'form': form})
        else:
            return redirect('login')


def announcements(request):
    if request.method== 'POST':

        form = AnnouncementForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('dashboard:home')
        else:
            return HttpResponse('Somethings Fishy')
    else:
        if (request.user.is_authenticated):
            form = AnnouncementForm()
            return render(request, 'dashboard/announcement.html', {'form': form})
        else:
            return redirect('login')

class ProfileEdit(UserPassesTestMixin,generic.UpdateView):
    model = CustomUser
    raise_exception = True
    fields = ['email','name','gender','resume', 'blood_group', 'contact_number', 'emergency_contact_name','emergency_contact_number', 'address']
    success_url = reverse_lazy('dashboard:profile')
    template_name = 'dashboard/profile/edit.html'

    def test_func(self):
        self.object = self.get_object()
        return self.object == self.request.user



class Documents(LoginRequiredMixin,generic.ListView):
    raise_exception = True
    model = Document
    template_name = 'dashboard/documents.html'
