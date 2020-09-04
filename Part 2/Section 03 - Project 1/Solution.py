import math


class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least three sides')
        self._n = n
        self._R = R

    def __repr__(self):
        return f'Polygon(n={self._n},R={self._R})'

    @property
    def count_vertices(self):
        return self._n

    @property
    def count_edges(self):
        return self._n

    @property
    def circumradius(self):
        return self._R

    @property
    def interior_angle(self):
        return (self._n - 2) * 180/self._n

    @property
    def side_length(self):
        return 2 * self._R * math.sin(math.pi/self._n)

    @property
    def apothem(self):
        return self._R * math.cos(math.pi/self._n)

    @property
    def area(self):
        return 0.5 * self._n * self.side_length * self.apothem

    @property
    def perimeter(self):
        return self._n * self.side_length

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("Only polygons can be compared")
        return (self.count_edges == other.count_edges) and (self.circumradius == other.circumradius)

    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("Only polygons can be compared")
        return self.count_vertices > other.count_vertices
