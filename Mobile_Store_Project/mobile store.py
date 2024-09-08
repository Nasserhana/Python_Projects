# A dictionary of available items
available_items = {"Google Pixel 6a": {"price": 280, "quantity": 5},
                   "SAMSUNG Galaxy S23 Ultra": {"price": 1200, "quantity": 3},
                   "iPhone 13 Pro Max": {"price": 1300, "quantity": 2},
                   "Xiaomi Redmi 9A": {"price": 100, "quantity": 4},
                   "Huawei P50 Pro": {"price": 1000, "quantity": 1},
                   "OnePlus 9 Pro": {"price": 800, "quantity": 1}}
print("Welcome to Nasser Store!")
# initialize the dic to store items
cart_items = {}
# initialize list for total cart
lst_total = []

# loop
while True:
    # print message
    message = """What would you like to do?
1. View Available Items
2. View Cart
3. Total Cart Price
4. Clear Cart
5. Quit"""
    print(message)
    # get the choice from user
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        # 1. view available items
        for i, item in enumerate(available_items):
            # get item price
            item_price = available_items[item]['price']
            # get item quantity
            item_quantity = available_items[item]['quantity']
            # if quantity is not available
            if item_quantity == 0:
                print(f'{i + 1}. {item}: ${item_price} (Not Available)')
            else:
                print(f'{i + 1}. {item}: ${item_price}')

        # 2. chose the item which you want to buy it
        num_purchase = int(input("Enter the number of the item you want to purchase (Enter 0 to return to previous menu): "))
        # To return on this menu enter 0
        if num_purchase == 0:
            continue
        # get quantity
        quantity = int(input("Please, Enter the quantity: "))

        # convert dic keys to list of this item and added the number of the user want it
        # get order name
        order_name = list(available_items.keys())[num_purchase - 1]
        available_quantity = available_items[order_name]['quantity']
        # check if item is not available ( quantity is 0)
        if available_quantity == 0:
            print("Sorry, The Item is Not Available Now.")
            print(" ")
            continue
        if quantity > available_items[order_name]['quantity']:
            print(f"Sorry, we only have {available_items[order_name]['quantity']} of this item")
            continue

        # subtract 1 from order quantity
        available_items[order_name]['quantity'] -= quantity
        # get price
        order_price = available_items[order_name]['price']

        # we use get() method to check the quantity of item

        order_quantity = cart_items.get(order_name, {}).get('quantity', 0) + quantity
        # get info to the cart
        total = order_quantity * order_price
        order_info2 = {
            order_name: {
                'price': order_price,
                'quantity': order_quantity,
                'total': total
            }
        }
        # add order info to the cart
        cart_items.update(order_info2)
        print(f'{order_name} mobile has been added to the cart successfully.')
        print(" ")
    # -----------------------------------------------------------------
    # 2. view cart
    elif choice == "2":
        if cart_items:   # indicate to if cart == true
            print("Cart:")
            print('-'*30)
            for item, info in cart_items.items():    # to print information to user.
                print(f"{item}: ${cart_items[item]['price']:,.2f} * {cart_items[item]['quantity']} = ${cart_items[item]['total']:,.2f}")
            # we use list comprehension to calculate total item and sum it from list.
            total_lst = [cart_items[item]['price'] * cart_items[item]['quantity'] for item in cart_items]
            total_price_cart = sum(total_lst)
            print('-'*30)
            print(f'Total cart price: ${total_price_cart:,.2f}')
            print('-'*30)
        else:
            print("No items have been bought.")   # case user not chose any item
            print('-'*30)
            print("Total Cart price: $0.00")
            print(" ")
    # -------------------------------------------------------------
    elif choice == "3":
        for item, info in cart_items.items():
            total_lst = cart_items[item]['total']
            lst_total.append(total_lst)
        print('-' * 30)
        total_lst = [cart_items[item]['price'] * cart_items[item]['quantity'] for item in cart_items]
        total_price_cart = sum(total_lst)
        print(f'Total cart price: ${total_price_cart:,.2f}')
        print(" ")
    # -----------------------------------------------------------------
    elif choice == "4":   # to delete the cart
        question = input("Are you sure you want to clear the cart? (y/n): ")
        print(' ')
        if question == "n":
            continue
        else:
            cart_items.clear()
            lst_total.clear()
        print("Cart has been cleared successfully.")
    # -----------------------------------------------------------------
    elif choice == "5":   # to Quitting the program and print the cart that user chose it and added it in cart
        if cart_items:
            print("Thanks for choosing Nasser!")
            print("Cart: ")
            print('-' * 30)
            for item, info in cart_items.items():
                print(f"{item}: ${cart_items[item]['price']:,.2f} * {cart_items[item]['quantity']} = ${cart_items[item]['total']:,.2f}")
                total_lst = cart_items[item]['total']
                lst_total.append(total_lst)
            total_lst = [cart_items[item]['price'] * cart_items[item]['quantity'] for item in cart_items]
            total_price_cart = sum(total_lst)
            print('-' * 30)
            print(f'Total cart price: ${total_price_cart:,.2f}')
            break
        else:
            print("No items have been bought.")
            print('-' * 30)
            print("Total Cart price: $0.00")
            print(" ")
            break