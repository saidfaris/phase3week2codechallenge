from review import Review  

class Restaurant:
    instances = []

    def __init__(self, name):
        self._name = name
        self._reviews = []
        Restaurant.instances.append(self)

    def name(self):
        return self._name

    def reviews(self):
        return self._reviews

    def customers(self):
        unique_customers = set()
        for review in self._reviews:
            unique_customers.add(review.customer())
        return list(unique_customers)

    def add_review(self, customer, rating):
        review = Review(customer, self, rating)  
        self._reviews.append(review)
