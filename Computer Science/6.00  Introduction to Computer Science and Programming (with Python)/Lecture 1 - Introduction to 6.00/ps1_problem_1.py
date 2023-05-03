# Paying the Minimum
# Problem 1
# Write a program to calculate the credit card balance after one year 
# if a person only pays the minimum monthly payment required by the credit card company each month


# TO DO
# >>>>>>>>> What if pay all in less than 12 months

def calculate_balance( outstanding_balance , annual_interest_rate , minimum_monthly_payment_rate ):
    
    # test data 
    # outstanding_balance = 4800
    # annual_interest_rate = .2
    # minimum_monthly_payment_rate = .02
    
    # this is the monthly interest rate
    mon_i_rate = annual_interest_rate / 12

    num_of_months = 12
    
    
    result = {
        'num_of_months': num_of_months,
        'month_calculations':[],
        'total_ammount_paid':0,
        'final_balance':0
        }
    
    
    # calculating for 12 months
    for month_num in range(1,num_of_months + 1 ):


        min_payment = round( minimum_monthly_payment_rate * outstanding_balance , 2)
        interests_paid = round( outstanding_balance * mon_i_rate, 2)
        principal_paid = round( min_payment - interests_paid , 2)
        
        outstanding_balance = round( outstanding_balance - principal_paid , 2)

        result['total_ammount_paid'] += min_payment

        result["month_calculations"].append({
            'month_number': month_num,
            'minimum_payment': min_payment,
            'principle_paid': principal_paid,
            'remaining_balance': outstanding_balance

        })

    result['final_balance'] = result["month_calculations"][-1]['remaining_balance']

    return result



def print_result(result):
    
    for month_num in range(0,result['num_of_months']):

        month_data = result['month_calculations'][month_num]
        
        print('------------------------------------------------------------')
        print(f'Month: { month_data["month_number"] }')
        print(f'Minimum monthly payment: ... ${ month_data["minimum_payment"] }')
        print(f'Principle paid: ............ ${ month_data["principle_paid"] }') 
        print(f'Remaining balance: ......... ${ month_data["remaining_balance"] }') 

    print('\nRESULT\n')
    print(f'Total amount paid: ${ result["total_ammount_paid"] }')
    print(f'Remaining balance: $${ result["final_balance"] }')
    print('------------------------------------------------------------')
    print('---------------------- end of values -----------------------')



def prompt_user(msg):
    
    while True:
        try:
            value = float(input(msg))
            return value
        except:
            print('Error: Please enter a decimal number')
        

def start_program():

    balance = prompt_user('Enter the outstanding balance on your credit card: ')
    i_rate = prompt_user('Enter the annual credit card interest rate as a decimal: ')
    min_payment = prompt_user('Enter the minimum monthly payment rate as a decimal: ')


    result = calculate_balance( balance , i_rate , min_payment )

    print_result(result)



def main():

    start_program()    


if __name__ == '__main__':
    main()