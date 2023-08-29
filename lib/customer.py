class Customer:
    instances = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self._reviews = []
        Customer.instances.append(self)

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    def all(self):
        return Customer.instances

    def restaurants(self):
        unique_restaurants = set()
        for review in self._reviews:
            unique_restaurants.add(review.restaurant())
        return list(unique_restaurants)

    def num_reviews(self):
        return len(self._reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.instances:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, given_name):
        matching_customers = []
        for customer in cls.instances:
            if customer.given_name() == given_name:
                matching_customers.append(customer)
        return matching_customers
