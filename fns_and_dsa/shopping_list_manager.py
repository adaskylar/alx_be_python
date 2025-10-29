#!/usr/bin/env python3
"""
shopping_list_manager.py
Simple interactive shopping list manager using Python lists.
"""

def display_menu():
    print("Shopping List Manager")
    print("---------------------")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter item to add: ").strip()
    if not item:
        print("No item entered. Nothing added.")
        return
    shopping_list.append(item)
    print(f"Added: '{item}'")

def remove_item(shopping_list):
    if not shopping_list:
        print("Shopping list is empty — nothing to remove.")
        return

    print("Remove by: 1) name  2) index")
    method = input("Choose (1 or 2): ").strip()
    if method == '1':
        name = input("Enter item name to remove: ").strip()
        if not name:
            print("No name entered.")
            return
        # case-insensitive remove of first matching item
        for i, existing in enumerate(shopping_list):
            if existing.lower() == name.lower():
                removed = shopping_list.pop(i)
                print(f"Removed: '{removed}'")
                return
        print(f"Item '{name}' not found in the list.")
    elif method == '2':
        view_list(shopping_list)
        idx_str = input("Enter index number to remove (0, 1, ...): ").strip()
        if not idx_str.isdigit():
            print("Invalid index. Please enter a non-negative integer.")
            return
        idx = int(idx_str)
        if 0 <= idx < len(shopping_list):
            removed = shopping_list.pop(idx)
            print(f"Removed: '{removed}' (index {idx})")
        else:
            print("Index out of range.")
    else:
        print("Invalid choice. Returning to main menu.")

def view_list(shopping_list):
    if not shopping_list:
        print("Shopping list is empty.")
        return
    print("\nCurrent shopping list:")
    for i, item in enumerate(shopping_list):
        print(f"{i}. {item}")
    print(f"Total items: {len(shopping_list)}")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
