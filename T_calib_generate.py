#!/usr/bin/env python3

# Python dependency scipy (numpy), sophuspy
# Binding dependency: Pybind11 https://github.com/pybind/pybind11 (Do not use pip to install, download the project and use camke to install manually)

import numpy as np
import sophus
from scipy.spatial.transform import Rotation as Rot

d2r = np.pi / 180.0

class SE3Object:

    #internal storage for left and right camera transformation
    T = sophus.SE3() # active rotation from world to the camera

    # roll, pitch, yaw in degree
    def fromRPYt_deg(self, roll, pitch, yaw, t_vec):
        self.fromRPYt_rad(roll*d2r, pitch*d2r, yaw*d2r, t_vec)

    def fromRPYt_rad(self, roll, pitch, yaw, t_vec):
        R = Rot.from_rotvec([roll, pitch, yaw])
        self.T = sophus.SE3(R.as_dcm(), t_vec)

    # convert from object coordinates to world coordinates
    def T_obj2world(self):
        return self.T

    # convert from object coordinates to world coordinates
    def T_world2obj(self):
        return self.T.inverse()


# left camera
caml = SE3Object()
caml.fromRPYt_deg(0,0,204, np.array([0,0,0]))
print(caml.T_world2obj())

#right camera
camr = SE3Object()
camr.fromRPYt_deg(0,0,109, np.array([-1,-5,0]))
print(camr.T_world2obj())