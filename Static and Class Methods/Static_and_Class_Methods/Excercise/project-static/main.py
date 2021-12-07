from project_wild_farm.customer import Customer
from project_wild_farm.equipment import Equipment
from project_wild_farm.exercise_plan import ExercisePlan
from project_wild_farm.gym import Gym
from project_wild_farm.subscription import Subscription
from project_wild_farm.trainer import Trainer

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))
