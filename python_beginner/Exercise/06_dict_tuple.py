from os import remove

population = {
    "china": 143.2,
    "india": 136,
    "USA": 32,
    "Pakistan": 21
}

# print(type(population))
func = input("Enter your input: ")
###########################################\
if func == "print":
    for k, v in population.items():
        print(k,"==>", v)
###########################################
elif func == "add":
    country = input("Enter new country: ")
    country = country.lower()
    if country in population:
        print(f"{country} already exists.")
    else:
        ppl = float(input("Enter population: "))
        # population.update({country:ppl})
        population[country]= ppl
############################################
elif func == "remove":
    country = input("Enter new country: ")
    country = country.lower()
    if country not in population:
        print(f"{country} doesn't exist.")
    else:
        del population[country]
###########################################
elif func == "query":
    query = input("Enter your query: ")
    query = query.lower()
    if query not in population:
        print(f"{query} doesn't exist.")
    else:
        print(f"Population of {query} is {population[query]}")
print(population)
