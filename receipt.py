import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF
from datetime import datetime
import os
import webbrowser  # To open the generated PDF in the default PDF viewer

# Function to generate PDF receipt using fpdf
def generate_sales_receipt(vendor_name, items, total_amount, payment_method):
    # Generate a unique receipt number (transaction ID)
    receipt_number = f"SALE{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    # Get the current system date and time for the purchase
    purchase_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    # Define the location of the purchase (fixed for now)
    location = "Department Store, Kevin Mall, Avinashi, India"
    
    # Define the directory where the receipt will be saved
    save_directory = os.path.expanduser("~/Downloads")  # Save in the Downloads folder
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)  # Create folder if it doesn't exist
    
    # Create the filename for the PDF
    pdf_filename = f"{save_directory}/sales_receipt_{receipt_number}.pdf"
    
    # Create an instance of FPDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Set font for the title
    pdf.set_font("Arial", 'B', 16)
    
    # Add title to the receipt
    pdf.cell(200, 10, vendor_name, ln=True, align='C')  # Vendor name as header
    pdf.cell(200, 10, "Sales Receipt", ln=True, align='C')
    
    # Set font for the body of the receipt
    pdf.set_font("Arial", size=12)
    
    # Add receipt data to the PDF
    pdf.ln(10)  # Line break
    pdf.cell(100, 10, f"Receipt Number: {receipt_number}")
    pdf.ln(10)
    pdf.cell(100, 10, f"Purchase Date & Time: {purchase_datetime}")
    pdf.ln(10)
    pdf.cell(100, 10, f"Location: {location}")
    pdf.ln(10)
    
    # Add itemized list
    pdf.cell(100, 10, "Items Purchased:") 
    pdf.ln(5)
    
    for item in items:
        pdf.cell(100, 10, f"- {item[0]}: {item[1]:,.2f} Rs.")  # Item name and price
        pdf.ln(5)
    
    # Add total amount
    pdf.ln(5)
    pdf.cell(100, 10, f"Total Amount: {total_amount:,.2f} Rs.")
    
    pdf.ln(10)
    pdf.cell(100, 10, f"Payment Method: {payment_method}")
    pdf.ln(10)
    pdf.cell(100, 10, "Status: Successful")
    pdf.ln(10)
    pdf.cell(100, 10, "Thank you for your purchase!")
    
    # Save the PDF file
    pdf.output(pdf_filename)
    
    # Open the generated PDF in the default PDF viewer (for preview)
    try:
        webbrowser.open(pdf_filename)  # Open the PDF in the default viewer
        messagebox.showinfo("Receipt Generated", f"Sales receipt generated!\nSaved to: {pdf_filename}\nYou can preview it now.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while opening the receipt: {str(e)}")
    
# Function to handle the button click event for adding items dynamically
def add_items():
    try:
        # Get the item numbers entered by the user
        item_numbers = item_numbers_entry.get().split(",")
        item_numbers = [int(num.strip()) for num in item_numbers if num.strip().isdigit()]
        
        if not item_numbers:
            raise ValueError("Please enter valid item numbers.")
        
        # Check if each item number is valid
        for num in item_numbers:
            if num < 1 or num > len(item_data):
                raise ValueError(f"Item number {num} is out of range.")
            
            item_name = item_data[num]["name"]
            item_price = item_data[num]["price"]
            items.append((item_name, item_price))
        
        update_item_list()
        item_numbers_entry.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Function to update the list of items in the display
def update_item_list():
    item_listbox.delete(0, tk.END)
    for item in items:
        item_listbox.insert(tk.END, f"{item[0]} - {item[1]:,.2f} Rs.")
    
    # Update the total amount dynamically
    total_amount = sum(item[1] for item in items)
    total_label.config(text=f"Total Amount: {total_amount:,.2f} Rs.")
    
# Function to handle the generate receipt button click event
def generate_receipt():
    if not items:
        messagebox.showerror("Input Error", "Please add at least one item.")
        return
    
    payment_method = payment_method_var.get()
    
    if not payment_method:
        messagebox.showerror("Input Error", "Please select a payment method.")
        return
    
    total_amount = sum(item[1] for item in items)  # Calculate total amount
    generate_sales_receipt("Feel Fresh", items, total_amount, payment_method)

# Create Tkinter window
root = tk.Tk()
root.title("Feel Fresh Sales Receipt Generator")

# List to hold the items added by the user
items = []

