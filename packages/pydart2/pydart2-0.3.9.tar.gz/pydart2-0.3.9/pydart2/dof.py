# Copyright (c) 2015, Disney Research
# All rights reserved.
#
# Author(s): Sehoon Ha <sehoon.ha@disneyresearch.com>
# Disney Research Robotics Group
import pydart2_api as papi


class Dof(object):
    """
    """
    def __init__(self, _skeleton, _id):
        """
        """
        self.skeleton = _skeleton
        self.id = _id
        self.name = papi.dof__getName(self.wid, self.skid, self.id)
        self.joint = None

    @property
    def skel(self):
        return self.skeleton

    @property
    def wid(self):
        return self.skel.world.id

    @property
    def skid(self):
        return self.skel.id

########################################
# Dof::Index functions
    def index_in_skeleton(self, ):
        return papi.dof__getIndexInSkeleton(self.wid,
                                            self.skid,
                                            self.id)

    def index_in_tree(self, ):
        return papi.dof__getIndexInTree(self.wid,
                                        self.skid,
                                        self.id)

    def index_in_joint(self, ):
        return papi.dof__getIndexInJoint(self.wid,
                                         self.skid,
                                         self.id)

    def tree_index(self, ):
        return papi.dof__getTreeIndex(self.wid, self.skid, self.id)

########################################
# Dof::Position functions
    def position(self, ):
        return papi.dof__getPosition(self.wid, self.skid, self.id)

    def set_position(self, _position):
        papi.dof__setPosition(self.wid, self.skid, self.id, _position)

    def initial_position(self, ):
        return papi.dof__getInitialPosition(self.wid, self.skid, self.id)

    def set_initial_position(self, _initial):
        papi.dof__setInitialPosition(self.wid, self.skid, self.id, _initial)

    def has_position_limit(self, ):
        return papi.dof__hasPositionLimit(self.wid, self.skid, self.id)

    def position_lower_limit(self, ):
        return papi.dof__getPositionLowerLimit(self.wid, self.skid, self.id)

    def set_position_lower_limit(self, _limit):
        papi.dof__setPositionLowerLimit(self.wid, self.skid, self.id, _limit)

    def position_upper_limit(self, ):
        return papi.dof__getPositionUpperLimit(self.wid, self.skid, self.id)

    def set_position_upper_limit(self, _limit):
        papi.dof__setPositionUpperLimit(self.wid, self.skid, self.id, _limit)

########################################
# Dof::Velocity functions
    def velocity(self, ):
        return papi.dof__getVelocity(self.wid, self.skid, self.id)

    def set_velocity(self, _velocity):
        papi.dof__setVelocity(self.wid, self.skid, self.id, _velocity)

    def initial_velocity(self, ):
        return papi.dof__getInitialVelocity(self.wid, self.skid, self.id)

    def set_initial_velocity(self, _initial):
        papi.dof__setInitialVelocity(self.wid, self.skid, self.id, _initial)

    def velocity_lower_limit(self, ):
        return papi.dof__getVelocityLowerLimit(self.wid, self.skid, self.id)

    def set_velocity_lower_limit(self, _limit):
        papi.dof__setVelocityLowerLimit(self.wid, self.skid, self.id, _limit)

    def velocity_upper_limit(self, ):
        return papi.dof__getVelocityUpperLimit(self.wid, self.skid, self.id)

    def set_velocity_upper_limit(self, _limit):
        papi.dof__setVelocityUpperLimit(self.wid, self.skid, self.id, _limit)

    def __repr__(self):
        return '[Dof(%d): %s]' % (self.id, self.name)
