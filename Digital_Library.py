#Digitalisation of Library Services
import os

class Librarian:
    def __init__(self, library_system):
        self.library_system = library_system

    def organize_books(self):
        # Logic to organize books on shelves
        pass

    def manage_borrowing(self, member_id, book_id):
        # Logic to handle book borrowing
        pass

    def manage_returns(self, member_id, book_id):
        # Logic to handle book returns
        pass

    def check_reservations(self, book_id):
        # Logic to check reservation queues for a book
        pass

    def notify_member(self, member_id, book_id):
        # Logic to notify members when reserved books are available
        pass

    def assist_member(self, member_id):
        # Logic to assist members with borrowing procedures and account questions
        pass

    def update_book_records(self, book_id, status):
        # Logic to ensure book records are accurate and up to date
        pass


class Librarian_Assistant:
        def __init__(self, library_system):
            self.library_system = library_system

        def shelve_books(self, book_id):
            # Logic to shelve returned books
            pass

        def update_catalog(self, book_info):
            # Logic to update the catalog with new books
            pass

        def assist_members(self, member_id, query):
            # Logic to assist members with basic questions
            pass

        def support_librarian(self):
            # Logic to support the Librarian during busy periods
            pass

        def maintain_records(self, book_id, status):
            # Logic to ensure physical and digital records are consistent
            pass

class Administrator:
    def __init__(self, library_system):
        self.library_system = library_system
    
    def manage_user_accounts(self, user_id, action):
        # Logic to create, update, or delete user accounts
        pass

    def compliance_monitoring(self):
        # Logic to ensure the library complies with legal and ethical standards
        pass

    def library_policy_enforcement(self):
        # Logic to enforce library policies and procedures
        pass

    def system_performance_monitoring(self):
        # Logic to monitor the performance of the library management system
        pass

class Members:
    def __init__(self, library_system):
        self.library_system = library_system

    def search_catalog(self, search_query):
        # Logic to search the library catalog
        pass

    def borrow_book(self, book_id):
        # Logic to borrow a book
        pass

    def return_book(self, book_id):
        # Logic to return a borrowed book
        pass

    def reserve_book(self, book_id):
        # Logic to reserve a book
        pass

    def view_account(self):
        # Logic to view member account details
        pass

    def pay_fines(self, amount):
        # Logic to pay overdue fines
        pass


def main():
    if not os.path.exists(LOG_FILE):
        log_action("--- Welcome to the Digital Library System ---")

    while True:
        print("\n" + "="*30)
        print("    Welcome to the Digital Library System")
        print("="*30)
        print("1. Speak to Librarian")
        print("2. Speak to Librarian Assistant")
        print("3. Speak to Administrator")
        print("4. I am a Member")
        print("5. Exit the digital library system")
        
        choice = input("Select an option: ")

        if choice == '1':
            # 
            print("\n--- Ship Information ---")
            s_name = input("Ship Name: ")
            s_x = float(input("Current X (0-100): "))
            s_y = float(input("Current Y (0-100): "))
            s_fuel = float(input("Fuel Amount: "))
            
            ship = Spaceship(s_name, s_x, s_y, s_fuel)
            active_ships.append(ship)

            print("\nSearching for reachable planets...")
            possible_landings = []

            for p in planets:
                possible, cost = ship.can_land(p)
                if possible:
                    dist = ship.calculate_distance(p)
                    possible_landings.append((p, dist, cost))

            if possible_landings:
                # Trier par distance la plus courte
                possible_landings.sort(key=lambda x: x[1])
                best_p, best_d, best_c = possible_landings[0]
                
                result = f"SUCCESS: {ship.name} can land on {best_p.name} (Dist: {best_d:.2f}, Cost: {best_c:.2f})"
                print(result)
                log_action(result)
            else:
                result = f"FAILURE: {ship.name} has insufficient fuel for any planet."
                print(result)
                log_action(result)

        elif choice == '2':
            print("\n--- Active Ships ---")
            if not active_ships:
                print("No ships currently in space.")
            for s in active_ships:
                print(f"Ship: {s.name} | Fuel: {s.fuel} | Pos: ({s.x}, {s.y})")

        elif choice == '3':
            print("\n--- Active Ships ---")
            if not active_ships:
                print("No ships currently in space.")
            for s in active_ships:
                print(f"Ship: {s.name} | Fuel: {s.fuel} | Pos: ({s.x}, {s.y})")

        elif choice == '4':
            print("\n--- Active Ships ---")
            if not active_ships:
                print("No ships currently in space.")
            for s in active_ships:
                print(f"Ship: {s.name} | Fuel: {s.fuel} | Pos: ({s.x}, {s.y})")

        elif choice == '5':
            print("Shutting down systems...")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()