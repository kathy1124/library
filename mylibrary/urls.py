"""
URL configuration for mylibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mytext import views as mv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mv.homepage, name='homepage'),
    path('post/<slug:slug>/', mv.postPage, name="postPage"),
    path('post', mv.show_all_post, name="show_all_post"),
    path('post/<int:post_id>/comments', mv.show_comments, name='show-comments'),
    path('addComment/',mv.addComment,name='addComents'),
    path('postPage', mv.postPage, name="postPage"),

    path('register/', mv.register, name= 'register'),
    path('login/',mv.login, name='login'),
    path('changePassword/',mv.changePassword,name='changePassword'),
    path('logout/',mv.logouts, name='logout'),

    path('search/',mv.index, name='search'),

    path('condition/',mv.condition,name='condition'),
    path('borrowBook/<int:post_id>/borrow',mv.borrow_book, name='borrowBook'),
    path('borrowList/',mv.getBorrowListByUser,name='borrowList'),

    path('returnBook/',mv.returnBook,name='returnBook'),
    path('returnBookPage/',mv.returnBookPage,name='returnBookPage'),

    path('addBook/',mv.addBook,name='addBook'),
    path('bookManagePage/',mv.bookManagePage,name='bookManagePage'),
    path('bookModify/<int:post_id>',mv.bookModify,name='bookModify'),
]
