
class Customer:
    def __init__(self, id, customer_name, active):
        self.id = id
        self.customer_name = customer_name
        self.active = active

    def to_dict(self):
        return {
            "id": self.id,
            "customer_name": self.customer_name,
            "active": self.active
        }
