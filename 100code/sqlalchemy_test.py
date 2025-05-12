from dynamic_models import Product, Customer

# Insert records
Product.create_table()  # Ensure the table is created
Customer.create_table()

# Insert records into the database
product1 = Product.insert_record(name="Laptop", price="1000")
product2 = Product.insert_record(name="Phone", price="500")

customer1 = Customer.insert_record(name="John Doe", email="john@example.com")
customer2 = Customer.insert_record(name="Jane Smith", email="jane@example.com")

print(f"Inserted Product: {product1.name}, {product1.price}")
print(f"Inserted Customer: {customer1.name}, {customer1.email}")