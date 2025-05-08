class Order:
    def __init__(self, order_id, items, customer):
        self.id = order_id
        self.items = items
        self.customer = customer


class OrderValidator:
    def validate(self, order: Order) -> None:
        print("Walidacja zamówienia.")


class OrderRepository:
    def save(self, order: Order) -> None:
        print("Zapisywanie zamówienia do bazy danych.")


class EmailSender:
    def send_confirmation(self, order: Order) -> None:
        print("Wysyłanie e-maila potwierdzającego.")


class OrderProcessor:
    def __init__(self, validator: OrderValidator, repository: OrderRepository, email_sender: EmailSender):
        self.validator = validator
        self.repository = repository
        self.email_sender = email_sender

    def process_order(self, order: Order) -> None:
        self.validator.validate(order)
        self.repository.save(order)
        self.email_sender.send_confirmation(order)


# Użycie
order = Order("123", ["Produkt A", "Produkt B"], "Jan Kowalski")
processor = OrderProcessor(
    validator=OrderValidator(),
    repository=OrderRepository(),
    email_sender=EmailSender()
)
processor.process_order(order)
