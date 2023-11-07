class Expenditure:
    def __init__(self, name, amount, date, classification):
        self.name = name
        self.amount = amount
        self.date = date
        self.classification = classification


class ExpenditureTracker:
    def __init__(self, budget):
        self.budget = budget
        self.expenditures = []

    def add_expenditure(self, expenditure):
        self.expenditures.append(expenditure)

    def delete_expenditure(self, expenditure):
        self.expenditures.remove(expenditure)

    def edit_expenditure(self, old_expenditure, new_expenditure):
        index = self.expenditures.index(old_expenditure)
        self.expenditures[index] = new_expenditure

    def calculate_total_expenditure(self):
        return sum(expenditure.amount for expenditure in self.expenditures)

    def calculate_difference_vs_budget(self):
        total_expenditure = self.calculate_total_expenditure()
        return self.budget - total_expenditure


def main():
    print("                                     EXPENDITURE TRACKER                                                  ")
    print("Welcome! Earning money is hard enough. Tracking money shouldn't be. Use our expenditure tracker to create a budget and add expenditures to a running list. ")
    print("Classify expenditures based on various factors and at the end, compare the final amount to your target budget! All in one, simple program.")
    print()
    budget = int(input("Enter your monthly budget (in US Dollars): "))
    tracker = ExpenditureTracker(budget)

    while True:
        print("\nMenu:")
        print("1. Add Expenditure")
        print("2. Delete Expenditure")
        print("3. Edit Expenditure")
        print("4. View Expenditures")
        print("5. View Expenditures vs. Budget")
        print("6. Exit")
        print("7. Help")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name of the expenditure: ")
            amount = float(input("Enter the amount spent (in US Dollars): "))
            date = input("Enter the date of the expenditure: ")
            classification = input("Enter the expenditure classification: ")
            expenditure = Expenditure(name, amount, date, classification)
            tracker.add_expenditure(expenditure)
            print("Expenditure added successfully!")

        elif choice == "2":
            name = input("Enter the name of the expenditure to delete: ")
            for expenditure in tracker.expenditures:
                if expenditure.name == name:
                    option = input(f"Are you sure you want to delete {name}? Type Y or N: ")
                    if option == 'Y':
                      tracker.delete_expenditure(expenditure)
                      print("Expenditure deleted successfully!")
                    else:
                      break
                else:
                   print("Expenditure not found!")

        elif choice == "3":
            old_name = input("Enter the name of the expenditure to edit: ")
            for expenditure in tracker.expenditures:
                if expenditure.name == old_name:
                    new_name = input("Enter the new name of the expenditure: ")
                    new_amount = float(input("Enter the new amount spent (in US Dollars): "))
                    new_date = input("Enter the new date of the expenditure: ")
                    new_classification = input("Enter the new expenditure classification: ")
                    new_expenditure = Expenditure(new_name, new_amount, new_date, new_classification)
                    tracker.edit_expenditure(expenditure, new_expenditure)
                    print("Expenditure edited successfully!")
                    break
            else:
                print("Expenditure not found!")

        elif choice == "4":
            print("\nExpenditures:")
            for i, expenditure in enumerate(tracker.expenditures, start=1):
                print(
                    f"{i}. Name: {expenditure.name}, Amount: ${expenditure.amount}, Date: {expenditure.date}, Classification: {expenditure.classification}")

        elif choice == "5":
            total_expenditure = tracker.calculate_total_expenditure()
            difference_vs_budget = tracker.calculate_difference_vs_budget()
            print(f"Total Expenditure: ${total_expenditure}")
            print(f"Budget: ${budget}")
            print(f"Difference vs. Budget: ${difference_vs_budget}")

        elif choice == "6":
            print("Exiting Expenditure Tracker. Goodbye!")
            break

        elif choice == "7":
            print("\nHelp:")
            print("- To add an expenditure, choose option 1 and provide the required details.")
            print("- To delete an expenditure, choose option 2 and enter the name of the expenditure to delete.")
            print("- To edit an expenditure, choose option 3 and follow the prompts to update the details.")
            print("- To view all expenditures, choose option 4.")
            print("- To view expenditures vs. budget, choose option 5.")
            print("- To exit the expenditure tracker, choose option 6.")
            print("- To view the help menu again, choose option 7.")
            print("NOTE: Remember, do NOT include commas when entering numbers.")


        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
