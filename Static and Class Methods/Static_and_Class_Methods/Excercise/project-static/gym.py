class Gym:
    def __init__(self):
        self.customers = list()
        self.trainers = list()
        self.equipment = list()
        self.plans = list()
        self.subscriptions = list()

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = [x for x in self.subscriptions if x.id == subscription_id][0]
        customer = [x for x in self.customers if subscription.customer_id == x.id][0]
        trainer = [x for x in self.trainers if subscription.trainer_id == x.id][0]
        plan = [x for x in self.plans if subscription.exercise_id == x.id][0]
        equipment = [x for x in self.equipment if plan.equipment_id == x.id][0]
        result = [subscription, customer, trainer,equipment, plan]
        return '\n'.join([x.__repr__() for x in result])
