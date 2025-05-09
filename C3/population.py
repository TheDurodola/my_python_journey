growth_rate = 0.032
world_population = 8_221_811_602

print(f"Year		Population")
for repeat in range(1,101):
	population_increment =0
	if repeat>1: population_increment= world_population*growth_rate
	world_population = world_population + population_increment
	
	print(f"{repeat}		{world_population}")
