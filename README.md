# phase3week2codechallenge
# Object Relations Code Challenge - Restaurants

Welcome to the Object Relations Code Challenge for a Yelp-style domain. In this challenge, we will be working with three models: `Restaurant`, `Customer`, and `Review`. The relationships between these models are as follows:
- A `Restaurant` has many `Reviews`.
- A `Customer` has many `Reviews`.
- A `Review` belongs to both a `Customer` and a `Restaurant`.

Additionally, there's a many-to-many relationship between `Restaurant` and `Customer`.

## Project Structure
Before diving into the code, it's essential to have a clear understanding of the domain. Consider sketching the relationships and interactions on paper or a whiteboard.

## Installation
To get started, make sure you have the required dependencies installed using the provided Pipfile. If you're using Pipenv, you can run:

```bash
pipenv install
```

## Initializers, Readers, and Writers

### Customer
- `Customer __init__(self, name, family_name)`
  - Initializes a customer with a given name and family name.
- `Customer given_name(self)`
  - Returns the customer's given name.
- `Customer family_name(self)`
  - Returns the customer's family name.
- `Customer full_name(self)`
  - Returns the full name of the customer in Western style.
- `Customer all(cls)`
  - Returns all customer instances.

### Restaurant
- `Restaurant __init__(self, name)`
  - Initializes a restaurant with a given name.
- `Restaurant name(self)`
  - Returns the restaurant's name (immutable).

### Review
- `Review __init__(self, customer, restaurant, rating)`
  - Initializes a review with a customer, restaurant, and a rating.
- `Review rating(self)`
  - Returns the rating for a review.
- `Review all(cls)`
  - Returns all reviews.

## Object Relationship Methods

### Review
- `Review customer(self)`
  - Returns the customer object associated with the review.
- `Review restaurant(self)`
  - Returns the restaurant object associated with the review.

### Restaurant
- `Restaurant reviews(self)`
  - Returns a list of all reviews for that restaurant.
- `Restaurant customers(self)`
  - Returns a unique list of all customers who have reviewed the restaurant.

### Customer
- `Customer restaurants(self)`
  - Returns a unique list of all restaurants a customer has reviewed.
- `Customer add_review(self, restaurant, rating)`
  - Creates a new review associated with the customer and restaurant.

## Aggregate and Association Methods

### Customer
- `Customer num_reviews(self)`
  - Returns the total number of reviews authored by a customer.
- `Customer find_by_name(cls, name)`
  - Returns the first customer whose full name matches the given name.
- `Customer find_all_by_given_name(cls, name)`
  - Returns a list of customers with the given name.

### Restaurant
- `Restaurant average_star_rating(self)`
  - Returns the average star rating for a restaurant based on its reviews.

## Usage
To use this code, create instances of `Customer`, `Restaurant`, and `Review`, and interact with them as needed. Ensure that you test your code in the console to verify its correctness.

## Project Submission
1. Create a new project folder.
2. Create a new private GitHub repository.
3. Add your TM (Technical Mentor) as a contributor for grading purposes.
4. Regularly commit your code to the repository.

## Rubric
- Folder Structure (5 points)
- Initializers and Methods (15 points)
- Object Relationship Methods (3 points)
- Method Usage and Correctness (2 points)

Please prioritize writing methods that work over writing more methods that don't work. Writing error-free code is essential.

Remember, the focus should be on functionality, and you can refactor for best practices after achieving a working solution.

## Good Luck!
Best of luck with your Object Relations Code Challenge for Restaurants. Feel free to reach out if you have any questions or need further assistance. Happy coding!
