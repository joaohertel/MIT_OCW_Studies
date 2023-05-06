# Monthly interest rate = Annual interest rate / 12.0 Updated balance each month = Previous balance * (1 + Monthly interest rate) – Minimum
def calculate_min_payment(balance, annual_interest_rate):

    # this is the monthly interest rate
    mon_i_rate = annual_interest_rate / 12

    num_of_months = 0
    
    # Initial guess
    min_payment = 10

    while True:
        
        outstanding_balance = balance

        for _ in range(0, 12):

            interests_paid = round(outstanding_balance * mon_i_rate, 2)
            principal_paid = round(min_payment - interests_paid, 2)

            outstanding_balance = round(outstanding_balance - principal_paid, 2)

            num_of_months += 1

            if outstanding_balance <= 0:
                break
        
        if outstanding_balance > 0:
            min_payment += 10
            num_of_months = 0
        else:
            break

    result = {
        'min_payment': min_payment,
        'num_of_months': num_of_months,
        'final_balance': outstanding_balance
    }


    return result


def print_result(result):

    print('\nRESULT\n')
    print(f'Monthly payment to pay off debt in 1 year: ${ result["min_payment"] }')
    print(f'Number of months needed: { result["num_of_months"] }')
    print(f'Balance: { result["final_balance"] }')
    print('------------------------------------------------------------')
    

def prompt_user(msg):

    while True:
        try:
            value = float(input(msg))
            return value
        except:
            print('Error: Please enter a decimal number')


def start_program():

    balance = prompt_user(
        'Enter the outstanding balance on your credit card: ')
    i_rate = prompt_user(
        'Enter the annual credit card interest rate as a decimal: ')

    result = calculate_min_payment(balance, i_rate)

    # print(result)
    print_result(result)


def main():

    start_program()


if __name__ == '__main__':
    main()
