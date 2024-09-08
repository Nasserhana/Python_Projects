# available items
pizzas = {"Margherita": 100, "Pepperoni": 120, "Meat Lovers": 150, "Chicken": 130}
burgers = {"Beef": 100, "Chicken": 80, "Bacon": 120}
drinks = {"Coke": 30, "Sprite": 25, "Fanta": 25, "Pepsi": 30}
soups = {"Chicken Soup": 50, "Beef Soup": 60, "Mushroom Soup": 40}
desserts = {"Ice Cream": 50, "Chocolate Cake": 60, "Cheese Cake": 70}
print("Welcome to Nasser Restaurant")
cart = {}
lst_total = []

while True:
    message = """
1. Pizzas
2. Burgers
3. Drinks
4. Soups
5. Desserts"""
    print(message)
    number_item = input("Please, Enter the number of the item you want (Enter to exit): ")
    if number_item == "":
        print('-' * 30)
        print("your order is:")
        for item, info in cart.items():
            print('-' * 30)
            print(
                f"Item: {item} {cart[item]['category']}\nQuantity: {cart[item]['quantity']} Units\nPrice: {cart[item]['price']} EGP")
        print('-' * 30)
        print(f"Total: {sum(lst_total):.2f} EGP")
        break

    elif number_item == "1":
        category = "Pizza"
        for i, item in enumerate(pizzas):
            print(f"{i + 1}. {item}: {pizzas[item]} EGP")

        choice_item = int(input("Please, Enter the number of the item you want (0 to return to the previous menu): "))
        if choice_item == 0:
            continue
        name_item = list(pizzas.keys())[choice_item - 1]
        price = float(pizzas[name_item])
        quantity = int(input("Please, Enter the quantity: "))
        # quantity_dic = cart.get(name_item, {}).get('quantity', 0) + 1
        total = quantity * price
        lst_total.append(total)
        cart.update({name_item: {'quantity': quantity, 'price': price, 'category': category, 'total': total}})
        print("Added item successfully")
        print('-'*30)
        # for item, info in cart.items():
        #     print(f"Name: {item}\nQuantity: {cart[item]['quantity']}\nPrice: {cart[item]['price']}")
        # line 30, 31 to if you want to print items on screen
        message2 = """1. Add another item
2. View the order
3. Clear the order
4. Exit """
        print(message2)
        choice = input("Please, Enter your choice: ")

        if choice == "1":
            continue
        elif choice == "2":
            print('-'*30)
            print("your order is:")
            for item, info in cart.items():
                print('-' * 30)
                print(f"Item: {item} {cart[item]['category']}\nQuantity: {cart[item]['quantity']} Units\nPrice: {cart[item]['price']} EGP")
                print('-' * 30)
                print(f"Item total: {cart[item]['total']} EGP")

            print('-'*30)
            print(f"Total: {sum(lst_total):,} EGP")

        elif choice == "3":
            cart.pop(name_item)
            lst_total.remove(total)
            print("Order cleared")
        elif choice == "4":
            print('-' * 30)
            print("your order is:")
            for item, info in cart.items():
                print('-' * 30)
                print(
                    f"Item: {item} {cart[item]['category']}\nQuantity: {cart[item]['quantity']} Units\nPrice: {cart[item]['price']} EGP")
                print('-' * 30)
                print(f"Item total: {cart[item]['total']} EGP")

            break
        else:
            print("Invalid option")
