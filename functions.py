# Question 1: Applies discount based on the percentage
# If the discount is 20% or more, it calculates the final price after discount.

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Question 2: Using the calculate_discount function  in question 1,
# it prompts the user for original price and discount percentage
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))
final_price = calculate_discount(original_price, discount_percentage)


if discount_percentage >= 20:
    print(f"The final price after a {discount_percentage}% discount is: {final_price}")
else:
    print(f"No discount applied. The price remains: {original_price}")

