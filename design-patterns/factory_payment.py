from abc import ABC, abstractmethod


# 1. The interface: every processor "promises" to have these two methods
class PaymentProcessor(ABC):
    @abstractmethod
    def validate(self, details: dict) -> bool:
        pass

    @abstractmethod
    def process(self, amount: float, details: dict) -> dict:
        pass


# 2. Concrete implementations: each class holds its own logic
class CreditCardProcessor(PaymentProcessor):
    FEE_RATE = 0.029  # 2.9%

    def validate(self, details: dict) -> bool:
        card_number = details.get("card_number")
        cvv = details.get("cvv")
        return bool(card_number) and len(card_number) == 16 and bool(cvv) and len(cvv) == 3

    def process(self, amount: float, details: dict) -> dict:
        if not self.validate(details):
            return {"success": False, "error": "Invalid card number or CVV"}
        fee = round(amount * self.FEE_RATE, 2)
        return {"success": True, "method": "credit_card", "amount": round(amount + fee, 2), "fee": fee}


class BankTransferProcessor(PaymentProcessor):
    FLAT_FEE = 1.50

    def validate(self, details: dict) -> bool:
        iban = details.get("iban")
        return bool(iban) and len(iban) >= 15

    def process(self, amount: float, details: dict) -> dict:
        if not self.validate(details):
            return {"success": False, "error": "Invalid IBAN"}
        fee = self.FLAT_FEE
        return {"success": True, "method": "bank_transfer", "amount": round(amount + fee, 2), "fee": fee}


class PayPalProcessor(PaymentProcessor):
    FEE_RATE = 0.034   # 3.4%
    FIXED_FEE = 0.30   # + 0.30€

    def validate(self, details: dict) -> bool:
        email = details.get("email")
        return bool(email) and "@" in email

    def process(self, amount: float, details: dict) -> dict:
        if not self.validate(details):
            return {"success": False, "error": "Invalid PayPal email"}
        fee = round(amount * self.FEE_RATE + self.FIXED_FEE, 2)
        return {"success": True, "method": "paypal", "amount": round(amount + fee, 2), "fee": fee}


# 3. The factory: maps a string to the right class (no if/elif chain)
class PaymentFactory:
    _processors = {
        "credit_card": CreditCardProcessor,
        "bank_transfer": BankTransferProcessor,
        "paypal": PayPalProcessor,
    }

    def get_processor(self, payment_type: str) -> PaymentProcessor:
        processor_class = self._processors.get(payment_type)
        if processor_class is None:
            raise ValueError(f"Unknown payment type: {payment_type}")
        return processor_class()

    # Add a new payment method without touching existing code
    @classmethod
    def register(cls, payment_type: str, processor_class):
        cls._processors[payment_type] = processor_class


if __name__ == "__main__":
    factory = PaymentFactory()

    processor = factory.get_processor("credit_card")
    print(processor.process(100.0, {"card_number": "1234567890123456", "cvv": "123"}))

    processor = factory.get_processor("bank_transfer")
    print(processor.process(100.0, {"iban": "FR7630006000011234567890189", "bic": "BNPAFRPP"}))

    processor = factory.get_processor("paypal")
    print(processor.process(100.0, {"email": "amina@example.com"}))

    # Invalid card
    processor = factory.get_processor("credit_card")
    print(processor.process(100.0, {"card_number": "123", "cvv": "123"}))

    # Unknown type
    try:
        factory.get_processor("crypto")
    except ValueError as e:
        print("Error:", e)
