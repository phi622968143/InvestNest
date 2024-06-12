# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/<int:user_id>/', views.user_portfolio, name='portfolio'),
    path('account/<int:account_id>/', views.account_detail, name='account_detail'),
    # path('dividend/<int:user_id>/', views.dividend_report, name='dividend'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
