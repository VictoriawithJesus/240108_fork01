# -*- coding: utf-8 -*-
"""Copy of modulab_0108_함경표_김도현.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S7Lspo87Z_hh38mqy74hW5zj2s9BCYyg

# 계좌 만들기

Account 클래스 :
- 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. Account 클래스를 생성한 후 init 메서드를 구현해보세요.
- init메서드에서는 예금주와 초기 잔액만 입력 받습니다.
- 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
  (은행이름: SC은행, 계좌번호: 111-11-111111)

입금 메서드 : Account 클래스에 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.

출금 메서드 : Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.

정보 출력 메서드 : Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하세요. (예시 - 은행이름: SC은행, 예금주: 파이썬, 계좌번호: 111-11-111111, 잔고: 10,000원)

이자 지급하기 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 추가해보세요.

입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요. (입금 시간과 출력 시간을 기록해주세요.)

입금 내역과 출금 내역을 함께 출력하는 all_history 메서드를 추가하세요.

*루브릭 3 달성 조건 : 위에서 제시된 메서드를 제외한 나만의 신규 메서드를 추가해보세요.

all_history : 시간 순서대로 기록

루브릭 달성 조건

- 루브릭 1 평가문항 / 상세기준

클래스를 잘 생성했는가? / 클래스가 오류 없이 잘 작동하였음.



- 루브릭 2 평가문항 / 상세기준

제시된 문제를 기준치 이상 해결하였는가? / 주어진 문제 중 4개 이상이 작동하였음.



- 루브릭 3 평가문항 / 상세기준

추가로 제시된 문제를 해결했는가? / 새로운 시도를 통해 추가 메서드를 구현하였음.
"""

import random
import time
import datetime

def generate_random_accountnumber():                                           # 랜덤 계좌 번호 생성 함수
    #generat3 three sets of random numbers
    part1 = ''.join(random.choices('0123456789', k=3))
    part2 = ''.join(random.choices('0123456789', k=4))
    part3 = ''.join(random.choices('0123456789', k=4))

    # Combine the parts with hyphens
    result = f'{part1}-{part2}-{part3}'
    return result

class Account() :
    def __init__(self, person, balance, bank_name = 'SC_은행'):
        self.person = person
        self.account_number = generate_random_accountnumber() # 계좌 생성 시 랜덤 계좌 번호 생성 함수 호출
        self.balance = balance
        self.bank_name = bank_name
        self.count = 1                       # 계좌를 생성할 때 잔고 금액을 입력한 것을 첫번째 입금으로 가정
        self.history = {'deposit':[], 'withdraw': []}

    def deposit(self, deposit_money):                  # 입금 함수. 입금 금액 매개변수(deposit_money) 설정
        if deposit_money <= 1:
            print('Input Error, you must put at least 1 won.')
        else:
            self.balance += deposit_money
            self.count += 1
            self.interest_payment()          # 입금 횟수가 5가 될 때 이자 지급 함수 interest_payment() 실행
            d = datetime.datetime.now()                                  # 입금 시 현재 시각을 받아와 저장
            now_time = '.'.join([str(d.year), str(d.month), str(d.day)]) + ' ' + ':'.join([str(d.hour), str(d.minute), str(d.second)])
            self.write_history(now_time, deposit_money)


    def withdraw(self, withdraw_money):                # 출금 함수. 출금 금액 매개변수(withdraw_money) 설정
        if withdraw_money > self.balance:
            print('You cannot withdraw over your balance.')
        else:
            self.balance -= withdraw_money
            d = datetime.datetime.now()
            now_time = '.'.join([str(d.year), str(d.month), str(d.day)]) + ' ' + ':'.join([str(d.hour), str(d.minute), str(d.second)])
            self.write_history(now_time, withdraw_money, deposit= False) # 출금임을 구분하기 위해 deposit= False 설정

    def write_history(self, now_time, money, deposit = True):       # 입출금 시 시간과 금액을 기록하는 함수
        if deposit == True:
            self.history['deposit'].append((now_time, str(money), True))
        else:
            self.history['withdraw'].append((now_time, str(money), False))

    def interest_payment(self):                                                          # 이자 지급 함수
        original = self.balance
        if self.count % 5 == 0:
            self.balance += int(self.balance * 0.01)
            print("이자가 지급되었습니다. orginal balance : {} -> final balance : {}".format(original,self.balance))

    def display_info(self):                                                               # 정보 출력 함수
        str_balance = format(self.balance, ',')                         # 잔액을 천 단위에 따라 쉼표로 구분
        print("은행이름 : {}, 예금주 : {}, 계좌번호: {}, 잔고 : {}".format(self.bank_name, self.person, self.account_number, str_balance))


    def print_deposit_history(self):                                     # 입금 시간과 금액만 출력하는 함수
        for element in self.history['deposit']:
            print("입금 : {}, 입금금액 : {}".format(element[0],element[1]))

    def print_withdraw_history(self):                                    # 출금 시간과 금액만 출력하는 함수
        for element in self.history['withdraw']:
            print("출금 : {}, 출금금액 : {}".format(element[0],element[1]))

    def print_all_hisorty(self) :                # 기록된 모든 입출력 시간과 금액을 시간 순서에 따라 출력하는 함수

        all_list = []
        for x in self.history['deposit']:
            all_list.append(x)
        for y in self.history['withdraw'] :
            all_list.append(y)

        a = sorted(all_list, key=lambda x : x[0])
        for element in a :
            if element[2]:
                print("입금 : {}, 입금금액 : {}".format(element[0],element[1]))
            else:
                print("출금 : {}, 출금금액 : {}".format(element[0],element[1]))

a = Account('함경표', 1000) # 계좌생성, 예금주 이름과 초기 입금 금액
a.display_info()            # display_info(): 정보 출력 함수

a.deposit(1000) # 1000원 씩 입금 2번
a.deposit(1000)
time.sleep(2)   # 입출금 시간 차를 두기 위한 time.sleep() 함수

a.withdraw(500) # 500원 출금
time.sleep(2)

a.deposit(1000) # 1000원 입금
time.sleep(2)

a.withdraw(500) # 500원 출금
a.deposit(1000) # 1000원 입금. 잔액 4000원 + 5번째 입금으로 인한 1% 이자지금 -> 최종 잔액 4040원, 이자 지급 시 메세지 출력

print('\n', '---display info')
a.display_info()

print('---print deposit history')
a.print_deposit_history()           # 입금 기록과 금액을 출력

print('\n', '---print withdraw history')
a.print_withdraw_history()          # 출금 기록과 금액을 출력

print('\n', '---print all history')
a.print_all_hisorty()               # 모든 입출금 기록과 금액을 출력

a.deposit(0) # 1원 이상이 아닐경우 에러 반환
a.withdraw(100000) # 출금 액수가 통장 잔고보다 많을 경우, 에러 반환

"""# 회고

김도현 : 코드 작성을 혼자 했다면 절대 시간 내에 끝내지 못했을 것입니다. 뛰어난 동료분이 계셔서 같이 코드를 이해해 가며 필요한 부분은 구글링하여 문제를 해결할 수 있었습니다. 협업의 중요성과 그 위력을 느낄 수 있는 시간이었습니다.

함경표 : 시간이 생각보다 많이 부족하고, 아쉽게 마지막 문제를 해결하지 못하였다. 기획을 처음에 잘하고 했으면 조금 더 좋았을 것 같다.
"""