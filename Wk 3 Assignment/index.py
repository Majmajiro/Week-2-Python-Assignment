def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price

# Try it out 
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Let's calculate the final price using the function
    final_price = calculate_discount(price, discount_percent)

    if final_price < price:
        print(f"Discount applied! Final price: KES {final_price:.2f}")
    else:
        print(f"No discount applied. Final price remains: KES {price:.2f}")
except ValueError:
    print("Please enter valid numbers for price and discount.")

