class Atm:
    def __init__(atm, CashWithdrawl, BalanceEnquiry ):
        atm.CashWithdrawl = CashWithdrawl
        atm.BalanceEnquiry = BalanceEnquiry

    def function(atm):
        print(atm.CashWithdrawl, atm.BalanceEnquiry)


cardNo = input("enter your card number: ")
pinNo = input("enter your pin number: ")

function()
