genome = input()
a = genome.lower() # a.lower()-привод символа к нижнему регистру
print(((a.count('g')+a.count('c'))/len(genome))*100)

