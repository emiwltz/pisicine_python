#!/usr/bin/env python3
class Plant:
	def __init__(self, name: str, height: int, age: int) -> None:
		self.name = name
		self.height = height
		self.age = age

class Garden:
	def __init__(self, name:str, size: int) -> None:
		self.plants: list[Plant] = []
		self.name = name
		self.size = size
	def add(self, plant: Plant) -> None:
        self.plants.append(plant)

    def display(self) -> None:
        for i in range(len(self.plants)):
            p = self.plants[i]
            print(p.name)

def	main():
	p1 = Plant("tulipe", 21, 60)
	p2 = Plant("tournesol", 34, 12)
	p3 = Plant("coquelicot", 5, 34)
	print(p1.name)

if __name__ == "__main__":
	main()
