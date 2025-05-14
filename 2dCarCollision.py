"""
Design a python simulator for 2d rectangle cars, they move in circles. Find time they first collide. 
You can assume the 2 cars are circles and the threshold for collision checking is the sum of the 2 radius of the circles, where the radius can be found using pythagoras on length and breadth of rectangles
"""

import math

class Car:
    def __init__(self, length, breadth, radius_path, angular_speed, initial_angle=0.0):
        self.length = length
        self.breadth = breadth
        self.radius_path = radius_path
        self.angular_speed = angular_speed  # radians per second
        self.initial_angle = initial_angle

        # Radius of circle that bounds the rectangle
        self.bounding_radius = math.hypot(length, breadth) / 2

    def position_at(self, t):
        angle = self.initial_angle + self.angular_speed * t
        x = self.radius_path * math.cos(angle)
        y = self.radius_path * math.sin(angle)
        return x, y

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def simulate_collision(car1, car2, dt=0.01, max_time=100):
    t = 0
    while t <= max_time:
        pos1 = car1.position_at(t)
        pos2 = car2.position_at(t)
        d = distance(pos1, pos2)
        if d <= (car1.bounding_radius + car2.bounding_radius):
            return t, pos1, pos2
        t += dt
    return None, None, None  # No collision within max_time

# Example usage
if __name__ == "__main__":
    car1 = Car(length=4, breadth=2, radius_path=10, angular_speed=0.5)
    car2 = Car(length=4, breadth=2, radius_path=10, angular_speed=0.6, initial_angle=math.pi / 2)

    collision_time, pos1, pos2 = simulate_collision(car1, car2)

    if collision_time is not None:
        print(f"Collision detected at time t = {collision_time:.2f} seconds.")
        print(f"Car1 position: {pos1}")
        print(f"Car2 position: {pos2}")
    else:
        print("No collision detected within simulation time.")
