#!/usr/bin/env python
# coding: utf-8

r"""Forces example"""

from corelib.core.forces import Force, SystemOfForces

# fam1 = ForceAndMoment([0,0,1],[0,0,0], [0,1,0])
# print fam1.moment

force_x_plus_at_0_m1_0 = Force([1., 0., 10.], [0., -1., 0.])
force_x_minus_at_0_1_0 = Force([-1., 0., 10.], [0., 1., 0.])

force_y_plus_at_m1_0_0 = Force([0., 1., 10.], [-1., 0., 0.])
force_y_minus_at_1_0_0 = Force([0., -1., -30.], [1., 0., 0.])

sf = SystemOfForces(moments_point_of_reference=[0., 0., 0.])
sf_2 = SystemOfForces(moments_point_of_reference=[10., 22., 3800.])

sf.add_force(force_x_plus_at_0_m1_0)
sf.add_force(force_x_minus_at_0_1_0)

sf.add_force(force_y_plus_at_m1_0_0)
sf.add_force(force_y_minus_at_1_0_0)

sf_2.add_force(force_x_plus_at_0_m1_0)
sf_2.add_force(force_x_minus_at_0_1_0)

sf_2.add_force(force_y_plus_at_m1_0_0)
sf_2.add_force(force_y_minus_at_1_0_0)

print('*************')
print('System of Forces - ref at 0,0,0')
print('Total force : %s' % str(sf.force))
print('Total moment : %s' % str(sf.moment))

print('*************')
print('System of Forces - ref somewhere else')
print('Total force : %s' % str(sf_2.force))
print('Total moment : %s' % str(sf_2.moment))