# 100 items with names and prices (item_data dictionary as provided)
item_data = {
    1: {"name": "Rice", "price": 500.00},
    2: {"name": "Wheat", "price": 350.00},
    3: {"name": "Sugar", "price": 250.00},
    4: {"name": "Salt", "price": 50.00},
    5: {"name": "Milk", "price": 45.00},
    6: {"name": "Butter", "price": 300.00},
    7: {"name": "Oil", "price": 120.00},
    8: {"name": "Tea", "price": 80.00},
    9: {"name": "Coffee", "price": 150.00},
    10: {"name": "Juice", "price": 90.00},
    11: {"name": "Cereal", "price": 200.00},
    12: {"name": "Pasta", "price": 150.00},
    13: {"name": "Tomatoes", "price": 60.00},
    14: {"name": "Onions", "price": 30.00},
    15: {"name": "Garlic", "price": 40.00},
    16: {"name": "Apples", "price": 100.00},
    17: {"name": "Bananas", "price": 50.00},
    18: {"name": "Oranges", "price": 90.00},
    19: {"name": "Lemons", "price": 120.00},
    20: {"name": "Grapes", "price": 150.00},
    21: {"name": "Carrots", "price": 40.00},
    22: {"name": "Potatoes", "price": 60.00},
    23: {"name": "Spinach", "price": 70.00},
    24: {"name": "Lettuce", "price": 50.00},
    25: {"name": "Cucumber", "price": 30.00},
    26: {"name": "Peppers", "price": 80.00},
    27: {"name": "Zucchini", "price": 60.00},
    28: {"name": "Eggplant", "price": 90.00},
    29: {"name": "Mango", "price": 120.00},
    30: {"name": "Pineapple", "price": 150.00},
    31: {"name": "Strawberries", "price": 200.00},
    32: {"name": "Blueberries", "price": 180.00},
    33: {"name": "Cherries", "price": 250.00},
    34: {"name": "Raspberries", "price": 230.00},
    35: {"name": "Blackberries", "price": 220.00},
    36: {"name": "Lettuce", "price": 50.00},
    37: {"name": "Sweet Corn", "price": 40.00},
    38: {"name": "Pumpkin", "price": 120.00},
    39: {"name": "Cabbage", "price": 50.00},
    40: {"name": "Avocados", "price": 180.00},
    41: {"name": "Pears", "price": 90.00},
    42: {"name": "Papaya", "price": 150.00},
    43: {"name": "Melons", "price": 130.00},
    44: {"name": "Watermelon", "price": 160.00},
    45: {"name": "Ginger", "price": 80.00},
    46: {"name": "Mustard", "price": 60.00},
    47: {"name": "Soya Sauce", "price": 40.00},
    48: {"name": "Vinegar", "price": 30.00},
    49: {"name": "Honey", "price": 250.00},
    50: {"name": "Maple Syrup", "price": 300.00},
    51: {"name": "Chocolate", "price": 200.00},
    52: {"name": "Cookies", "price": 180.00},
    53: {"name": "Cake", "price": 220.00},
    54: {"name": "Biscuits", "price": 150.00},
    55: {"name": "Chips", "price": 120.00},
    56: {"name": "Crackers", "price": 100.00},
    57: {"name": "Popcorn", "price": 50.00},
    58: {"name": "Nuts", "price": 200.00},
    59: {"name": "Cheese", "price": 250.00},
    60: {"name": "Yogurt", "price": 100.00},
    61: {"name": "Ice Cream", "price": 300.00},
    62: {"name": "Pudding", "price": 120.00},
    63: {"name": "Jelly", "price": 80.00},
    64: {"name": "Cakes", "price": 250.00},
    65: {"name": "Muffins", "price": 180.00},
    66: {"name": "Bread", "price": 50.00},
    67: {"name": "Toast", "price": 70.00},
    68: {"name": "Bagels", "price": 120.00},
    69: {"name": "Croissants", "price": 150.00},
    70: {"name": "Buns", "price": 80.00},
    71: {"name": "Sausages", "price": 300.00},
    72: {"name": "Chicken", "price": 450.00},
    73: {"name": "Pork", "price": 500.00},
    74: {"name": "Beef", "price": 600.00},
    75: {"name": "Lamb", "price": 700.00},
    76: {"name": "Fish", "price": 200.00},
    77: {"name": "Shrimp", "price": 250.00},
    78: {"name": "Crab", "price": 300.00},
    79: {"name": "Mussels", "price": 150.00},
    80: {"name": "Oysters", "price": 200.00},
    81: {"name": "Tuna", "price": 180.00},
    82: {"name": "Salmon", "price": 220.00},
    83: {"name": "Prawns", "price": 250.00},
    84: {"name": "Fish Fillets", "price": 350.00},
    85: {"name": "Hot Sauce", "price": 60.00},
    86: {"name": "Barbecue Sauce", "price": 80.00},
    87: {"name": "Ketchup", "price": 40.00},
    88: {"name": "Mayonnaise", "price": 50.00},
    89: {"name": "Mustard Sauce", "price": 30.00},
    90: {"name": "Soy Sauce", "price": 70.00},
    91: {"name": "Salad Dressing", "price": 100.00},
    92: {"name": "Chili Sauce", "price": 90.00},
    93: {"name": "Ghee", "price": 350.00},
    94: {"name": "Milk Powder", "price": 300.00},
    95: {"name": "Tea Bags", "price": 50.00},
    96: {"name": "Coffee Powder", "price": 120.00},
    97: {"name": "Herbal Tea", "price": 150.00},
    98: {"name": "Green Tea", "price": 180.00},
    99: {"name": "Chai Tea", "price": 100.00},
    100: {"name": "Lemon Tea", "price": 120.00}
}
# Adding a Scrollable Listbox with an Entry for item numbers and button

# Setup UI elements
item_numbers_label = tk.Label(root, text="Enter Item Numbers (comma separated):")
item_numbers_label.grid(row=0, column=0, padx=10, pady=10)

item_numbers_entry = tk.Entry(root)
item_numbers_entry.grid(row=0, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add Items", command=add_items)
add_button.grid(row=0, column=2, padx=10, pady=10)

item_listbox = tk.Listbox(root, width=60, height=10)
item_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Total amount label
total_label = tk.Label(root, text="Total Amount: 0 Rs.")
total_label.grid(row=2, column=0, padx=10, pady=10)

payment_method_var = tk.StringVar()
payment_method_label = tk.Label(root, text="Select Payment Method:")
payment_method_label.grid(row=3, column=0, padx=10, pady=10)

payment_method_options = ["Cash", "Card", "UPI"]
payment_method_menu = tk.OptionMenu(root, payment_method_var, *payment_method_options)
payment_method_menu.grid(row=3, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Receipt", command=generate_receipt)
generate_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
