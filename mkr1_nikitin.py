def read_population_data(file_name):
    population_data = {}
    with open(file_name, 'r') as file:
        for line in file:
            country, year, population = line.strip().split(',')
            if country not in population_data:
                population_data[country] = []
            population_data[country].append((int(year), int(population)))
    return population_data

def calculate_population_change(population_data):
    changes = []
    for country, data in population_data.items():
        for i in range(1, len(data)):
            year, population = data[i]
            prev_year, prev_population = data[i - 1]
            change = "+" if population > prev_population else "-"
            changes.append((country, year, change))
    return changes

def main():
    file_name = "population.txt"
    population_data = read_population_data(file_name)
    changes = calculate_population_change(population_data)
    for change in changes:
        print("{}, {}, population size {}".format(change[0], change[1], change[2]))

if __name__ == "__main__":
    main()
