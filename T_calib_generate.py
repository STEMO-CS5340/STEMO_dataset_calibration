#!/usr/bin/env python3

# Python dependency scipy (numpy), sophuspy
# Binding dependency: Pybind11 https://github.com/pybind/pybind11 (Do not use pip to install, download the project and use camke to install manually)

import numpy as np
import sophus
from scipy.spatial.transform import Rotation as Rot

d2r = np.pi / 180.0

class SE3Object:

    # internal storage for left and right camera transformation
    T = sophus.SE3() # active rotation from world to the camera

    # change of coordinates from NWU to Camera
    T_nwu_cam = sophus.SE3([[0,-1,0, 0],
                            [0,0,-1, 0],
                            [1,0,0,0],
                            [0,0,0,1]])

    # roll, pitch, yaw (yaw = - heading) in degree
    def fromRPYt_deg(self, roll, pitch, yaw, t_vec):
        self.fromRPYt_rad(roll*d2r, pitch*d2r, yaw*d2r, t_vec)

    def fromRPYt_rad(self, roll, pitch, yaw, t_vec):
        R = Rot.from_rotvec([roll, pitch, yaw])
        self.T = sophus.SE3(R.as_dcm(), t_vec)

    # convert from body (NWU) coordinates to world coordinates
    def T_body2world(self):
        return self.T

    def T_cam2world(self):
        return self.T * self.T_nwu_cam.inverse() # T is in NWU frame
    # convert from body (NWU) coordinates to world coordinates

    def T_world2body(self):
        return self.T_body2world().inverse()

    def T_world2cam(self):
        return self.T_cam2world().inverse()

# left camera
caml = SE3Object()
caml.fromRPYt_deg(0,0,-(204 - 160), np.array([0,0,0])) # NWU frame
print(caml.T_world2cam())

#right camera
camr = SE3Object()
camr.fromRPYt_deg(0,0,-(109 - 160), np.array([-1,-5,0])) # NWU frame
print(camr.T_world2cam())