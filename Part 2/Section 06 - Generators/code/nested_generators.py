start = 1
stop = 10

mult_gen = ((i * j for j in range(start, stop+1))
            for i in range(start, stop+1))

print([list(row) for row in mult_gen])
