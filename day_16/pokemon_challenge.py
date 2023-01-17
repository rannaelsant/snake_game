from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Chamander", "Bublesaurus"])
table.add_column("Type", ["Eletric", "Fire", "Vegetal"])
print(table)