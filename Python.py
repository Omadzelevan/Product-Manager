import math
import random
import json

def save_to_json(data, filename='Data.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def add_products():
    while True:
        product_name = input('Product Name: ')
        product_count = input('Product Count: ')
        product_price = input('Product Price: ')
        product_category = input('Product Category: ')
        new_products = {"name":"",
                    "count":"",
                    "price":"" ,
                    "category":"" }
        try:
         with open('Data.json', 'r') as file:
            data = json.load(file)
        except FileNotFoundError:
            data = []
        new_products['name'] = product_name
        new_products['count'] = product_count
        new_products['price'] = product_price
        new_products['category'] = product_category
        data.append(new_products)
        save_to_json(data)
        print('Product added successfully!')
        choice_one = input('Do you want to add another product? (y/n): ')
        if choice_one.lower() == 'y':
            continue
        else:
            break
        

def remove_products():
    while True:
        try:
            with open('Data.json', 'r') as file:
                data = json.load(file)
            if isinstance(data, list):
                product_names = [product["name"] for product in data if "name" in product]
                print("Product Names:")
                print("\n".join(product_names))
                product_to_remove = input("Enter the product name to remove (enter c to cancel): ")
            if product_to_remove.lower() == 'c':
                main_menu()
            else:
                break
                
                
            product_found = False
            for product in data:
                if product.get("name") == product_to_remove:
                    data.remove(product)
                    product_found = True
                    break
            if product_found:
                save_to_json(data)
                print(f'Product "{product_to_remove}" removed successfully!')
            else:
                product_to_remove = input("Enter correct product name to remove: ")
                continue
        except FileNotFoundError:
            print("No products found in the JSON file!")
            break
def main_menu():
        while True:
            print("\nMain Menu:")
            print("1 - Add Products")
            print("2 - Remove Products")
            print("3 - Exit")
        
            options = input("Choose an operation: ").strip()
        
            if options == '1':
                add_products()
            elif options == '2':
                remove_products()
            elif options == '3':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    
if __name__ == "__main__":
    main_menu()
    