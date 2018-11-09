import json

import pygal

from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from country_codes import get_country_code


#Load data into a list
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

#Build dict of population data
cc_population = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country_name)
		if code:
			cc_population[code] = population

#Group countries in 3 population levels
cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc, pop in cc_population.items():
	if pop < 10000000:
		cc_pop_1[cc] = pop
	elif pop < 1000000000:
		cc_pop_2[cc] = pop
	else:
		cc_pop_3 = pop

wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World population in 2010, by country'
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)

wm.render_to_file('world_population.svg')
