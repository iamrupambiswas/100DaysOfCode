from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    
    @abstractmethod
    def make_payment(self, amount):
        pass
    
    def payment_processed(self, amount):
        print(f"Payment of rupees {amount} was processed!")
        
class PayPal(PaymentSystem):
    def make_payment(self, amount):
        self.payment_processed(amount)
        
class CreditCard(PaymentSystem):
    def make_payment(self, amount):
        print(f"Payment of credit card {amount} was processed!")
        
pay1 = PayPal()
pay1.make_payment(100000)

pay2 = CreditCard()
pay2.make_payment(50000)