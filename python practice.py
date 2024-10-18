def open_account():
    print("새로운 계좌가 생성되었습니다.")
#입금
def deposit(balance,money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance + money
#출금
def withdraw(balance,money):
    if balance>=money:
        print("출금이 완료되었습니다. 잔액은{0}원 입니다.".format(balance-money))
        return balance - money 
    else:
         print("출금이 불가합니다. 잔액은 {0}원입니다.".format(balance))
#저녁에 출금 (**수수료**)
def withdraw_night(balance,money):
    yangochi=100
    return yangochi, balance-money-yangochi

balance=0
balance=deposit(balance,1000)
yangochi,balance=withdraw_night(balance,1200)
print("수수료는 {0}원이며,. 잔액은 {1}원입니다.".format(yangochi,balance))