# -------------------------------------------------------------------------------------
    elif number_item == "2":
        category2 = "Burger"
        for i, name in enumerate(burgers):
            print(f"{i + 1}. {name}: {burgers[name]} EGP")

        choice_item = int(input("Please, Enter the number of the item you want (0 to return to the previous menu): "))
        if choice_item == 0:
            continue
        name_item = list(burgers.keys())[choice_item - 1]
        price = float(burgers[name_item])
        quantity = int(input("Please, Enter the quantity: "))
        # quantity_dic = cart.get(name_item, {}).get('quantity', 0) + 1
        total = quantity * price
        cart.update({name_item: {'quantity': quantity, 'price': price, 'category': category2, 'total': total}})
        lst_total.append(total)
        print("Added item successfully")
        print('-' * 30)
        # for item, info in cart.items():
        #     print(f"Name: {item}\nQuantity: {cart[item]['quantity']}\nPrice: {cart[item]['price']}")
        # line 30, 31 to if you want to print items on screen
        message2 = """1. Add another item
2. View the order
3. Clear the order
4. Exit """
        print(message2)
        choice = input("Please, Enter your choice: ")

        if choice == "1":
            continue
        elif choice == "2":
            print('-' * 30)
            print("your order is:")
            for name, info in cart.items():
                print('-' * 30)
                print(f"Item: {name} {cart[name]['category']}\nQuantity: {cart[name]['quantity']} Units\nPrice: {cart[name]['price']} EGP")
                print('-' * 30)
                print(f"Item total: {cart[name]['total']} EGP")

            print('-' * 30)
            print(f"Total: {sum(lst_total):,} EGP")

        elif choice == "3":
            cart.pop(name_item)
            lst_total.remove(total)
            print("Order cleared")
        elif choice == "4":
            print('-' * 30)
            print("your order is:")
            for item, info in cart.items():
                print('-' * 30)
                print(
                    f"Item: {item} {cart[item]['category']}\nQuantity: {cart[item]['quantity']} Units\nPrice: {cart[item]['price']} EGP")
                print('-' * 30)
                print(f"Item total: {cart[item]['total']} EGP")

            break
        else:
            print("Invalid option")

# -----------------------------------------------------------------------------------------------------------------

    elif number_item == "3":
        category3 = "Drink"
        for i, name in enumerate(drinks):
            print(f"{i + 1}. {name}: {drinks[name]} EGP")

        choice_item = int(input("Please, Enter the number of the item you want (0 to return to the previous menu): "))
        if choice_item == 0:
            continue
        name_item = list(drinks.keys())[choice_item - 1]
        price = float(drinks[name_item])
        quantity = int(input("Please, Enter the quantity: "))
        # quantity_dic = cart.get(name_item, {}).get('quantity', 0) + 1
        total = quantity * price
        cart.update({name_item: {'quantity': quantity, 'price': price, 'category': category3, 'total': total}})
        lst_total.append(total)
        print("Added item successfully")
        print('-' * 30)
        # for item, info in cart.items():
        #     print(f"Name: {item}\nQuantity: {cart[item]['quantity']}\nPrice: {cart[item]['price']}")
        # line 30, 31 to if you want to print items on screen
        message2 = """1. Add another item
2. View the order
3. Clear the order
4. Exit """
        print(message2)
        choice = input("Please, Enter your choice: ")

        if choice == "1":
            continue
        elif choice == "2":
            print('-' * 30)
            print("your order is:")
            for name, info in cart.items():
                print('-' * 30)
                print(
                    f"Item: {name} {cart[name]['category']}\nQuantity: {cart[name]['quantity']} Units\nPrice: {cart[name]['price']} EGP")
                print('-' * 30)
                print(f"Item total: {cart[name]['total']} EGP")

            print('-' * 30)
            print(f"Total: {sum(lst_total):,} EGP")

        elif choice == "3":
            cart.pop(name_item)
            lst_total.remove(total)
            print("Order cleared")
        elif choice == "4":
            print('-' * 30)
            print("your order is:")
            for item, info in cart.items():
                print('-' * 30)
                print(
                    f"Item: {item} {cart[item]['category']}\nQuantity: {cart[item]['quantity']} Units\nPrice: {cart[item]['price']} EGP")
                print('-' * 30)
                print(f"Item total: {cart[item]['total']} EGP")

            break
        else:
            print("Invalid option")
