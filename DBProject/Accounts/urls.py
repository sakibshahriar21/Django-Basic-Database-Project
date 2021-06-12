from django.urls import path
from . import views

urlpatterns = [ path("register",views.register,name="register"),
                path("login",views.login,name='login'),
                path("logout", views.logout, name='logout'),

                path("page1",views.page1,name='page1'),
                path("page2",views.page2,name='page2'),
                path("page3",views.page3,name='page3'),
                path("page4",views.page4,name='page4'),
                path("page5",views.page5,name='page5'),
                path("page6",views.page6,name='page6'),
                path("page7",views.page7,name='page7'),

                ]


