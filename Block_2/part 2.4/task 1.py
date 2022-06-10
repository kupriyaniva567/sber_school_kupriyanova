genome = input()
a = genome.lower() # привод символа к нижнему регистру
print(((a.count('g')+a.count('c'))/len(genome))*100)

