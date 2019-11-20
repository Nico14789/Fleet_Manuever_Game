import Fleet
import Coordinate
import Playfield
import Player
import Ship
import random
#   import numpy

board_size = Coordinate.Coordinate
board_size.x = 10
board_size.y = 10
fleet_class = Fleet.Fleet()
TestFleet_Test = fleet_class.create_fleet(board_size, 4468415)
print("Test")

TestShip = TestFleet_Test[1]
TestShip_Type = TestShip.get_ship_type()
print(TestShip_Type)


Player_1 = Player.Player(board_size, 1)
Player_2 = Player.Player(board_size, 2)


TestPlayfield = Playfield.Playfield(board_size)

TestValue = TestPlayfield.get_position_value(board_size)
print(TestValue)

status = "ship"
TestPlayfield.set_position_value(board_size, status)

status = "water"
board_size.x = 2
TestPlayfield.set_position_value(board_size, status)

board_size.x = 9
TestValue = TestPlayfield.get_position_value(board_size)
print(TestValue)

TestPlayfield.draw_playfield()
TestPlayfield.draw_playfield_2()

input("Press enter to exit !")


class FleetManeuverGame:

    def __init__(self):
        """"""
        """"""
