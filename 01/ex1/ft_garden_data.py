#!/usr/bin/env python3
class Plant:
	def __init__(self, name: str, height: int, age: int) -> None:
		self.name = name
		self.height = height
		self.age = age

def	main():
	p1 = Plant("tulipe", 21, 60)
	p2 = Plant("tournesol", 34, 12)
	p3 = Plant("coquelicot", 5, 34)
	plants = [p1, p2 , p3]
	print("=== Garden Plant Registry ===")
	for plant in plants:
		print(f"{plant.name}: {plant.height}cm, {plant.age} days old")

if __name__ == "__main__":
	main()
