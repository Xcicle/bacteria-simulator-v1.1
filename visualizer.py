import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self):
        pass

    def create_graph(self, graph_type):

        # Read population data
        with open("population.txt", "r") as file:
            populations = [int(line.strip()) for line in file if line.strip()]

        # Get last 20 days
        last_pop = populations[-20:]

        # Generate day numbers
        start_day = len(populations) - len(last_pop) + 1
        days = list(range(start_day, start_day + len(last_pop)))

        plt.figure()
        plt.ylim(0,5000)

        if graph_type == "line":
            plt.plot(days, last_pop, marker="o")

        elif graph_type == "bar":
            plt.bar(days, last_pop)

        plt.title("Bacteria Population (Last 20 Days)")
        plt.xlabel("Day")
        plt.ylabel("Population")

        plt.grid(True)

        plt.show()