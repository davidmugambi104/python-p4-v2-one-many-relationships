import datetime
from app import app
from models import db, User, Category, Product, Customer, Sale, SaleItem, Inventory, Supplier, Payment

with app.app_context():
    # Delete all rows in tables (if needed, ensure proper order to avoid foreign key constraints)
    SaleItem.query.delete()
    Sale.query.delete()
    Inventory.query.delete()
    Product.query.delete()
    Category.query.delete()
    Customer.query.delete()
    User.query.delete()
    Supplier.query.delete()
    Payment.query.delete()
    
    # Create Users
    admin = User(username="admin", role="admin", email="admin@example.com")
    admin.set_password("securepassword")
    cashier = User(username="cashier1", role="cashier", email="cashier1@example.com")
    cashier.set_password("cashierpassword")
    db.session.add_all([admin, cashier])
    db.session.commit()

    # Create Categories
    electronics = Category(name="Electronics", description="Electronic gadgets and devices")
    groceries = Category(name="Groceries", description="Everyday grocery items")
    db.session.add_all([electronics, groceries])
    db.session.commit()

    # Create Products
    laptop = Product(
        name="Laptop",
        description="15-inch laptop with 8GB RAM",
        sku="ELEC001",
        price=800.00,
        cost_price=600.00,
        stock_quantity=10,
        category=electronics
    )
    apple = Product(
        name="Apple",
        description="Fresh red apple",
        sku="GROC001",
        price=0.50,
        cost_price=0.30,
        stock_quantity=200,
        category=groceries
    )
    db.session.add_all([laptop, apple])
    db.session.commit()

    # Create Customers
    john_doe = Customer(name="John Doe", email="johndoe@example.com", phone="1234567890", address="123 Main Street")
    jane_smith = Customer(name="Jane Smith", email="janesmith@example.com", phone="0987654321", address="456 Elm Street")
    db.session.add_all([john_doe, jane_smith])
    db.session.commit()

    # Create Sales and Sale Items
    sale1 = Sale(user=admin, customer=john_doe, total_amount=1600.00, payment_method="card")
    sale_item1 = SaleItem(sale=sale1, product=laptop, quantity=2, price=800.00)
    sale2 = Sale(user=cashier, customer=jane_smith, total_amount=5.00, payment_method="cash")
    sale_item2 = SaleItem(sale=sale2, product=apple, quantity=10, price=0.50)
    db.session.add_all([sale1, sale_item1, sale2, sale_item2])
    db.session.commit()

    # Create Inventory Changes
    inventory_change1 = Inventory(product=laptop, change_quantity=-2, reason="Sold", user=admin)
    inventory_change2 = Inventory(product=apple, change_quantity=-10, reason="Sold", user=cashier)
    db.session.add_all([inventory_change1, inventory_change2])
    db.session.commit()

    # Create Suppliers
    supplier1 = Supplier(name="Tech Distributors", contact_person="Alice", phone="1122334455", email="tech@example.com", address="789 Tech Street")
    supplier2 = Supplier(name="Fresh Farms", contact_person="Bob", phone="9988776655", email="fresh@example.com", address="321 Orchard Lane")
    db.session.add_all([supplier1, supplier2])
    db.session.commit()

    # Create Payments
    payment1 = Payment(sale=sale1, amount=1600.00, payment_method="card", transaction_reference="TRX12345")
    payment2 = Payment(sale=sale2, amount=5.00, payment_method="cash")
    db.session.add_all([payment1, payment2])
    db.session.commit()

    print("Database seeded successfully!")