# -----------------------------------------------------------------------------------------------------------------

    elif number_item == "4":
        category4 = "Soup"
        for i, name in enumerate(soups):
            print(f"{i + 1}. {name}: {soups[name]} EGP")

        choice_item = int(input("Please, Enter the number of the item you want (0 to return to the previous menu): "))
        if choice_item == 0:
            continue
        name_item = list(soups.keys())[choice_item - 1]
        price = float(soups[name_item])
        quantity = int(input("Please, Enter the quantity: "))
        # quantity_dic = cart.get(name_item, {}).get('quantity', 0) + 1
        total = quantity * price
        cart.update({name_item: {'quantity': quantity, 'price': price, 'category': category4, 'total': total}})
        lst_total.append(total)
        print("Added item successfully")
        print('-' * 30)
        # for item, info in cart.items():
        #     print(f"Name: {item}\nQuantity: {cart[item]['quantity']}\nPrice: {cart[item]['price']}")
        # line 30, 31 to if you want to print items on screen
        message2 = """1. Add another item
2. View the order
3. Clear the order
4. Exit """
        print(message2)
        choice = input("Please, Enter your choice: ")

        if choice == "1":
            continue
        elif choice == "2":
            print('-' * 30)
            print("your order is:")
            for name, info in cart.items():
                print('-' * 30)
                print(
                    f"Item: {name} {cart[name]['category']}\nQuantity: {cart[name]['quantity']} Units\nPrice: {cart[name]['price']} EGP")
                print('-' * 30)
                print(f"Item total: {cart[name]['total']} EGP")

            print('-' * 30)
            print(f"Total: {sum(lst_total):,} EGP")
        elif choice == "3":
            cart.pop(name_item)
            lst_total.remove(total)
            print("Order cleared")
        elif choice == "4":
            print('-' * 30)
            print("your order is:")
            for item, info in cart.items():
                print('-' * 30)
                print(
                    f"Item: {item} {cart[item]['category']}\nQuantity: {cart[item]['quantity']} Units\nPrice: {cart[item]['price']} EGP")
                print('-' * 30)
                print(f"Item total: {cart[item]['total']} EGP")

            break
        else:
            print("Invalid option")
# -----------------------------------------------------------------------------------------------------------------

    elif number_item == "5":
        category5 = "Dessert"
        for i, name in enumerate(desserts):
            print(f"{i + 1}. {name}: {desserts[name]} EGP")

        choice_item = int(input("Please, Enter the number of the item you want (0 to return to the previous menu): "))
        if choice_item == 0:
            continue
        name_item = list(desserts.keys())[choice_item - 1]
        price = float(desserts[name_item])
        quantity = int(input("Please, Enter the quantity: "))
        # quantity_dic = cart.get(name_item, {}).get('quantity', 0) + 1
        total = quantity * price
        cart.update({name_item: {'quantity': quantity, 'price': price, 'category': category5, 'total': total}})
        lst_total.append(total)
        print("Added item successfully")
        print('-' * 30)
        # for item, info in cart.items():
        #     print(f"Name: {item}\nQuantity: {cart[item]['quantity']}\nPrice: {cart[item]['price']}")
        # line 30, 31 to if you want to print items on screen
        message2 = """1. Add another item
2. View the order
3. Clear the order
4. Exit """
        print(message2)
        choice = input("Please, Enter your choice: ")

        if choice == "1":
            continue
        elif choice == "2":
            print('-' * 30)
            print("your order is:")
            for name, info in cart.items():
                print('-' * 30)
                print(
                    f"Item: {name} {cart[name]['category']}\nQuantity: {cart[name]['quantity']} Units\nPrice: {cart[name]['price']} EGP")
                print('-' * 30)
                print(f"Item total: {cart[name]['total']} EGP")

            print('-' * 30)
            print(f"Total: {sum(lst_total):,} EGP")
        elif choice == "3":
            cart.pop(name_item)
            lst_total.remove(total)
            print("Order cleared")
        elif choice == "4":
            print('-' * 30)
            print("your order is:")
            for item, info in cart.items():
                print('-' * 30)
                print(f"Item: {item} {cart[item]['category']}\nQuantity: {cart[item]['quantity']} Units\nPrice: {cart[item]['price']} EGP")
                print('-' * 30)
                print(f"Item total: {cart[item]['total']} EGP")

            break
        else:
            print("Invalid option")
    else:
        print("Invalid Option")
        continue