#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jan 03, 2020 9:47 AM
Filename: money2020.py
@author: Rabih Fawaz
@email: rf28@aub.edu.lb
"""

import os

MY_ACCOUNTS = {'Cancel': []}
DOLLAR_RATE = 1500
# accounts = ['Exit', 'Bank - NBK', 'BOB - Souyoula', 'Rabih Cash LL', 'Rabih Saving LL']
A_CURRENCIES = ['Cancel', 'LBP', 'USD', 'EUR']
A_TYPE = ['Cancel', 'Bank', 'Cash']
T_TYPE = ['Cancel', 'expense', 'income']
T_PAYEE = ['Cancel', 'Rabih Fawaz', 'Ramzi Fawaz']
T_EXPENSE_TYPE = ['Cancel']
T_MEMO = ['Cancel']
MAIN_MENU = ['Exit', 'Add New Account', 'Add Transaction', 'List Accounts']


class Account:
    def __init__(self, a_name, a_opening_balance=0.0, a_currency='LBP', a_type='Bank'):
        self.a_id = len(MY_ACCOUNTS)
        self.a_name = a_name
        self.a_type = a_type
        self.a_number = 'XXX'
        self.a_comment = ''
        self.a_fav = True
        self.a_opening_balance = a_opening_balance
        self.a_min_balance = 0.0
        self.a_balance = self.a_opening_balance
        self.a_currency = a_currency
        self.transactions = []

    def __str__(self):
        return '{:>3} | {:<20} | {:<3} | {:4} | {:>15,.2f} {:>3}'.format(self.a_id, self.a_name, self.a_number,
                                                                         self.a_type,
                                                                         float(self.a_balance),
                                                                         self.a_currency)

    def __eq__(self, other):
        other = Account(self.a_name, self.a_opening_balance, self.a_currency, self.a_type)
        other.a_id = self.a_id
        other.a_number = self.a_number
        other.a_comment = self.a_comment
        other.a_fav = self.a_fav
        other.a_min_balance = self.a_min_balance
        other.a_balance = self.a_balance
        other.transactions = self.transactions

    def Transaction(self, t_type, t_date, t_amount, t_payee, t_exp_type, t_memo):
        self.transactions.append([t_type, t_date, t_amount, t_payee, t_exp_type, t_memo])
        if t_type == 'expense':
            self.a_balance -= t_amount
        elif t_type == 'income':
            self.a_balance += t_amount


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def add_new_account():
    """
    Creates new account and updates the Dict MY_ACCOUNT

    :return: list of created Account
    :rtype: list
    """
    created_ok: bool = False
    a_name_ok: bool = False
    a_name: str = ''
    while not created_ok:
        try:
            while not a_name_ok:
                List = [key for key in MY_ACCOUNTS]
                print_title('Existing Accounts')
                list_enumerated(List, False)
                a_name = input('Enter new account name:')
                if a_name == '' or a_name == '0':
                    return
                elif a_name in List:
                    print('Account already exist.')
                    return
                else:
                    a_name_ok = True
            question: str = input('Account with default values? [Yes|No]')
            if question.lower() == 'yes' or question == '':
                # default values
                A: Account = Account(a_name)
                # update MY_ACCOUNT dict
                MY_ACCOUNTS[a_name] = [A]
            elif question.lower() == 'no':
                # non default values
                a_opening_balance: float = float(input('Enter opening balance:'))
                a_currency: str = select_val(A_CURRENCIES, 'CURRENCIES', 'currency')
                a_type: str = select_val(A_TYPE, 'ACCOUNT TYPE', 'type')
                A: Account = Account(a_name, a_opening_balance, a_currency, a_type)
                # update MY_ACCOUNT dict
                MY_ACCOUNTS[a_name] = [A]
            created_ok = True
            return MY_ACCOUNTS[a_name]
        except Exception as e:
            print('Error! Enter a valid account name.', e)
    return [A]


def add_account(A: Account) -> bool:
    """

    :param A:
    :type A:
    :return:
    :rtype:
    """
    # print(type(A))
    # print(A)
    # print(A.a_name)
    # print(type(MY_ACCOUNTS))
    # return True

    if A.a_name not in MY_ACCOUNTS:
        MY_ACCOUNTS[A.a_name] = [A]
        #     # MY_ACCOUNTS[T.a_name] = {'a_id': T.a_id,
        #     #                          'a_name': T.a_name,
        #     #                          'a_type': T.a_type,
        #     #                          'a_number': T.a_number,
        #     #                          'a_comment': T.a_comment,
        #     #                          'a_fav': T.a_fav,
        #     #                          'a_opening_balance': T.a_opening_balance,
        #     #                          'a_min_balance': T.a_min_balance,
        #     #                          'a_balance': T.a_balance,
        #     #                          'a_currency': T.a_currency}
        return True
    else:
        print('Error, Account [{}] already exists'.format(A.a_name))
        return False


def main_menu2():
    choice = ''
    while choice != 'Exit':
        choice = select_val(MAIN_MENU, 'MAIN MENU', 'a selection 0 to exit', True)
        print('choice:', choice)
        if choice == MAIN_MENU[1]:
            add_new_account()
        elif choice == MAIN_MENU[2]:
            # TODO: check this choice
            add_transaction_menu()
        elif choice == MAIN_MENU[3]:
            print('No of accounts:', list_accounts_menu())
        elif choice == MAIN_MENU[0]:
            return 0


"""
def main_menu():
    choice = -1
    while choice != 0:
        print('1 - Add Transaction')
        print('2 - List Accounts')
        print('0 - Exit')
        choice = int(input('Enter a choice, 0 to Exit:'))
        if choice == 1:
            add_transaction_menu()
        elif choice == 2:
            list_accounts_menu()
        elif choice == 0:
            return 0
