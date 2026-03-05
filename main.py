from bacteria import Bacteria
from environment import Environment
from visualizer import Visualizer

bacteria = Bacteria()
environment = Environment()
visualizer = Visualizer()

systemOn = True
current_day = 1   # NEW: Track simulation day

print("\n" + "=" * 30 + "  Bacteria Simulator  " + "=" * 30 + "\n")

while systemOn:

    # Display Status
    print(" " * 26 + "="*30)
    print(" " * 26 + f"| Day              | {current_day:<7} |")
    print(" " * 26 + f"| Population       | {bacteria.population:<7} |")
    print(" " * 26 + "-"*30)
    print(" " * 26 + f"| Temperature      | {environment.temperature:>5}°C |")
    print(" " * 26 + f"| Humidity         | {environment.humidity:>6}% |")
    print(" " * 26 + f"| pH level         | {environment.pH_level:>7} |")
    print(" " * 26 + f"| Nutrients        | {environment.nutrients:>6}% |")
    print(" " * 26 + "=" * 30 + "\n")

    # Menu
    print("=" * 40)
    print("| Function                   |  Value  |")
    print("-" * 40)
    print("| Change temperature         |    1    |")
    print("| Change humidity            |    2    |")
    print("| Change pH level            |    3    |")
    print("| Change nutrients           |    4    |")
    print("| Skip time (days)           |    5    |")
    print("| Check statistics           |    6    |")
    print("| See statistical graph      |    7    |")
    print("| Exit simulation            |    8    |")
    print("=" * 40 + "\n")

    choice = input("Choose option: ")

    # -------------------------
    # OPTION HANDLING
    # -------------------------

    if choice == "1":
        environment.temperature = float(input("Enter new temperature (°C): "))
        print("\n"+"=" * 88)

    elif choice == "2":
        environment.humidity = float(input("Enter new humidity (%): "))
        print("\n" + "=" * 88)

    elif choice == "3":
        environment.pH_level = float(input("Enter new pH level: "))
        print("\n" + "=" * 88)

    elif choice == "4":
        environment.nutrients = float(input("Enter new nutrients level (0-10): "))
        print("\n" + "=" * 88)

    elif choice == "5":
        days = int(input("How many days to skip? "))

        for _ in range(days):
            bacteria.update(environment)
            current_day += 1

        print(f"\nTime skipped {days} days.")

    elif choice == "6":
        print("\n--- Statistics ---")
        print(f"Current Day: {current_day}")
        print(f"Population: {bacteria.population}")
        print(f"Birth rate: {bacteria.base_birth_rate}")
        print(f"Death rate: {bacteria.base_death_rate}")
        input("\nPress Enter to continue...")
        print("\n" + "=" * 88)

    elif choice == "7":
        type_of_graph = input("Choose graph (line, bar): ")
        if type_of_graph == "line" or type_of_graph == "bar":
            visualizer.create_graph(type_of_graph)
        else:
            print("Invalid option. Try again.")
            print("\n" + "=" * 88)

    elif choice == "8":
        print("Simulation ended.")
        systemOn = False

    else:
        print("Invalid option. Try again.")
        print("\n" + "=" * 88)
