#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    result_of_root = math.sqrt(a)
    return result_of_root


def square(a: float) -> float:
    result_of_square = math.pow(a, 2)
    return result_of_square


def average(a: float, b: float, c: float) -> float:
    result_of_average = (a+b+c)/3
    return result_of_average


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_total= math.radians(angle_degs+angle_mins/60+angle_secs/3600)
    return angle_total


def to_degrees(angle_rads: float) -> tuple:
    angle_degree = math.degrees(angle_rads)
    angle_minutes = (angle_degree-int(angle_degree))*60
    angle_secondes = (angle_minutes-int(angle_minutes))*60
    return int(angle_degree), int(angle_minutes), angle_secondes


def to_celsius(temperature: float) -> float:

    return (temperature-32)*5/9


def to_farenheit(temperature: float) -> float:
    return temperature*9/5+32


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
