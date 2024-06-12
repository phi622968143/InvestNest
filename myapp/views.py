# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User, Account, Trade, Dividend, Receive, Distribute


@login_required
def user_portfolio(request, user_id):
    user = get_object_or_404(User, id=user_id)
    accounts = Account.objects.filter(user=user)

    if request.method == 'POST':
        if 'add_account' in request.POST:
            bank_name = request.POST.get('bank_name')
            acc_balance = request.POST.get('acc_balance')
            open_date = request.POST.get('open_date')
            Account.objects.create(user=user, bank_name=bank_name, acc_balance=acc_balance, open_date=open_date)
            messages.success(request, 'Account added successfully')
            return redirect('portfolio', user_id=user_id)
        elif 'delete_account' in request.POST:
            account_id = request.POST.get('account_id')
            Account.objects.filter(acc_id=account_id).delete()
            messages.success(request, 'Account deleted successfully')
            return redirect('portfolio', user_id=user_id)
        elif 'update_account' in request.POST:
            account_id = request.POST.get('account_id')
            account = get_object_or_404(Account, acc_id=account_id)
            account.bank_name = request.POST.get('bank_name')
            account.acc_balance = request.POST.get('acc_balance')
            account.open_date = request.POST.get('open_date')
            account.save()
            messages.success(request, 'Account updated successfully')
            return redirect('portfolio', user_id=user_id)

    context = {
        'user': user,
        'accounts': accounts,
    }
    return render(request, 'portfolio.html', context)

from decimal import Decimal


@login_required
def account_detail(request, account_id):
    account = get_object_or_404(Account, acc_id=account_id)
    trades = Trade.objects.filter(account=account)
    receives = Receive.objects.filter(account=account)

    if request.method == 'POST':
        if 'add_trade' in request.POST:
            stock_name = request.POST['stock_name']
            stock_code = request.POST['stock_code']
            action = request.POST['action']
            price = Decimal(request.POST['price'])
            quantity = int(request.POST['quantity'])
            date = request.POST['date']

            if action == 'buy':
                account.acc_balance -= price * quantity
            elif action == 'sell':
                account.acc_balance += price * quantity

            Trade.objects.create(account=account, stock_name=stock_name, stock_code=stock_code, action=action, price=price, quantity=quantity, date=date)
            account.save()
            messages.success(request, 'Trade added successfully')
            return redirect('account_detail', account_id=account_id)
        elif 'delete_trade' in request.POST:
            trade_id = request.POST.get('trade_id')
            Trade.objects.filter(trade_id=trade_id).delete()
            messages.success(request, 'Trade deleted successfully')
            return redirect('account_detail', account_id=account_id)
        elif 'update_trade' in request.POST:
            trade_id = request.POST.get('trade_id')
            trade = get_object_or_404(Trade, trade_id=trade_id)
            trade.stock_name = request.POST['stock_name']
            trade.stock_code = request.POST['stock_code']
            trade.action = request.POST['action']
            trade.price = Decimal(request.POST['price'])
            trade.quantity = int(request.POST['quantity'])
            trade.date = request.POST['date']

            if trade.action == 'buy':
                account.acc_balance -= trade.price * trade.quantity
            elif trade.action == 'sell':
                account.acc_balance += trade.price * trade.quantity

            trade.save()
            account.save()
            messages.success(request, 'Trade updated successfully')
            return redirect('account_detail', account_id=account_id)
        elif 'add_dividend' in request.POST:
            stock_name = request.POST['stock_name']
            stock_code = request.POST['stock_code']
            dividend_per_share = Decimal(request.POST['dividend_per_share'])
            date = request.POST['date']

            total_quantity = sum(t.quantity for t in trades.filter(stock_name=stock_name))
            receive_amount = dividend_per_share * total_quantity
            Receive.objects.create(account=account, stock_name=stock_name, receive_amount=receive_amount, receive_date=date, quantity=total_quantity)
            messages.success(request, 'Dividend added successfully')
            return redirect('account_detail', account_id=account_id)

    total_cost = sum(t.price * t.quantity for t in trades if t.action == 'buy') - sum(t.price * t.quantity for t in trades if t.action == 'sell')
    total_dividend = sum(r.receive_amount for r in receives)
    overall_yield = (total_dividend / total_cost * 100) if total_cost else 0

    for trade in trades:
        trade.dividend_yield = 0
        trade_receives = receives.filter(stock_name=trade.stock_name)
        if trade_receives.exists():
            total_dividend_for_stock = sum(r.receive_amount for r in trade_receives)
            total_quantity_for_stock = sum(r.quantity for r in trade_receives)
            if total_quantity_for_stock > 0:
                dividend_per_share = total_dividend_for_stock / total_quantity_for_stock
                trade.dividend_yield = (dividend_per_share * trade.quantity) / (trade.price * trade.quantity) * 100

    context = {
        'account': account,
        'trades': trades,
        'receives': receives,
        'total_dividend': total_dividend,
        'total_cost': total_cost,
        'overall_yield': overall_yield,
    }
    return render(request, 'dividend_report.html', context)


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        user_balance = request.POST.get('user_balance', 0.00)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('register')
        
        user = User(name=name, phone=phone, email=email, password=password, user_balance=user_balance)
        user.set_password(password)
        user.save()
        messages.success(request, 'User registered successfully')
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render, redirect

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    user_id = request.user.id
    context = {
        'user_id': user_id,
    }
    return render(request, 'index.html', context)

