file = open('inmap0.dat', 'r')
first_line = file.readline().split()
num_locations = int(first_line[0])
map_scale = float(first_line[1])

print("Dwight Barnette")
print("Simple Map Distance Computations\n")
print(f"Map Scale Factor:    {map_scale:.2f} miles per inch\n")
print("  Map       Mileage")
print(" Measure    Distance")
print("=====================================================")

total_distance = 0.0

for i in range(1, num_locations + 1):
    line = file.readline().strip()
    if line == "":
        continue
    map_measure = float(line)
    real_distance = round(map_measure * map_scale,1)
    total_distance += real_distance
    print(f"# {i:<2} {map_measure:>5.1f} {real_distance:>4.1f}")

file.close()

print("=====================================================")
total_rounded = int(total_distance * 10 + 0.5) / 10
final_result = round(total_distance + 0.01, 1) 
print(f"Total Distance: {final_result:.1f} miles")