import matplotlib.pyplot as plotter

def collatz(number):
	sequence = [number]
	while 1 not in sequence:
		if number % 2 == 0:
			number //= 2
		else:
			number = (number * 3) + 1
		sequence.append(number)
	return sequence

def graph(y_axis, graph_type):
	x_axis = list(range(len(y_axis)))
	if graph_type == "scatter":
		plotter.scatter(x_axis, y_axis, s = 10)
	else:
		plotter.plot(x_axis, y_axis)
	plotter.xlabel("Number of iterations")
	plotter.ylabel("Size of iteration")
	plotter.title(f"Collatz conjecture with {y_axis[0]} as input")
	plotter.show()

def disprove(sequence):
	for item in sequence:
		if sequence.count(item) > 1:
			return True

if __name__ == "__main__":
	sequence = collatz(int(float(input("Enter a number: "))))

	if disprove(sequence):
		print("You have disproved the Collatz conjecture!")

	plot_response = input("Line or scatter graph: ").lower()
	graph(sequence, "scatter") if "scatter" in plot_response else graph(sequence, None)
