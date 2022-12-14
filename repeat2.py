import matplotlib.pyplot as plt

area = 2.3 # m**2
force = [2.0, 6.0, 9.0, 10.0, 13.5] # N (Newton)
for force_val in force:
	pressure = force_val/area
	print("A force of {0:.2f} N on an area of {1:.2f} m**2 will exert a pressure of {2:.2f} Pa".format(force_val, area, pressure))
	
area = 2.5 # m**2
force = [2.0, 4.0, 8.3, 10.1, 11.5] # N (Newton)
for counter in range(len(force)):
	pressure = force[counter]/area
	print("A force of {0:.2f} N on an area of {1:.2f} m**2 will exert a pressure of {2:.2f} Pa".format(force[counter], area, pressure))

area = [2.5, 2.4, 2.3, 2.2, 2.1] # m**2
force = [2.0, 4.0, 8.3, 10.1, 11.5] # N (Newton)
for counter, force_val in enumerate(force):
	print(counter)
	print(force_val)

print("Area    Force    Pressure")
print("====    =====    ========")
for counter, force_val in enumerate(force):
	pressure = force_val/area[counter]
	print("{0:<4.2f}    {1:<5.2f}    {2:<.2f}".format(area[counter], force_val, pressure))

print("Area    Force    Pressure")
print("====    =====    ========")
for a, f in zip(area, force):
	pressure = f/a
	print("{0:<4.2f}    {1:<5.2f}    {2:<.2f}".format(a, f, pressure))

print("Area    Force    Pressure")
print("====    =====    ========")
pressure = []
for i in range(len(force)):
	pressure.append(force[i]/area[i])
	print("{0:<4.2f}    {1:<5.2f}    {2:<.2f}".format(area[i], force[i], pressure[-1]))

plt.figure(figsize=(10, 6))
plt.plot(force, pressure, '-k', linewidth=3)
plt.scatter(force, pressure, s=50, marker='s', c='r')
plt.xlabel("Force (N)", fontsize=12, weight='bold')
plt.ylabel("Pressure (Pa)", fontsize=12, weight='bold')
plt.title("Plot of Pressure vs Force", fontsize=14, weight='bold')
plt.xticks(fontsize=12, weight='bold')
plt.yticks(fontsize=12, weight='bold')
plt.grid()
plt.show()
