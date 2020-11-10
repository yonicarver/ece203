def currency( money ):
    "input currency, return value with $ to 2 decimal places"
    
    print '$%.2f' % (money)
    
    return;

money = float(raw_input())

currency(money)
