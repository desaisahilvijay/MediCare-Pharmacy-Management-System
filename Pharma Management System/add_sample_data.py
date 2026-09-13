from app import app
from models import db, Medicine, Customer
from datetime import datetime, date

def add_sample_medicines():
    medicines = [
        {"name": "Paracetamol 500mg", "category": "Pain Relief", "price": 2.50, "stock": 100, "expiry_date": date(2025, 12, 31)},
        {"name": "Ibuprofen 400mg", "category": "Pain Relief", "price": 3.75, "stock": 80, "expiry_date": date(2025, 10, 15)},
        {"name": "Amoxicillin 250mg", "category": "Antibiotic", "price": 8.50, "stock": 50, "expiry_date": date(2025, 8, 20)},
        {"name": "Cetirizine 10mg", "category": "Antihistamine", "price": 4.25, "stock": 60, "expiry_date": date(2025, 11, 30)},
        {"name": "Omeprazole 20mg", "category": "Antacid", "price": 6.00, "stock": 40, "expiry_date": date(2025, 9, 10)},
        {"name": "Aspirin 75mg", "category": "Blood Thinner", "price": 1.80, "stock": 120, "expiry_date": date(2025, 7, 25)},
        {"name": "Metformin 500mg", "category": "Diabetes", "price": 5.50, "stock": 35, "expiry_date": date(2025, 6, 15)},
        {"name": "Lisinopril 10mg", "category": "Blood Pressure", "price": 7.25, "stock": 45, "expiry_date": date(2025, 12, 5)},
        {"name": "Simvastatin 20mg", "category": "Cholesterol", "price": 9.00, "stock": 30, "expiry_date": date(2025, 8, 30)},
        {"name": "Salbutamol Inhaler", "category": "Respiratory", "price": 12.50, "stock": 25, "expiry_date": date(2025, 10, 20)},
        {"name": "Loratadine 10mg", "category": "Antihistamine", "price": 3.50, "stock": 70, "expiry_date": date(2025, 11, 12)},
        {"name": "Diclofenac 50mg", "category": "Pain Relief", "price": 4.75, "stock": 55, "expiry_date": date(2025, 9, 8)},
        {"name": "Cough Syrup 100ml", "category": "Respiratory", "price": 6.75, "stock": 40, "expiry_date": date(2025, 7, 18)},
        {"name": "Vitamin D3 1000IU", "category": "Vitamin", "price": 8.25, "stock": 65, "expiry_date": date(2026, 1, 15)},
        {"name": "Calcium Tablets", "category": "Supplement", "price": 5.25, "stock": 50, "expiry_date": date(2025, 12, 20)}
    ]
    
    customers = [
        {"name": "John Smith", "phone": "555-0101", "email": "john.smith@email.com"},
        {"name": "Sarah Johnson", "phone": "555-0102", "email": "sarah.j@email.com"},
        {"name": "Mike Davis", "phone": "555-0103", "email": "mike.davis@email.com"},
        {"name": "Emily Brown", "phone": "555-0104", "email": "emily.brown@email.com"},
        {"name": "David Wilson", "phone": "555-0105", "email": "david.w@email.com"}
    ]
    
    with app.app_context():
        # Add medicines
        for med_data in medicines:
            existing = Medicine.query.filter_by(name=med_data["name"]).first()
            if not existing:
                medicine = Medicine(**med_data)
                db.session.add(medicine)
        
        # Add customers
        for cust_data in customers:
            existing = Customer.query.filter_by(phone=cust_data["phone"]).first()
            if not existing:
                customer = Customer(**cust_data)
                db.session.add(customer)
        
        db.session.commit()
        print("Sample data added successfully!")
        print(f"Total medicines: {Medicine.query.count()}")
        print(f"Total customers: {Customer.query.count()}")

if __name__ == "__main__":
    add_sample_medicines()