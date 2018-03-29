# -*- coding: utf-8 -*-

r"""Modeling of forces and systems of forces

References
----------
http://civile.utcb.ro/cmsdc/mechanics.pdf
http://ocw.nthu.edu.tw/ocw/upload/43/716/static_ch3.pdf

"""

import numpy as np


class Force(object):
    """A force represented by a vector (force parameter) 
    acting at a given position (position parameter)

    Parameters
    ----------
    force : list of 3 floats, optional (default : [0., 0., 0.])
        Represents the x, y, z components of the force vector.
    position : list of 3 floats,  optional (default : [0., 0., 0.])
        Represents the x, y, z coordinates of the force point of application.
    name : string, optional (default : None)
        A name given to the force.

    """

    def __init__(self, force=None, position=None, name=None):
        if force is None:
            self.force = [0., 0., 0.]
        else:
            if len(force) != 3:
                msg = "A Force object vector should be initialized " \
                      "with a list of length == 3"
                raise ValueError(msg)
            else:  # len(force) == 3
                # raises ValueError if cast impossible
                self.force = [float(force[0]), float(force[1]), float(force[2])]

        if position is None:
            self.position = [0., 0., 0.]
        else:
            if len(position) != 3:
                msg = "A Force object position should be initialized " \
                      "with a list of length == 3"
                raise ValueError(msg)
            else:
                self.position = [float(position[0]),
                                 float(position[1]),
                                 float(position[2])]

        self.name = name

    def moment(self, point_of_reference):
        """Moment of the force about the origin of the frame of reference 
        used to define 'position'

        Parameters
        ----------
        point_of_reference : tuple or list[float]
            Tuple or list of 3 floats
        """
        relative_position = [self.position[0] - point_of_reference[0],
                             self.position[1] - point_of_reference[1],
                             self.position[2] - point_of_reference[2]]
        return np.cross(relative_position, self.force)

    @property
    def x(self):
        r"""X component of Force"""
        return self.force[0]

    @property
    def y(self):
        r"""Y component of Force"""
        return self.force[1]

    @property
    def z(self):
        r"""Z component of Force"""
        return self.force[2]

    @property
    def px(self):
        r"""X coordinate of the point of application"""
        return self.position[0]

    @property
    def py(self):
        r"""Y coordinate of the point of application"""
        return self.position[1]

    @property
    def pz(self):
        r"""Z coordinate of the point of application"""
        return self.position[2]

    def __repr__(self):
        """Readable representation of the Force"""
        if self.name is None:
            n = 'no_name'
        else:
            n = self.name
        return 'F:' + str(self.force) + '@' + str(self.position) + '-name: ' + str(n)

    def __str__(self):
        r"""User friendly representation of the Force"""
        return self.__repr__()


class SystemOfForces(object):
    """A system of forces made of n forces

    Parameters
    ----------
    forces : list of Force object(s), optional (default : [])
        Represents all the Forces in the SystemOfForces
    moments_point_of_reference : list of 3 floats,
                                 optional (default : [0., 0., 0.])
        Represents the x, y, z coordinates of the point
        of reference for moments calculations.
    """

    def __init__(self, forces=None, moments_point_of_reference=None):
        self.forces = forces if forces is not None else []
        if moments_point_of_reference is None:
            self.moments_point_of_reference = [0., 0., 0.]
        else:
            self.moments_point_of_reference = moments_point_of_reference

    @property
    def moment(self):
        """The moment vector coordinates [x,y,z] of the SystemOfForces

        Returns
        -------
        list[float]

        """
        # axis = 0 -> sum of each column
        return np.sum([f.moment(self.moments_point_of_reference)
                       for f in self.forces], axis=0)

    @property
    def mx(self):
        r"""Moment around X axis"""
        return self.moment[0]

    @property
    def my(self):
        r"""Moment around Y axis"""
        return self.moment[1]

    @property
    def mz(self):
        r"""Moment around Z axis"""
        return self.moment[2]

    @property
    def force(self):
        """The sum of all force vectors [x,y,z] of the SystemOfForces

        Returns
        -------
        list[float]

        """
        # axis = 0 -> sum of each column
        return np.sum([f.force for f in self.forces], axis=0)

    @property
    def x(self):
        r"""X component of the resulting force"""
        return self.force[0]

    @property
    def y(self):
        r"""Y component of the resulting force"""
        return self.force[1]

    @property
    def z(self):
        r"""Z component of the resulting force"""
        return self.force[2]

    def add_force(self, force):
        """Add a Force object to the SystemOfForces object

        Parameters
        ----------
        force : Force object

        """
        self.forces.append(force)
