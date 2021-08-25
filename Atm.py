class Atm(object):
    def __init__(self,atmCardNo,pinNumber):
        self.atmCardNo=atmCardNo,
        self.pinNumber=pinNumber
        
    def cashWithdrawal(self):
        print('Enter The Amount Of Withdrawal:-4646') 
    def balanceInquiry(self):
        print('Type BAL space 16 digits A/C No" to 5607040:- ')
        
AtmClass=Atm('1473429876','4643')
print(AtmClass.cashWithdrawal())