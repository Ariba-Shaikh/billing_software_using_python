from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import bgcolor
from datetime import datetime
import sqlite3
import random

# Defining class Bill_App
class Bill_App:
    def __init__(self, root):
        self.root=root
        self.root.title("Billing Software")
        self.root.geometry("1400x700+0+0")
        self.root.configure(bg="beige")

        # Items list to store (product, qty, price, total) in Textarea
        self.items = []

        #======Variables======
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        bill_no = datetime.now().strftime("BILL-%Y%m%d%H%M%S")
        self.bill_no.set(bill_no)
        self.c_email=StringVar()
        self.product=StringVar()
        self.price=IntVar() 
        self.qty=IntVar() 
        self.sub_total=StringVar() 
        self.discount=StringVar() 
        self.tax=StringVar() 
        self.total=StringVar()
        self.bill_saved = False
        

        # Product list

        #Categories

        self.Category=["Select Option", "Fruit","Drinks", "Vegetable", "Dairy Products", "Snacks", "Beauty & Hygiene"]

        #Fruit

        self.SubCatFruit=["Apple","Banana", "Mango", "Guvava", "Orange"]

        self.Fruit_Prices={"Apple":120, "Banana":140, "Mango":200, "Guvava":150, "Orange":180}
        
        #Drinks

        self.SubCatDrinks=["Fruti","Fanta", "Big Cola"]

        self.Drinks_Prices={"Fruti":250, "Fanta":300, "Big Cola":200}

        #Vegetable
        self.SubCatVegetable=["Cabbage", "Onion", "Potato", "Cucumber", "Bottleguard", "Cauliflower", "Carrot"]

        self.Vegetable_Prices = {"Cabbage": 40, "Onion": 50, "Potato": 30, "Cucumber": 45, "Bottleguard": 60, "Cauliflower": 55, "Carrot": 35}

        #Dairy Products
        self.SubCatDairy=["Milk", "Yogurt", "Butter", "Cheese", "Paneer", "Cream"]

        self.Dairy_Prices={"Milk":75, "Yogurt":50, "Butter":250, "Cheese":250, "Paneer": 380, "Cream":150}

        #Snacks
        self.SubCatSnacks=["Lays", "Doritos", "Bourbon", "Oreo", "Noodles", "Snickers", "Skittles"]

        self.Snacks_Prices={"Lays":30, "Doritos":40, "Bourbon":30, "Oreo":40, "Noodles":50, "Snickers":40, "Skittles":40}

        #Beauty and Hygiene
        self.CatHygiene=["Shampoo", "Soap", "Lotion", "Sanitizer"]
        self.Shampoo=["Himalaya", "Treseme", "Pantene"]
        self.Shampoo_Price={"Himalaya":200, "Treseme":280, "Pantene":250}
        self.Soap=["Dettol", "Cinthol", "Lifebuoy", "Pears", "Dove"]
        self.Soap_Price={"Dettol":50, "Cinthol":45, "Lifebuoy":35, "Pears":50, "Dove":50}
        self.Lotion=["Nivea", "Pond's", "Lotus", "Mamaearth"]
        self.Lotion_Price={"Nivea":200, "Pond's":180, "Lotus":190, "Mamaearth":250}
        self.Sanitizer=["Savlon", "Godrej Protekt", "3M"]
        self.Sanitizer_Price={"Savlon":40, "Godrej Protekt":50, "3M":45}

        ##Customer details
        ##Customer details Label Frame
        label_frame = LabelFrame(self.root, text="Customer Details", font=("Courier New", 20, "bold"), padx=10, pady=10, bg="beige", relief=SOLID, bd=2)
        label_frame.pack(side="top", fill="x", padx=10, pady=10)

        ##Name
        Label(label_frame, text="Name:", font=("Courier New", 15, "bold"), bg="beige").grid(row=0, column=0, padx=5)
        self.txtCustName=Entry(label_frame, textvariable=self.c_name, font=("Courier New", 15), width=24, relief=SOLID, bg="white")
        self.txtCustName.grid(row=0, column=1)
        
        ##Mobile Number
        Label(label_frame, text=" Mobile Number:", font=("Courier New", 15, "bold"), bg="beige").grid(row=0, column=2, padx=5)
        self.entry_mob=Entry(label_frame, textvariable=self.c_phone, font=("Courier New", 15), relief=SOLID, bg="white")
        self.entry_mob.grid(row=0, column=3)

        ##Email
        Label(label_frame, text=" Email:", font=("Courier New", 15, "bold"), bg="beige").grid(row=0, column=4, padx=5)
        self.txtEmail=Entry(label_frame, textvariable=self.c_email, font=("Courier New", 15), width=25, relief=SOLID, bg="white")
        self.txtEmail.grid(row=0, column=5)

        #Products details Label Frame
        label_frame2=LabelFrame(self.root, text="Product Details", font=("Courier New", 20, "bold"), padx=10, pady=10, bg="beige", relief=SOLID, bd=2)
        label_frame2.pack(side="top", anchor="nw", padx=10, pady=5)

        #Categories
        Label(label_frame2, text="Select Category:", font=("Courier New", 15, "bold"), bg="beige").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.Combo_Category=ttk.Combobox(label_frame2, font=("Courier New", 15), value=self.Category, width=24, state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #Sub-Categories
        Label(label_frame2, text="Select Sub-Category:", font=("Courier New", 15, "bold"), bg="beige").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.ComboSubCategory=ttk.Combobox(label_frame2, font=("Courier New", 15), value=[""], width=24,state="readonly")
        self.ComboSubCategory.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)
        self.ComboSubCategory.bind("<<ComboboxSelected>>", self.update_price, add="+")
        
        #Sub-Category Items
        Label(label_frame2, text="Select Sub-Category Item:", font=("Courier New", 15, "bold"), bg="beige").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.ComboProduct=ttk.Combobox(label_frame2, textvariable=self.product, font=("Courier New", 15), value=[""], width=24, state="readonly")
        self.ComboProduct.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.ComboProduct.bind("<<ComboboxSelected>>", self.update_price)
        
        #Price
        Label(label_frame2, text="Price Per Item:", font=("Courier New", 15, "bold"), bg="beige").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.ComboPrice=Entry(label_frame2, font=("Courier New", 15), textvariable=self.price, width=25, state="readonly")
        self.ComboPrice.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        
        #Quantity
        Label(label_frame2, text="Quantity:", font=("Courier New", 15, "bold"), bg="beige").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.ComboQty=Entry(label_frame2, textvariable=self.qty, font=("Courier New", 15),width=25)
        self.ComboQty.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        #Bill Number
        Label(self.root, text="Bill Number:", font=("Courier New", 15, "bold"), bg="beige").place(x=730, y=120)
        self.bill_number=Entry(self.root, textvariable=self.bill_no, font=("Courier New", 15), width=24, relief=SOLID, bg="white", state="readonly").place(x=885, y=120)

        #Bill area
        self.textarea=Text(self.root, fg="Black", font=("Roboto Medium", 13), relief=SOLID, bd=3, bg="white", width=59)
        self.textarea.place(x=730, y=170)

        #Add Button
        self.add_btn=Button(self.root, text="Add Item", fg="black", bg="#e29e0b", width="27", height="1", font=("Courier New", 15, "bold"), bd=2, command=self.add_item)
        self.add_btn.place(x=10, y=375)

        #Clear Button
        self.add_btn=Button(self.root, text="Clear", fg="black", bg="#b5b5b5", width="27", height="1", font=("Courier New", 15, "bold"), bd=2, command=self.clear)
        self.add_btn.place(x=355, y=375)

        #Total Amount
        Label(self.root, text="Sub-Total:", font=("Courier New", 15, "bold"), bg="beige").place(x=10, y=440)
        self.txtCustName=Entry(self.root, textvariable=self.sub_total, font=("Courier New", 15), width=24, relief=SOLID, bg="white", state="readonly")
        self.txtCustName.place(x=178, y=440)

        #Tax Applied
        Label(self.root, text="Tax (%):", font=("Courier New", 15, "bold"), bg="beige").place(x=10, y=480)
        self.txtCustName=Entry(self.root, textvariable=self.tax, font=("Courier New", 15), width=24, relief=SOLID, bg="white", state="readonly")
        self.txtCustName.place(x=178, y=480)

        #Discount
        Label(self.root, text="Discount (%):", font=("Courier New", 15, "bold"), bg="beige").place(x=10, y=520)
        self.txtCustName=Entry(self.root, textvariable=self.discount, font=("Courier New", 15), width=24, relief=SOLID, bg="white", state="readonly")
        self.txtCustName.place(x=178, y=520)
        
        #Grand Total
        Label(self.root, text="Grand Total:", font=("Courier New", 15, "bold"), bg="beige").place(x=10, y=560)
        self.txtCustName=Entry(self.root, textvariable=self.total, font=("Courier New", 15), width=24, relief=SOLID, bg="white", state="readonly")
        self.txtCustName.place(x=178, y=560)

        #Generate Bill Button
        self.add_btn=Button(self.root, text="Generate Bill", fg="black", bg="#3ae20b", width="27", height="1", font=("Courier New", 15, "bold"), bd=2, command=self.generate_bill)
        self.add_btn.place(x=10, y=600)

        #Save Bill Button
        self.add_btn=Button(self.root, text="Save Bill", fg="black", bg="#459af6", width="27", height="1", font=("Courier New", 15, "bold"), bd=2, command=self.save_bill_to_db)
        self.add_btn.place(x=355, y=600)

        self.welcome()

    ##======Functions=======

    #Categories
    def Categories(self, event=""):
        if self.Combo_Category.get()=="Fruit":
            self.ComboSubCategory.config(value=self.SubCatFruit)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Drinks":
            self.ComboSubCategory.config(value=self.SubCatDrinks)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Vegetable":
            self.ComboSubCategory.config(value=self.SubCatVegetable)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Dairy Products":
            self.ComboSubCategory.config(value=self.SubCatDairy)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Snacks":
            self.ComboSubCategory.config(value=self.SubCatSnacks)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Beauty & Hygiene":
            self.ComboSubCategory.config(value=self.CatHygiene)
            self.ComboSubCategory.current(0)
        
    #Product Add
    def Product_add(self, event=""):
        if self.ComboSubCategory.get()=="Shampoo":
            self.ComboProduct.config(value=self.Shampoo)
            self.ComboProduct.current(0)
            
        if self.ComboSubCategory.get()=="Soap":
            self.ComboProduct.config(value=self.Soap)
            self.ComboProduct.current(0)
            

        if self.ComboSubCategory.get()=="Lotion":
            self.ComboProduct.config(value=self.Lotion)
            self.ComboProduct.current(0)
            

        if self.ComboSubCategory.get()=="Sanitizer":
            self.ComboProduct.config(value=self.Sanitizer)
            self.ComboProduct.current(0)
            

        if self.ComboSubCategory.get() not in self.CatHygiene:
            self.ComboProduct.config(value="No-Sub-Category-items")
            self.ComboProduct.current(0)
    
    #Update Price
    def update_price(self, event=""):
        category = self.Combo_Category.get()
        subcat = self.ComboSubCategory.get()
        product = self.ComboProduct.get()

        # Beauty & Hygiene, product comes in ComboProduct from ComboSubCategory combobox
        if category == "Beauty & Hygiene":
            if subcat == "Shampoo":
                self.price.set(self.Shampoo_Price.get(product, 0))
            elif subcat == "Soap":
                self.price.set(self.Soap_Price.get(product, 0))
            elif subcat == "Lotion":
                self.price.set(self.Lotion_Price.get(product, 0))
            elif subcat == "Sanitizer":
                self.price.set(self.Sanitizer_Price.get(product, 0))

        # Other categories, product comes in ComboSubCategory from Combo_Category combobox
        else:
            if category == "Fruit":
                self.price.set(self.Fruit_Prices.get(subcat, 0))
            elif category == "Drinks":
                self.price.set(self.Drinks_Prices.get(subcat, 0))
            elif category == "Vegetable":
                self.price.set(self.Vegetable_Prices.get(subcat, 0))
            elif category == "Dairy Products":
                self.price.set(self.Dairy_Prices.get(subcat, 0))
            elif category == "Snacks":
                self.price.set(self.Snacks_Prices.get(subcat, 0))
    
    def add_item(self):
        try:
            category = self.Combo_Category.get()

            # Get product name based on category type
            if category == "Beauty & Hygiene":
                product = self.ComboProduct.get()
            else:
                product = self.ComboSubCategory.get()

            name=self.c_name.get()
            phone=self.c_phone.get()
            email=self.c_email.get()
            price = self.price.get()
            qty = self.qty.get()

            if not name:
                messagebox.showerror("Input Error", "Name field should not be empty.")
                return
            if not phone:
                messagebox.showerror("Input Error", "Mobile number field should not be empty.")
                return
            if not email:
                messagebox.showerror("Input Error", "Email field should not be empty.")
                return
            if qty == 0:
                messagebox.showerror("Input Error", "Please enter quantity.")
                return

            #Calculate subtotal
            line_total = price * qty

            # Update subtotal field
            current_subtotal = float(self.sub_total.get()) if self.sub_total.get() else 0
            new_subtotal = current_subtotal + line_total
            self.sub_total.set(str(new_subtotal))

            # Store item for later bill generation
            self.items.append((product, category, qty, price, line_total))

            self.display_items()

        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")
    
    def welcome(self):
        # Get today's date in DD-MM-YYYY format
        current_date = datetime.now().strftime("%d-%m-%Y")

        # Define styles
        self.textarea.tag_configure("header", font=("Segoe UI", 13, "bold"))
        self.textarea.tag_configure("bold", font=("Segoe UI", 11, "bold"))

        # Header
        self.textarea.insert(END, f"\t\tWELCOME TO SUPER MARKET\t\t\n\n", "header")
        self.textarea.insert(END, f"Date: {current_date}\n", "bold")
        self.textarea.insert(END, f"Contact Number : 7392754101\n", "bold")
        self.textarea.insert(END, f"GSTIN : 27ABCDE1234F1Z5\n", "bold")
        self.textarea.insert(END, f"City : Mumbai\n", "bold")
        self.textarea.insert(END, "-"*88 + "\n")

    def display_items(self):
        self.textarea.delete(1.0, END)  # clear old text

        # Define styles
        self.textarea.tag_configure("header", font=("Segoe UI", 13, "bold"))
        self.textarea.tag_configure("footer", font=("Segoe UI", 12, "italic"))

        self.welcome()     #Call welcome method everytime

        #Customer details
        self.textarea.insert(END, f"{'Customer Details:'}\n\n", "header")
        self.textarea.insert(END, f"Bill Number   : {self.bill_no.get()}\n")
        self.textarea.insert(END, f"Customer Name : {self.c_name.get()}\n")
        self.textarea.insert(END, f"Customer Phone: {self.c_phone.get()}\n")
        self.textarea.insert(END, f"Customer Email: {self.c_email.get()}\n")
        self.textarea.insert(END, "-"*88 + "\n")

        #Bill details
        self.textarea.insert(END, f"Bill Details:\n\n", "header")
        
        # Table header
        self.textarea.insert(END, f"Product\t\tCategory\t\tQty\tPrice\tAmount\n", "header")
        self.textarea.insert(END, "-"*88 + "\n")

        #loop through items list of tuples
        # self.items = [(product, qty, price, total), ...]
        for item in self.items:
            product, category, qty, price, line_total = item
            self.textarea.insert(END, f"{product}\t\t{category}\t\t  {qty}\t{price}\t{line_total}\n")
            self.textarea.insert(END, "-"*88 + "\n")

        self.textarea.insert(END, "\n")
    
    def clear(self):

        if not self.bill_saved:
            confirm = messagebox.askyesno("Warning", "You haven't saved this bill yet. Do you want to clear without saving?")
            if not confirm:
                return # stop clearing if user chooses No

        # proceed with clearing
        # Clear the bill text area
        self.textarea.delete(1.0, END)
        self.welcome()

        # Reset customer details
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")

        # Reset product details
        self.product.set("")
        self.price.set(0)
        self.qty.set(0)

        # Reset totals
        self.sub_total.set("")
        self.tax.set("")
        self.discount.set("")
        self.total.set("")

        # Clear items list
        self.items.clear()

        # Generate a new bill number
        new_bill_no = datetime.now().strftime("BILL-%Y%m%d%H%M%S")
        self.bill_no.set(new_bill_no)

        # reset for new bill
        self.bill_saved = False 


    
    def calc_tax(self):
        if self.sub_total.get():
            total_amount=float(self.sub_total.get())
            if total_amount <= 500:
                tax_pct = 4
            elif total_amount <= 1000:
                tax_pct = 8
            elif total_amount <= 5000:
                tax_pct = 10 
            else:
                tax_pct = 12
            tax_amt = total_amount * (tax_pct / 100)
            return tax_amt, tax_pct
    
    def calc_discount(self):
        if self.sub_total.get():
            total_amount=float(self.sub_total.get())
            if total_amount <= 500:
                discount_pct = 3
            elif total_amount <= 1000:
                discount_pct = 5
            elif total_amount <= 5000:
                discount_pct = 8
            else:
                discount_pct = 10
            discount_amt = total_amount * (discount_pct / 100)
            return discount_amt, discount_pct
    
    def generate_bill(self):

        #Get the sub-total value from Entry
        total_amount=float(self.sub_total.get())
        #Get tax values (in % & in Rs)
        tax_amt, tax_pct = self.calc_tax()
        #Get discount values (in % & in Rs)
        discount_amt, discount_pct = self.calc_discount()
        #Clculate grand total
        grand_total = total_amount - discount_amt + tax_amt
        #Display grand total
        self.total.set(str(grand_total))
        #Display tax in %
        self.tax.set(str(tax_pct))
        #display discount in %
        self.discount.set(str(discount_pct))

        #Define styles
        self.textarea.tag_configure("footer", font=("Segoe UI", 12, "italic"))

        #Dispaly totals
        self.textarea.insert(END, f"Sub-Total:\t{self.sub_total.get()} Rs\n")
        self.textarea.insert(END, f"Tax (%):\t{self.tax.get()} %\n")
        self.textarea.insert(END, f"Discount (%):\t{self.discount.get()} %\n")
        self.textarea.insert(END, f"Grand Total:\t{self.total.get()} Rs\n\n")

        # Footer
        self.textarea.insert(END, f"Thank You for shopping with us!\n", "footer")
        self.textarea.insert(END, f"Visit Again.\n", "footer")

        # bill is generated but not saved yet
        self.bill_saved = False


    
    def save_bill_to_db(self):
        try:
            conn = sqlite3.connect("billing.db")
            cursor = conn.cursor()

            # Create tables if not exist
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS bills (
            bill_no TEXT PRIMARY KEY,
            customer_name TEXT,
            phone TEXT,
            email TEXT,
            sub_total REAL,
            tax REAL,
            discount REAL,
            grand_total REAL,
            date TEXT
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS bill_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bill_no TEXT,
            product TEXT,
            category TEXT,
            qty INTEGER,
            price REAL,
            line_total REAL,
            FOREIGN KEY (bill_no) REFERENCES bills(bill_no)
            )
            """)

            # Insert bill summary
            cursor.execute("""
            INSERT INTO bills (bill_no, customer_name, phone, email, sub_total, tax, discount, grand_total, date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
            self.bill_no.get(),
            self.c_name.get(),
            self.c_phone.get(),
            self.c_email.get(),
            float(self.sub_total.get()),
            float(self.tax.get()),
            float(self.discount.get()),
            float(self.total.get()),
            datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            ))

            # Insert line items
            for product, category, qty, price, line_total in self.items:
                cursor.execute("""
                INSERT INTO bill_items (bill_no, product, category, qty, price, line_total)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (
                self.bill_no.get(),
                product,
                category,
                qty,
                price,
                line_total
                ))

            conn.commit()
            conn.close()
            self.bill_saved = True
            messagebox.showinfo("Success", "Bill and items saved successfully!")

        except Exception as e:
            messagebox.showerror("Database Error", f"Could not save bill: {e}")




if __name__=='__main__':
    # Creating object of class Tk()
    root=Tk()
    #Creating object of class Bill_App
    obj=Bill_App(root)
    root.mainloop()