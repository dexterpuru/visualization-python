from random import choice


class RandomWalk():
	def __init__(self, num_points=5000):
		self.num_points = num_points

		#All walks start at [0,0]
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		#Keep taking steps until the walk reaches the desired length
		while len(self.x_values) < self.num_points:
			#Decide which dxn to go and how far to go
			x_dxn = choice([1, -1])
			x_dis = choice([0, 1, 2, 3, 4])
			x_step = x_dxn * x_dis

			y_dxn = choice([1, -1])
			y_dis = choice([0, 1, 2, 3, 4])
			y_step = y_dxn * y_dis

			#Reject moves to go nowhere
			if x_step == 0 and y_step == 0:
				continue

			#Calculate next x and y values
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)
