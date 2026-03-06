# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ewaltz <ewaltz@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/06 13:06:18 by ewaltz            #+#    #+#              #
#    Updated: 2026/03/06 13:08:11 by ewaltz           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

class GardenManager:
    def __init__(self, action_to_do: str):

        def GardenStat


class Garden:
    def __init__(self, name: str, plants: list)


class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.type = "Undefined"

    def grow(self):
        self.height += 1
        self.days += 1


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, days: int, color: str) -> None:
        super().__init__(name, height, days)
        self.color = color

        if self.days > 7:
            self.blooming = True
        else:
            self.blooming = False


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, days: int, color: str) -> None:
        super().__init__(name, height, days, color)
        self.prize = self.height * self.days


def main():


if __name__ == "__main__":
    main()
