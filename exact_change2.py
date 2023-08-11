def exact_change(user_total):
    
    # values of each denomination
    dollar_val = 100
    quarter_val = 25
    dime_val = 10
    nickel_val = 5
    penny_val = 1
    
    # remaining_coins tracks how much money we have to make change for
    remaining_coins = user_total
    
    # Each block of if statements checks for the coin denominations and performs
    # the required arithmetic and deducting it from the remaining_coins.

    if remaining_coins >= dollar_val:
        dollars = remaining_coins // dollar_val
        remaining_coins -= dollars * dollar_val
    else:
        dollars = 0
        

    if remaining_coins >= quarter_val:
        quarters = remaining_coins // quarter_val
        remaining_coins -= quarters * quarter_val
    else:
        quarters = 0

    if remaining_coins >= dime_val:
        dimes = remaining_coins // dime_val
        remaining_coins -= dimes * dime_val
    else:
        dimes = 0

    if remaining_coins >= nickel_val:
        nickels = remaining_coins // nickel_val
        remaining_coins -= nickels * nickel_val
    else:
        nickels = 0


    if remaining_coins >= penny_val:
        pennies = remaining_coins // penny_val
        remaining_coins -= pennies * penny_val
    else:
        pennies = 0

    return dollars, quarters, dimes, nickels, pennies


        

if __name__ == '__main__': 
    input_val = int(input())
    
        # checking for edge cases of 0 or negative money
    if input_val <= 0:
        print('no change')
    
    else:
        num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

        # each block checks for whether there exists any amount of the coin, then
        # the plurality of the denomination and outputs the grammatically correct
        # response.
        if num_dollars == 1:
            print(f'{num_dollars} dollar')
        elif num_dollars > 1:
            print(f'{num_dollars} dollars')
        else:
            pass
        
        if num_quarters == 1:
            print(f'{num_quarters} quarter')
        elif num_quarters > 1:
            print(f'{num_quarters} quarters')
        else:
            pass

        if num_dimes == 1:
            print(f'{num_dimes} dime')
        elif num_dimes > 1:
            print(f'{num_dimes} dimes')
        else:
            pass

        # Point of interest: that there is no check for a plurality of
        # nickels. Discovered that you only ever need 1 nickel
        # as 2 nickels == 1 dime.
        if num_nickels == 1:
            print(f'{num_nickels} nickel')
        else:
            pass

        if num_pennies == 1:
            print(f'{num_pennies} penny')
        elif num_pennies > 1:
            print(f'{num_pennies} pennies')
        else:
            pass