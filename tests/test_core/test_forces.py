#!/usr/bin/env python
# coding: utf-8

r"""Tests for the core.force.py module"""

from corelib.core.forces import Force, SystemOfForces

force_x_plus_at_0_m1_0 = Force([1., 0., 10.], [0., -1., 0.])
force_x_minus_at_0_1_0 = Force([-1., 0., 10.], [0., 1., 0.])

force_y_plus_at_m1_0_0 = Force([0., 1., 10.], [-1., 0., 0.])
force_y_minus_at_1_0_0 = Force([0., -1., -30.], [1., 0., 0.])


def test_system_of_forces_ref_at_0_0_0():
    r"""Reference is at the origin"""
    sf = SystemOfForces(moments_point_of_reference=[0., 0., 0.])
    sf.add_force(force_x_plus_at_0_m1_0)
    sf.add_force(force_x_minus_at_0_1_0)
    sf.add_force(force_y_plus_at_m1_0_0)
    sf.add_force(force_y_minus_at_1_0_0)
    assert (sf.force == [0., 0.,  0.]).all()
    assert (sf.moment == [0., 40., 0.]).all()


def test_system_of_forces_ref_somewhere_else():
    r"""Reference is at an arbitrary point"""
    sf_2 = SystemOfForces(moments_point_of_reference=[10., 22., 3800.])
    sf_2.add_force(force_x_plus_at_0_m1_0)
    sf_2.add_force(force_x_minus_at_0_1_0)
    sf_2.add_force(force_y_plus_at_m1_0_0)
    sf_2.add_force(force_y_minus_at_1_0_0)
    assert (sf_2.force == [0., 0.,  0.]).all()
    assert (sf_2.moment == [0., 40., 0.]).all()

