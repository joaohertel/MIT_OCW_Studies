# Monthly interest rate = Annual interest rate / 12.0 Updated balance each month = Previous balance * (1 + Monthly interest rate) – Minimum
def calculate_month_by_month(outstanding_balance,mon_i_rate,min_payment):

    num_of_months = 0

    for _ in range(0, 12):

            interests_paid = outstanding_balance * mon_i_rate
            principal_paid = min_payment - interests_paid

            outstanding_balance = outstanding_balance - principal_paid

            num_of_months += 1

            if outstanding_balance <= 0:
                break
    
    interests_paid = round(interests_paid, 2)
    principal_paid = round(principal_paid, 2)

    outstanding_balance = round(outstanding_balance, 2)

    return (min_payment, num_of_months, outstanding_balance)

def calculate_min_payment(balance, annual_interest_rate):
    """Using the bisection method for faster results"""
    
    lower_bound = balance / 12.0 
    upper_bound = (balance * (1 + (annual_interest_rate / 12.0)) ** 12.0) / 12.0

    # this is the monthly interest rate
    mon_i_rate = annual_interest_rate / 12


    count = 0

    while True:

        count += 1
        # prevent infinite loop
        if count > 500: 
            break    

        outstanding_balance = balance

        guess = round(( upper_bound + lower_bound ) / 2 , 2) 
        # guess = ( upper_bound + lower_bound ) / 2 

        
        (min_payment, num_of_months, outstanding_balance) = calculate_month_by_month(outstanding_balance,mon_i_rate,guess)



        if outstanding_balance < 0:
            if upper_bound - lower_bound <= 0.03: # 0.03 is the tolerance
                break
            else:
                # guess was too big
                upper_bound = guess
        else:
            # guess was too small
            lower_bound = guess

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
