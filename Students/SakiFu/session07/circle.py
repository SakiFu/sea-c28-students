#!/usr/bin/env python
"""circle class --
fill this in so it will pass all the tests.
"""

import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def _set_diameter(self, diameter):
        self.radius = diameter / 2.0

    def _get_diameter(self):
        return self.radius * 2.0

    diameter = property(_get_diameter, _set_diameter)

    def _get_area(self):
        return self.radius ** 2 * math.pi

    area = property(_get_area)

    def __str__(self):
        return 'Circle with radius: %f' % (float(self.radius))

    def __repr__(self):
        return 'Circle(%d)' % (self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        return self.radius == other.radius
        return self.radius <= other.radius
        return self.radius >= other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.radius >= other.radius:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False

    def __le__(self, other):
        if self.radius <= other.radius:
            return True
        else:
            return False