"""


def list_accounts_menu():
    clear_screen()
    print_title('List Accounts')
    return print_account_list()


def add_transaction_menu():
    # TODO: check this function
    selected_list_no = [account for (index, account) in enumerate(MY_ACCOUNTS)]
    selected_account = select_val(selected_list_no, 'ACCOUNT LIST', 'Account no')
    # print('selected_account:', selected_account)
    if selected_account == 'Cancel':
        return
    elif selected_account not in MY_ACCOUNTS:
        print('New Account added {}'.format(selected_account))

        add_account(Account(selected_account))

    add_transaction(selected_account)


def print_title(TITLE):
    print(TITLE)
    print('-' * len(TITLE))


def main():
    # A: Account
    # add_account_list()
    # add_new_account()
    # print(MY_ACCOUNTS)
    # print_account_list()
    # main_menu()
    main_menu2()


def add_transaction(account):
    # TODO: check the inputs if empty and check for errors
    list_transactions(account)
    t_type = select_val(T_TYPE, 'New Transaction', 'Type of Transaction')

    t_date = input('Date               :')
    t_amount = int(input('Amount             :'))

    t_payee = select_val(T_PAYEE, 'PAYEES', 'Payee')
    t_exp_type = select_val(T_EXPENSE_TYPE, 'EXPENSES/INCOMES TYPES', 'Expense/Income Type')
    t_memo = select_val(T_MEMO, 'MEMO', 'Memo')
    MY_ACCOUNTS[account][0].Transaction(t_type, t_date, t_amount, t_payee, t_exp_type, t_memo)
    list_transactions(account)


def select_val(List, title, input_string, locked=False):
    selected_list_val = ''
    selected_ok = False
    selected_list_no = [index for (index, val) in enumerate(List)]
    print(selected_list_no)
    while not selected_ok:
        clear_screen()
        print_title(title)
        list_enumerated(List)
        selected_val = input('Enter ' + input_string + ': ')
        try:
            if selected_val == '':
                print('Invalid selection choose from list')
                print('or')
                print('Enter a new selection')
            elif int(selected_val) in selected_list_no:
                print(List[int(selected_val)])
                selected_list_val = List[int(selected_val)]
                selected_ok = True
            else:
                print('Invalid selection choose from list')
                print('or')
                print('Enter a new selection')
        except ValueError:
            if locked:
                print('Invalid selection choose from list')
                print('or')
                print('Enter a new selection')
            else:
                print('New selection added {}'.format(selected_val))
                List.append(selected_val)
                print(List)
                selected_list_val = selected_val
                selected_ok = True
    print(selected_list_val)
    return selected_list_val


def list_enumerated(List, enumerated=True):
    if len(List) == 1:
        print('Empty List')
    else:
        if enumerated:
            for index, val in enumerate(List):
                if index != 0:
                    print(index, '-', val)
        else:
            for index, val in enumerate(List):
                if index != 0:
                    print(val)
    print(0, '-', List[0])


def list_transactions(test_account):
    print('[', test_account, ']')
    print('-' * 18)
    print("{:^10} {:^15} {:<20} {:<20} {:<20}".format('Date', 'Amount', 'Payee', 'Type', 'Memo'))
    print('-' * 89)
    for t in MY_ACCOUNTS[test_account][0].transactions:
        print("{:>10} {:>15,.2f} {:<20} {:<20} {:<20}".format(t[1], t[2], t[3], t[4], t[5]))
    print('-' * 89)
    print('{:^67} | {:15,.2f} {}'.format('TOTAL AMOUNTS', MY_ACCOUNTS[test_account][0].a_balance, 'LBP'))


def add_account_list():
    # pass
    add_account(Account('Bank - NBK', 610966.8))
    # add_account(Account('BOB - Souyoula', 32463))
    # add_account(Account('Loan - BOB', -20800000))
    # add_account(Account('Bank - QH Leila', 595, 'USD'))
    # add_account(Account('Bank - QH Rabih', 740, 'USD'))
    # add_account(Account('Bank - QH Wafaa', 760, 'USD'))
    # add_account(Account('Loan - QH Leila', -900, 'USD'))
    # add_account(Account('Loan - QH Rabih', -1462, 'USD'))
    # add_account(Account('Loan - QH Wafaa', -1563, 'USD'))
    # add_account(Account('Loan Ramzi', 3459214, a_type='Cash'))
    # add_account(Account('Rabih Cash LL', 200000, a_type='Cash'))
    # add_account(Account('Rabih Saving LL', 1220000, a_type='Cash'))
    # add_account(Account('Rabih Saving Snack', 12000, a_type='Cash'))
    # add_account(Account('Rabih Cash USD', 321, a_currency='USD', a_type='Cash'))


def print_account_list() -> int:
    """
    Prints list of all accounts in MY_ACCOUNT

    :return: nb of accounts
    :rtype: int
    """
    if len(MY_ACCOUNTS) == 1:
        print('No Accounts available.')
    else:
        print('{:^3} | {:^20} | {:^3} | {:^4} | {:^15} {:^3}'.format('ID', 'Account Name', 'NO', 'Type', 'BALANCE',
                                                                     'CUR'))
        print('-' * 63)
        total_amounts = 0
        for key in MY_ACCOUNTS:
            if key != 'Cancel':
                print(MY_ACCOUNTS[key][0])
                if MY_ACCOUNTS[key][0].a_currency == 'USD':
                    total_amounts += MY_ACCOUNTS[key][0].a_balance * DOLLAR_RATE
                else:
                    total_amounts += MY_ACCOUNTS[key][0].a_balance
        print('-' * 63)
        print('{:^39} | {:15,.2f} {}'.format('TOTAL AMOUNTS', total_amounts, 'LBP'))
    return len(MY_ACCOUNTS) - 1


if __name__ == '__main__':
    main()
