#!/usr/bin/env python3
class Plant:
	def __init__(self, name: str, height: int, age_days: int) -> None:
		self.name = name
		self.height = height
		self.age_days = age_days
	def grow(self):
		self.height = self.height + 1
	def age(self):
		self.age_days = self.age_days + 1
	def get_info(self):
		return (f"{self.name}: {self.height}cm, {self.age_days} days old")


def main():
	p1 = Plant("Tulipe", 23, 12)
	p2 = Plant("tournesol", 34, 12)
	p3 = Plant("coquelicot", 5, 34)
	plants = [p1,p2,p3]
	start = p1.height
	print("\n=== Day 1 ===")
	for plant in plants:
		print(plant.get_info())
	for days in range(6):
		for plant in plants:
			plant.grow()
			plant.age()
	print("\n=== Day 7 ===")
	for plant in plants:
		print(plant.get_info())
	growth = p1.height - start
	print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
	main()
