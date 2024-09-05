from rental_system import RentalSystem


def main():
    rental_system = RentalSystem()
    
    while True:
        print("""
                    -----------------------------------------------
                    |                                             | 
                    |    Welcome to Chandroy Equipment Rentals    |
                    |                                             |
                    -----------------------------------------------
                    """);

        print("Choices:\nPress (1) to rent.\nPress (2) to return.\nPress (3) to exit.\n")
        
        choice = input("Enter your choice:")
        try:
            if choice == "1":
                
                customer_name = input("Enter customer name: ")
                
                print("\nAvailable Equipment:")
                first="{0}{1:>15}{2:>37}{3:>25}{4:>28}".format("SN","Name","Brand","Price","Quantity");
                second="{0}{1:>23}{2:>26}{3:>26}{4:>27}".format(1,"Velvet Table Cloth","Saathi","$8",20);
                third="{0}{1:>19}{2:>39}{3:>19}{4:>25}".format(2,"Microphone Set","Audio Technicia","$189",15);
                fourth="{0}{1:>20}{2:>29}{3:>28}{4:>25}".format(3,"Disco Light Set","Sonoff","$322",24);
                fifth="{0}{1:>35}{2:>13}{3:>29}{4:>25}".format(4,"7.1 Surround Sound Speaker Set","Dolby","$489",4);
                sixth="{0}{1:>21}{2:>38}{3:>18}{4:>25}".format(5,"Dinner Table 8*5","Panda Furnitures","$344",8);
                print(first)
                print("-------------------------------------------------------------------------------------------------------------")
                print(second)
                print(third)
                print(fourth)
                print(fifth)
                print(sixth)
                
                equipment_name = input("\nEnter equipment name: ")
                quantity = int(input("Enter quantity: "))
                rental_system.rent_equipment(customer_name, equipment_name, quantity)
                print("\nEquipment rented successfully.")
            
            elif choice == "2":
                customer_name = input("Enter customer name: ")
                print("\nAvailable Equipment:")
                first="{0}{1:>15}{2:>37}{3:>25}{4:>28}".format("SN","Name","Brand","Price","Quantity");
                second="{0}{1:>23}{2:>26}{3:>26}{4:>27}".format(1,"Velvet Table Cloth","Saathi","$8",20);
                third="{0}{1:>19}{2:>39}{3:>19}{4:>25}".format(2,"Microphone Set","Audio Technicia","$189",15);
                fourth="{0}{1:>20}{2:>29}{3:>28}{4:>25}".format(3,"Disco Light Set","Sonoff","$322",24);
                fifth="{0}{1:>35}{2:>13}{3:>29}{4:>25}".format(4,"7.1 Surround Sound Speaker Set","Dolby","$489",4);
                sixth="{0}{1:>21}{2:>38}{3:>18}{4:>25}".format(5,"Dinner Table 8*5","Panda Furnitures","$344",8);
                print(first)
                print("-------------------------------------------------------------------------------------------------------------")
                print(second)
                print(third)
                print(fourth)
                print(fifth)
                print(sixth)
                
                equipment_name = input("\nEnter equipment name: ")
                rental_system.return_equipment(customer_name, equipment_name)
                print("\nEquipment returned successfully.")
            
            elif choice == "3":
                print("You have exited from the rental system.")
                break
        except ValueError as ve:
            print(ve)
            
        except Exception as e:
            print("An error occured:", e)

        print("\nAvailable equipment:")
        for equipment in rental_system.equipment_list:
            print(f"{equipment.name}: {equipment.quantity}")

if __name__ == "__main__":
    main()
