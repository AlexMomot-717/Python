# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
# оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных. Подсказка: постарайтесь по возможности реализовать
# в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from abc import abstractmethod, ABC


class OfficeEquipmentWarehouse:

    @staticmethod
    def in_store(pos_data):
        while True:
            try:
                quantity_in = int(input(f'Enter incoming quantity of {pos_data["good name"]}: '))
            except (ValueError, NameError, TypeError) as err:
                print(f'Attention! {err}!')
            else:
                pos_data['quantity'] = pos_data.__getitem__('quantity') + quantity_in
                return pos_data

    @staticmethod
    def out_store(pos_data):
        department = input(f'Enter a name of department where {pos_data["good name"]} to transfer to: ')
        while True:
            try:
                quantity_out = int(input(f'Enter quantity for transfer to {department} department: '))
            except (ValueError, NameError, TypeError) as err:
                print(f'Attention! {err}!')
            else:
                pos_data['quantity'] = pos_data.__getitem__('quantity') - quantity_out
                print(f'{quantity_out} units are transferred to {department} department')
                return pos_data


class OfficeEquipment:

    def __init__(self):
        self.pos_data = []
        self.pos_card = {}

    @property
    def get_card_filled(self):
        name = input(f'enter {self.subclass} name: ').capitalize()
        self.pos_data.append(name)
        mode = input('enter mode: ')
        self.pos_data.append(mode)
        unit = input('enter measurement unit: ')
        self.pos_data.append(unit)
        while True:
            try:
                quantity = int(input('enter quantity: '))
            except (ValueError, NameError, TypeError) as err:
                print(f'Attention! {err}!')
            else:
                self.pos_data.append(quantity)
                break
        while True:
            try:
                price = int(input('enter price: '))
            except (ValueError, NameError, TypeError) as err:
                print(f'Attention! {err}!')
            else:
                self.pos_data.append(price)
                return self.pos_data

    @abstractmethod
    def __str__(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self):
        super(Printer, self).__init__()
        self.subclass = 'Printer'

    @property
    def get_card_filled(self):
        super(Printer, self).get_card_filled
        card_form = ['subclass', 'good name', 'mode', 'measurement unit', 'quantity', 'price']
        subclass = self.subclass
        self.pos_data.insert(0, subclass)
        card_form.append('color')
        is_color = input('is it color? Yes/No: ')
        self.pos_data.append('multicolor' if is_color.lower() == 'yes' else 'mono')
        self.pos_card = dict(zip(card_form, self.pos_data))
        return self.pos_card

    def __str__(self):
        print('\n' + f'*** Position "{self.pos_card["good name"]}" card***')
        for c, d in self.pos_card.items():
            print(f'{c}: {d}')
        return f'***End of card***'

    def let_print_go(self, name, is_on, start):
        if is_on == True and start == 1:
            return f'just wait! {name} is printing'
        elif is_on == False and start == 0:
            return f'for printing turn on {name} and start'
        elif is_on == True and start == 0:
            return f'{name} is ready'
        else:
            return f'no answer. {name} is off'


class Scanner(OfficeEquipment):
    def __init__(self):
        super(Scanner, self).__init__()
        self.subclass = 'Scanner'

    @property
    def get_card_filled(self):
        super(Scanner, self).get_card_filled
        card_form = ['subclass', 'good name', 'mode', 'measurement unit', 'quantity', 'price']
        subclass = self.subclass
        self.pos_data.insert(0, subclass)
        card_form.append('image resolution')
        image_resolution = input('enter image resolution: ')
        self.pos_data.append(image_resolution)
        self.pos_card = dict(zip(card_form, self.pos_data))
        return self.pos_card

    def __str__(self):
        print('\n' + f'***Position "{self.pos_card["good name"]}" card***')
        for c, d in self.pos_card.items():
            print(f'{c}: {d}')
        return f'***End of card***'

    def let_do_scan(self, name, pc_id, start):
        if start == 1:
            return f'{name} sent scan on PC {pc_id}'
        else:
            return f'{name} is off work'


class Xerox(OfficeEquipment):
    def __init__(self):
        super(Xerox, self).__init__()
        self.subclass = 'Xerox'

    @property
    def get_card_filled(self):
        super(Xerox, self).get_card_filled
        card_form = ['subclass', 'good name', 'mode', 'measurement unit', 'quantity', 'price']
        subclass = self.subclass
        self.pos_data.insert(0, subclass)
        card_form.append('copy speed')
        copy_speed = input('enter copy speed, copies in minutes: ')
        self.pos_data.append(copy_speed)
        self.pos_card = dict(zip(card_form, self.pos_data))
        return self.pos_card

    def __str__(self):
        print('\n' + f'***Position "{self.pos_card["good name"]}" card***')
        for c, d in self.pos_card.items():
            print(f'{c}: {d}')
        return f'***End of card***'

    @classmethod
    def service_notice(cls):
        return f'technical service must be done every 2 months'




pos1 = Printer()
pos1_card = pos1.get_card_filled
print(type(pos1_card))
print(pos1_card)
print(pos1, '\n')
store_card1 = pos1_card
store_card1 = OfficeEquipmentWarehouse().in_store(store_card1)
print(store_card1)
store_card1 = OfficeEquipmentWarehouse().out_store(store_card1)
print(store_card1)
print(pos1.let_print_go(pos1_card['good name'], True, 1))
print('---------')

pos2 = Scanner()
pos2_card = pos2.get_card_filled
print(pos2_card)
print(pos2, '\n')
store_card2 = pos2_card
store_card2 = OfficeEquipmentWarehouse().in_store(store_card2)
print(store_card2)
store_card2 = OfficeEquipmentWarehouse().out_store(store_card2)
print(store_card2)
print(Scanner().let_do_scan(pos2_card['good name'], '12478', 1))
print('---------')

pos3 = Xerox()
pos3_card = pos3.get_card_filled
print(pos3_card)
print(pos3, '\n')
store_card3 = pos3_card
store_card3 = OfficeEquipmentWarehouse().in_store(store_card3)
print(store_card3)
store_card3 = OfficeEquipmentWarehouse().out_store(store_card3)
print(store_card3)
print(Xerox().service_notice())
print('---------')
