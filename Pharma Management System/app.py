from flask import Flask, render_template, request, redirect, url_for, jsonify, session, send_file
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, Medicine, Customer, Sale, SaleItem, User
from datetime import datetime
import qrcode
import io
import base64
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your-secret-key'

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def dashboard():
    total_medicines = Medicine.query.count()
    total_customers = Customer.query.count()
    low_stock = Medicine.query.filter(Medicine.stock < 10).count()
    return render_template('dashboard.html', 
                         total_medicines=total_medicines,
                         total_customers=total_customers,
                         low_stock=low_stock)

@app.route('/inventory')
def inventory():
    medicines = Medicine.query.all()
    return render_template('inventory.html', medicines=medicines)

@app.route('/add_medicine', methods=['POST'])
def add_medicine():
    medicine = Medicine(
        name=request.form['name'],
        category=request.form['category'],
        price=float(request.form['price']),
        stock=int(request.form['stock']),
        expiry_date=datetime.strptime(request.form['expiry_date'], '%Y-%m-%d').date()
    )
    db.session.add(medicine)
    db.session.commit()
    return redirect(url_for('inventory'))

@app.route('/sales')
def sales():
    customers = Customer.query.all()
    medicines = Medicine.query.all()
    return render_template('sales.html', customers=customers, medicines=medicines)

@app.route('/process_sale', methods=['POST'])
def process_sale():
    customer_type = request.form.get('customer_type', 'existing')
    
    if customer_type == 'new':
        # Create new customer
        new_customer = Customer(
            name=request.form['new_customer_name'],
            phone=request.form['new_customer_phone'],
            email=request.form.get('new_customer_email', '')
        )
        db.session.add(new_customer)
        db.session.flush()
        customer_id = new_customer.id
    else:
        customer_id = request.form['customer_id']
    
    medicine_id = request.form['medicine_id']
    quantity = int(request.form['quantity'])
    
    medicine = Medicine.query.get(medicine_id)
    total = medicine.price * quantity
    
    sale = Sale(customer_id=customer_id, total_amount=total)
    db.session.add(sale)
    db.session.flush()
    
    sale_item = SaleItem(
        sale_id=sale.id,
        medicine_id=medicine_id,
        quantity=quantity,
        unit_price=medicine.price
    )
    db.session.add(sale_item)
    
    medicine.stock -= quantity
    db.session.commit()
    
    return redirect(url_for('generate_bill', sale_id=sale.id))

@app.route('/bill/<int:sale_id>')
def generate_bill(sale_id):
    sale = Sale.query.get_or_404(sale_id)
    customer = Customer.query.get(sale.customer_id)
    sale_items = db.session.query(SaleItem, Medicine).join(Medicine).filter(SaleItem.sale_id == sale_id).all()
    
    # Generate QR code
    qr_data = f"Bill #{sale.id}\nCustomer: {customer.name}\nAmount: ${sale.total_amount:.2f}\nDate: {sale.date.strftime('%d/%m/%Y %H:%M')}"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white")
    img_buffer = io.BytesIO()
    qr_img.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    qr_code_b64 = base64.b64encode(img_buffer.getvalue()).decode()
    
    return render_template('bill.html', sale=sale, customer=customer, sale_items=sale_items, qr_code=qr_code_b64)

@app.route('/sales_history')
def sales_history():
    sales = db.session.query(Sale, Customer).join(Customer).order_by(Sale.date.desc()).all()
    return render_template('sales_history.html', sales=sales)

@app.route('/customers')
def customers():
    customers = Customer.query.all()
    return render_template('customers.html', customers=customers)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    customer = Customer(
        name=request.form['name'],
        phone=request.form['phone'],
        email=request.form.get('email', '')
    )
    db.session.add(customer)
    db.session.commit()
    return redirect(url_for('customers'))

# Admin Panel Routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('dashboard'))

@app.route('/admin')
@login_required
def admin_dashboard():
    total_sales = Sale.query.count()
    total_revenue = db.session.query(db.func.sum(Sale.total_amount)).scalar() or 0
    recent_sales = db.session.query(Sale, Customer).join(Customer).order_by(Sale.date.desc()).limit(5).all()
    
    return render_template('admin_dashboard.html', 
                         total_sales=total_sales,
                         total_revenue=total_revenue,
                         recent_sales=recent_sales)

@app.route('/admin/medicines')
@login_required
def admin_medicines():
    medicines = Medicine.query.all()
    return render_template('admin_medicines.html', medicines=medicines)

@app.route('/admin/edit_medicine/<int:medicine_id>', methods=['GET', 'POST'])
@login_required
def edit_medicine(medicine_id):
    medicine = Medicine.query.get_or_404(medicine_id)
    
    if request.method == 'POST':
        medicine.name = request.form['name']
        medicine.category = request.form['category']
        medicine.price = float(request.form['price'])
        medicine.stock = int(request.form['stock'])
        medicine.expiry_date = datetime.strptime(request.form['expiry_date'], '%Y-%m-%d').date()
        db.session.commit()
        return redirect(url_for('admin_medicines'))
    
    return render_template('edit_medicine.html', medicine=medicine)

@app.route('/admin/delete_medicine/<int:medicine_id>')
@login_required
def delete_medicine(medicine_id):
    medicine = Medicine.query.get_or_404(medicine_id)
    db.session.delete(medicine)
    db.session.commit()
    return redirect(url_for('admin_medicines'))

@app.route('/admin/create_user', methods=['GET', 'POST'])
@login_required
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return render_template('create_user.html', error='Username already exists')
        
        new_user = User(
            username=username,
            password=generate_password_hash(password),
            role='admin'
        )
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('admin_dashboard'))
    
    return render_template('create_user.html')

@app.route('/admin/users')
@login_required
def admin_users():
    users = User.query.all()
    return render_template('admin_users.html', users=users)

@app.route('/download_bill/<int:sale_id>')
def download_bill(sale_id):
    sale = Sale.query.get_or_404(sale_id)
    customer = Customer.query.get(sale.customer_id)
    
    # Create bill content for download
    bill_content = f"""MEDICARE PHARMACY
123 Health Street, Medical City
Phone: (555) 123-4567

{'='*40}
BILL #{sale.id}
{'='*40}

Customer: {customer.name}
Phone: {customer.phone}
Date: {sale.date.strftime('%d/%m/%Y %H:%M')}

{'='*40}
ITEMS:
{'='*40}
"""
    
    sale_items = db.session.query(SaleItem, Medicine).join(Medicine).filter(SaleItem.sale_id == sale_id).all()
    for sale_item, medicine in sale_items:
        bill_content += f"{medicine.name:<20} {sale_item.quantity:>3} x ${sale_item.unit_price:>6.2f} = ${sale_item.quantity * sale_item.unit_price:>8.2f}\n"
    
    bill_content += f"\n{'='*40}\nTOTAL: ${sale.total_amount:.2f}\n{'='*40}\n\nThank you for choosing MediCare Pharmacy!"
    
    # Create file-like object
    bill_file = io.StringIO(bill_content)
    bill_bytes = io.BytesIO(bill_content.encode('utf-8'))
    
    return send_file(bill_bytes, as_attachment=True, download_name=f'bill_{sale.id}.txt', mimetype='text/plain')

def create_admin_user():
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(
            username='admin',
            password=generate_password_hash('admin123'),
            role='admin'
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin user created: username=admin, password=admin123")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_admin_user()
    app.run(debug=True, port=5001, host='127.0.0.1')