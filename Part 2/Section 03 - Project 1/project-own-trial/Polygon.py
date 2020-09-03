from math import sin, cos, pi
import numbers


class Polygon:
    def __init__(self, edges: int, circumradius: float):

        if not isinstance(edges, numbers.Real) or not isinstance(circumradius, numbers.Real):
            raise TypeError(
                'Both edges and circumradius value must be real numbers')

        if edges < 3:
            raise ValueError("Edges cannot be less than 3")
        self._edges = edges
        self._vertices = edges
        self._circumradius = circumradius
        self._interior_angle = (edges-2) * (180/edges)
        self._edge_length = 2 * circumradius * sin(pi/edges)
        self._apothem = circumradius * cos(pi/edges)
        self._area = 0.5 * self._edges * self._edge_length * self._apothem
        self._perimeter = self._edges * self._edge_length

    @property
    def edges(self):
        return self._edges

    @property
    def vertices(self):
        return self._vertices

    @property
    def interior_angle(self):
        return self._interior_angle

    @property
    def edge_length(self):
        return self._edge_length

    @property
    def apothem(self):
        return self._apothem

    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter

    def __repr__(self):
        return f'Polygon(edges={self.edges}, edge_length = {self._edge_length}, angle={self._interior_angle},apothem={self._apothem})'

    def __eq__(self, other):
        if not isinstance(other, Polygon):
            raise TypeError("Only polygons can be compared")
        return (self._vertices == other._vertices) and (self._circumradius == other._circumradius)

    def __gt__(self, other):
        if not isinstance(other, Polygon):
            raise TypeError("Only polygons can be compared")
        return (self._vertices > other._vertices)


class Polygons:
    def __init__(self, max_vertices: int, circumradius: float):

        if not isinstance(max_vertices, numbers.Real) or not isinstance(circumradius, numbers.Real):
            raise TypeError(
                'Both edges and circumradius value must be real numbers')

        if max_vertices < 3:
            raise ValueError("Edges cannot be less than 3")

        self._max_vertices = max_vertices
        self._circumradius = circumradius
        self._polygons = [Polygon(i, circumradius)
                          for i in range(3, max_vertices+1)]

    @property
    def maxefficiencyp(self) -> Polygon:
        sorted_eff_ratios = sorted(self._polygons, key=Polygons.rank_function)
        return sorted_eff_ratios[-1]

    @staticmethod
    def rank_function(polygon: Polygon):
        return polygon.area/polygon.perimeter

    def __getitem__(self, s):
        return self._polygons[s]

    def __len__(self):
        return len(self._polygons)



