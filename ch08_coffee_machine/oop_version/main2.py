from menu import Menu  # *를 안 써도 됨. Menu객체를 생성하면 MenuItem객체는 자동으로 생성되니깐.
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input(f'어떤 음료를 드시겠습니까? ({menu.get_items()}) >>> ')
    if choice == 'off':
        is_on = False
        print(f'자판기가 종료되었습니다. 🫥')
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink == None:  # choice에 오타가 있을 경우 None이 반환되기 때문에 고전적 예외 처리
            continue  # continue가 실행되면 이 이하의 코드라인은 실행되지 않고,
            # while 반복문의 가장 앞 부분으로 돌아가서 다음 반복이 실행됨.
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                # 이거 왜 drink임? ㅇㅋ 알았음

