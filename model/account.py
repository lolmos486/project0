class Account:
    def __init__(self, t_id, description, completed, customer_id):
        self.id = t_id
        self.description = description
        self.completed = completed
        self.customer_id = customer_id

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "customer_id": self.customer_id
        }