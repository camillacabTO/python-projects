import os
import shutil
from pathlib import Path
import platform
import time


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def get_recipe_categories():
    return [category.name for category in Path("Recipes").iterdir() if category.is_dir()]


def display_menu():
    print("Welcome to the RecipeVault!")
    print(f"Path to the directory: {Path('Recipes').resolve()}")
    print(f"Number of recipes: {len(get_recipe_categories())}\n")

    print("Please choose an option:")
    print("1. Read a recipe")
    print("2. Create a new recipe")
    print("3. Create a new category")
    print("4. Delete a recipe")
    print("5. Delete a category")
    print("6. Exit the program")


def read_recipe():
    categories = get_recipe_categories()
    print("Categories:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    try:
        category_choice = int(input("Which category do you choose? ")) - 1
        selected_category = categories[category_choice]
    except IndexError:
        print("\nInvalid category choice. Please try again.")
        return

    recipes = list(Path(f"Recipes/{selected_category}").glob("*.txt"))
    print("\nRecipes:")
    for index, recipe in enumerate(recipes, start=1):
        print(f"{index}. {recipe.stem}")

    try:
        recipe_choice = int(input("Which recipe do you want to read? ")) - 1
        selected_recipe = recipes[recipe_choice]
    except IndexError:
        print("\nInvalid recipe choice. Please try again.")
        return

    with open(selected_recipe, "r") as file:
        print("\n" + file.read())


def create_recipe():
    categories = get_recipe_categories()
    print("Categories:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    category_choice = int(input("Which category do you choose? ")) - 1
    selected_category = categories[category_choice]

    recipe_name = input("Enter the name of the new recipe: ").strip()
    recipe_content = input("Enter the content of the recipe: ").strip()

    with open(f"Recipes/{selected_category}/{recipe_name}.txt", "w") as file:
        file.write(recipe_content)

    print(f"\n{recipe_name}.txt has been created in the {selected_category} category.")


def create_category():
    category_name = input("Enter the name of the new category: ").strip()
    os.makedirs(f"Recipes/{category_name}")
    print(f"\nCategory '{category_name}' has been created.")


def delete_recipe():
    categories = get_recipe_categories()
    print("Categories:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    try:
        category_choice = int(input("Which category do you choose? ")) - 1
        selected_category = categories[category_choice]
    except IndexError:
        print("\nInvalid category choice. Please try again.")
        return

    recipes = list(Path(f"Recipes/{selected_category}").glob("*.txt"))
    print("\nRecipes:")
    for index, recipe in enumerate(recipes, start=1):
        print(f"{index}. {recipe.stem}")

    try:
        recipe_choice = int(input("Which recipe do you want to delete? ")) - 1
        selected_recipe = recipes[recipe_choice]
    except IndexError:
        print("\nInvalid recipe choice. Please try again.")
        return

    os.remove(selected_recipe)
    print(f"\n{selected_recipe.name} has been deleted.")


def delete_category():
    categories = get_recipe_categories()
    print("Categories:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    try:
        category_choice = int(input("Which category do you want to delete? ")) - 1
        selected_category = categories[category_choice]
    except IndexError:
        print("\nInvalid category choice. Please try again.")
        return

    confirmation = input(f"Are you sure you want to delete the '{selected_category}' category? (y/n) ").lower()
    if confirmation == 'y':
        shutil.rmtree(f"Recipes/{selected_category}")
        print(f"\nCategory '{selected_category}' has been deleted.")
    else:
        print("\nCategory deletion canceled.")


def main():
    while True:
        clear_screen()
        display_menu()
        user_choice = int(input("\nEnter your choice: "))

        if user_choice == 1:
            read_recipe()
        elif user_choice == 2:
            create_recipe()
        elif user_choice == 3:
            create_category()
        elif user_choice == 4:
            delete_recipe()
        elif user_choice == 5:
            delete_category()
        elif user_choice == 6:
            print("\nThank you for using the Recipe Manager!")
            time.sleep(2)
            clear_screen()
            break
        else:
            print("\nInvalid choice. Please try again.")
            time.sleep(2)

        input("\nPress any key to continue...")


if __name__ == "__main__":
    main()
