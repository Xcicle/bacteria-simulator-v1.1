class Bacteria:

    def __init__(self):
        self.population = 1000

        with open('population.txt',mode='w') as f:
            f.write(str(self.population))

        self.base_birth_rate = 0.05
        self.base_death_rate = 0.01

    def update(self, environment):

        births = self.calculate_births(environment)
        deaths = self.calculate_deaths(environment)

        self.population = max(0, int(self.population + births - deaths))

        with open('population.txt',mode='a') as f:
            f.write('\n'+str(self.population))

    def calculate_births(self, env):

        birth_modifier = 1
        # -------------------- # TEMPERATURE EFFECT # --------------------
        temp = env.temperature
        if 35 <= temp <= 39:  # Optimal
            birth_modifier *= 1.3
        elif 30 <= temp < 35 or 39 < temp <= 42:  # Stress
            birth_modifier *= 0.6
        else:  # Lethal
            birth_modifier *= 0.1
        # -------------------- # pH EFFECT # --------------------
        ph = env.pH_level
        ph_diff = abs(ph - 7)
        if ph_diff <= 1:  #
            Optimal
            birth_modifier *= 1.2
        elif ph_diff <= 3:  # Stress
            birth_modifier *= 0.5
        else:  # Lethal
            birth_modifier *= 0.05
        # -------------------- # HUMIDITY EFFECT # --------------------
        humidity = env.humidity
        if 40 <= humidity <= 70:
            birth_modifier *= 1.1
        elif 25 <= humidity < 40:
            birth_modifier *= 0.7
        else:
            birth_modifier *= 0.3
        # -------------------- # NUTRIENTS EFFECT # --------------------
        nutrients = env.nutrients
        if nutrients >= 7:
            birth_modifier *= 1.2
        elif 3 <= nutrients < 7:
            birth_modifier *= 0.7
        else:
            birth_modifier *= 0.2
        # Logistic Growth Limit
        carrying_capacity = 5000
        logistic_factor = 1 - (self.population / carrying_capacity)
        return self.population * self.base_birth_rate * birth_modifier * logistic_factor

    def calculate_deaths(self, env):

        death_modifier = 1
        deaths = self.population * self.base_death_rate

        # --------------------
        # TEMPERATURE EFFECT
        # --------------------
        temp = env.temperature
        optimal_low = 35
        optimal_high = 39

        if temp < optimal_low:
            diff = optimal_low - temp
        elif temp > optimal_high:
            diff = temp - optimal_high
        else:
            diff = 0

        death_modifier += (diff / 5) * 0.5

        # --------------------
        # pH EFFECT
        # --------------------
        ph = env.pH_level
        ph_diff = abs(ph - 7)

        # every 1 pH away adds stress
        death_modifier += ph_diff * 0.4

        # extreme pH still very dangerous
        if ph <= 2 or ph >= 12:
            death_modifier += 3

        # --------------------
        # HUMIDITY EFFECT
        # --------------------
        humidity = env.humidity
        optimal_low = 40
        optimal_high = 70

        if humidity < optimal_low:
            diff = optimal_low - humidity
        elif humidity > optimal_high:
            diff = humidity - optimal_high
        else:
            diff = 0

        # every 10% away increases deaths
        death_modifier += (diff / 10) * 0.3

        # --------------------
        # NUTRIENTS EFFECT
        # --------------------
        nutrients = env.nutrients

        # ideal nutrients = 8
        nutrient_diff = abs(nutrients - 8)

        death_modifier += nutrient_diff * 0.35

        # --------------------
        # Waste buildup (overcrowding stress)
        # --------------------
        waste_level = (self.population / 8000)
        death_modifier += waste_level

        return deaths * death_modifier