import matplotlib.pyplot as plt


class Population:
    def __init__(self, initial_population: int, growth_rate: float):
        self._population = initial_population
        self._growth_rate = growth_rate

    @property
    def population(self):
        return self._population

    @property
    def growth_rate(self):
        return self._growth_rate

    def grow(self, amount: float):
        self._population += amount

    def decrease(self, amount: float):
        self._population -= amount
        self._population = max(0, self._population)


def simulate_ecosystem(prey, predator, predator_efficiency, time_steps):
    """Simulate the ecosystem dynamics over the specified number of time steps."""
    prey_population_history = [prey.population]
    predator_population_history = [predator.population]

    for _ in range(time_steps):
        prey_growth = prey.growth_rate * prey.population
        prey_loss_to_predator = predator_efficiency * \
            predator.population * prey.population

        predator_growth = predator.growth_rate * prey_loss_to_predator
        predator_loss = predator.growth_rate * predator.population

        prey.grow(prey_growth)
        predator.grow(predator_growth)

        prey.decrease(prey_loss_to_predator)
        predator.decrease(predator_loss)

        prey_population_history.append(prey.population)
        predator_population_history.append(predator.population)

    return prey_population_history, predator_population_history


def plot_population_dynamics(time_steps: int, prey_history: list, predator_history: list, config: dict):
    """Plot the prey and predator population dynamics over time with the given configuration."""
    time = range(time_steps + 1)
    plt.plot(time, prey_history, label="Prey Population")
    plt.plot(time, predator_history, label="Predator Population")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.legend()
    plt.title("Predator-Prey Population Dynamics")

    # Adding configuration information as a footnote
    footnote = f"Prey Initial Population: {config['prey_population']}, Growth Rate: {config['prey_growth_rate']}\n"
    footnote += f"Predator Initial Population: {config['predator_population']}, Growth Rate: {config['predator_growth_rate']}\n"
    footnote += f"Predator Efficiency: {config['predator_efficiency']}"

    # Get the y-axis limit and adjust the position of the footnote
    _, ymax = plt.ylim()
    plt.text(350, -0.35 * ymax, footnote, ha="center", fontsize=8)

    plt.tight_layout()
    plt.show()


def main():
    config = {
        "prey_population": 5000,
        "predator_population": 200,
        "prey_growth_rate": 0.015,
        "predator_growth_rate": 0.002,
        "predator_efficiency": 0.00002,
    }

    time_steps = 700

    prey = Population(config["prey_population"], config["prey_growth_rate"])
    predator = Population(
        config["predator_population"], config["predator_growth_rate"])

    prey_history, predator_history = simulate_ecosystem(
        prey, predator, config["predator_efficiency"], time_steps
    )

    plot_population_dynamics(time_steps, prey_history,
                             predator_history, config)


if __name__ == "__main__":
    main()
