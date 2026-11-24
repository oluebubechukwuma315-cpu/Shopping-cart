import tkinter as tk


class ShoppingCart:
    def __init__(self):
        self.cart = []
    def present(self,name):
        for item in self.cart:
            if item["name"] == name:
                return True
        return False
    def add_item(self,name,price,qty):
        item = {"name":name,"price":price,"qty":qty}

        if not self.present(name):
            self.cart.append(item)
        else:
            for item in self.cart:
                if item["name"] == name:
                    item["qty"] += qty

    def remove(self,name):
        for i,item in enumerate(self.cart):
            if item["name"] == name:
                self.cart.pop(i)

    def total(self):
        total = 0
        for item in self.cart:
            total += (item["price"]*item["qty"])
        return total
    def discount(self,total,percent):
        per = percent/100
        result = round(total - (total*per),2)
        return result


carts = ShoppingCart()

window = tk.Tk()
window.geometry("500x500")
label = tk.Label(window,text="SHOPPING CART", font  = ("Arial",24),fg = "black",bg="gray")
label.pack(fill = "x")

form = tk.Frame(window)
form.pack()

label2 = tk.Label(form,text = "NAME ")
label2.grid(row =0 ,column = 0)
entry_name = tk.Entry(form)
entry_name.grid(row =0,column=1)

label3 = tk.Label(form,text="PRICE")
label3.grid(row = 1, column=0)
entry_price = tk.Entry(form)
entry_price.grid(row=1,column=1)

label4 = tk.Label(form,text="QUANTITY")
label4.grid(row = 2, column=0)
entry_qty = tk.Entry(form)
entry_qty.grid(row = 2,column=1)

def add():
    name = entry_name.get()
    price = entry_price.get()
    qty = entry_qty.get()
    show.config(text="")
    if not name:
        show.config(text="name cannot be empty")
        return
    try:
        price = float(price)
        qty = int(qty)
    except:
        show.config(text = "Error: box cannot be empty and price and quantity must be numbers")
        return
    carts.add_item(name,price,qty)
    entry_name.delete(0,tk.END)
    entry_price.delete(0,tk.END)
    entry_qty.delete(0,tk.END)
def view():
    show.config(text="")

    if not carts.cart:
        show.config(text = "empty")
        return
    else:   
        formatted_text = [f"Name: {item["name"]}, price: {item["price"]}, qty: {item["qty"]}" for item in carts.cart]
        formatted_text = "\n".join(formatted_text)
        show.config(text = formatted_text)

def rmv():
    window.withdraw()
    second = tk.Toplevel(window)
    second.title("Remove")
    second.geometry("300x300")
    slabel = tk.Label(second,text = "NAME").grid(row=0,column=0)
    entry_name2 = tk.Entry(second)
    entry_name2.grid(row = 0,column=1)
    def remv():
        name = entry_name2.get()
        if not name:
            show.config(text = "Name cannot be empty")
            return
        else:        name = entry_name2.get()
        if not name:
            show.config(text = "Name cannot be empty")
        else:
            carts.remove(name)
        second.destroy()
        window.deiconify()
    button = tk.Button(second,text = "click",command=remv)
    button.grid()
    show = tk.Label(second,text = "")
    show.grid()

def cal_total():
    show.config(text="")
    totals = carts.total()
    show.config(text= f"Total: {totals}")
button_add = tk.Button(window,text = "Add item",fg = "blue",command=add)
button_add.pack()
button_view = tk.Button(window,text = "view cart",command=view)
button_view.pack()
button_rmv = tk.Button(window,text = "remove",command=rmv)
button_rmv.pack()

button_total = tk.Button(window,text = "Total",command=cal_total)
button_total.pack()
show = tk.Label(window,text = "")
show.pack()
window.mainloop()



