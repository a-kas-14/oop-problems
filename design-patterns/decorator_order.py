from abc import ABC, abstractmethod


# 1. The interface: every order (plain or decorated) has these methods
class OrderComponent(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_base_price(self) -> float:
        pass


# 2. The basic order, with nothing added
class BaseOrder(OrderComponent):
    def __init__(self, base_price: float):
        self.base_price = base_price

    def get_cost(self) -> float:
        return self.base_price

    def get_description(self) -> str:
        return f"Base price: {self.base_price}€"

    def get_base_price(self) -> float:
        return self.base_price


# 3. Base decorator: holds an order and passes calls through to it
class OrderDecorator(OrderComponent):
    def __init__(self, order: OrderComponent):
        self._order = order

    def get_cost(self) -> float:
        return self._order.get_cost()

    def get_description(self) -> str:
        return self._order.get_description()

    def get_base_price(self) -> float:
        return self._order.get_base_price()


# 4. Concrete decorators: each adds ONE thing, then delegates the rest
class ExpressShippingDecorator(OrderDecorator):
    COST = 15.00

    def get_cost(self):
        return self._order.get_cost() + self.COST

    def get_description(self):
        return self._order.get_description() + f"\nExpress shipping: +{self.COST}€"


class InsuranceDecorator(OrderDecorator):
    RATE = 0.05  # 5% of the base price

    def _insurance(self):
        return self.get_base_price() * self.RATE

    def get_cost(self):
        return self._order.get_cost() + self._insurance()

    def get_description(self):
        return self._order.get_description() + f"\nInsurance (5%): +{self._insurance()}€"


class GiftWrapDecorator(OrderDecorator):
    COST = 5.00

    def get_cost(self):
        return self._order.get_cost() + self.COST

    def get_description(self):
        return self._order.get_description() + f"\nGift wrap: +{self.COST}€"


class DiscountDecorator(OrderDecorator):
    def __init__(self, order: OrderComponent, percent: float):
        super().__init__(order)
        self.percent = percent

    def _discount(self):
        return self._order.get_cost() * (self.percent / 100)

    def get_cost(self):
        return self._order.get_cost() - self._discount()

    def get_description(self):
        return self._order.get_description() + f"\nDiscount ({self.percent}%): -{self._discount()}€"


class PremiumMemberDecorator(OrderDecorator):
    RATE = 0.10  # 10%

    def _discount(self):
        return self._order.get_cost() * self.RATE

    def get_cost(self):
        return self._order.get_cost() - self._discount()

    def get_description(self):
        return self._order.get_description() + f"\nPremium member (10%): -{self._discount()}€"


if __name__ == "__main__":
    # Simple order
    order = BaseOrder(100.00)
    print(order.get_description())
    print(f"Total: {order.get_cost()}€")

    print("\n---\n")

    # Complex order - readable and flexible
    order = BaseOrder(100.00)
    order = ExpressShippingDecorator(order)
    order = InsuranceDecorator(order)
    order = GiftWrapDecorator(order)
    order = DiscountDecorator(order, percent=15)
    order = PremiumMemberDecorator(order)

    print(order.get_description())
    print(f"Total: {order.get_cost()}€")

    print("\n---\n")

    # The order of decorators is now visible and controllable
    a = DiscountDecorator(ExpressShippingDecorator(BaseOrder(100.00)), percent=15)
    b = ExpressShippingDecorator(DiscountDecorator(BaseOrder(100.00), percent=15))
    print(f"Discount after shipping:  {a.get_cost()}€")
    print(f"Discount before shipping: {b.get_cost()}€")
