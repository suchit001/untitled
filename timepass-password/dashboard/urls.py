from django.urls import path
from . import views
app_name='dashboard'


urlpatterns = [
    path('birthday_list/',views.birthdaylist,name='birthday_list'),

    path('profile/', views.profile, name='profile'),
    path('home/',views.home,name='home'),
    path('new_post/',views.new_posts,name='new_posts'),
    path('posts/', views.PostLists, name='posts'),
    path('announcements/', views.announcements, name='announcements'),
    path('approval/', views.approval, name='approval'),
    path('applyleave/', views.applyleave, name='applyleave'),
    path('post/delete/<int:pk>',views.PostDelete.as_view(),name='delete'),
    path('expenseapproval/', views.expenseapproval, name='expenseapproval'),
    path('applyexpense/', views.applyexpense, name='applyexpense'),
    path('profile/edit/<int:pk>',views.ProfileEdit.as_view(),name='profileEdit'),
    path('documents/',views.Documents.as_view(),name='documents'),
]
