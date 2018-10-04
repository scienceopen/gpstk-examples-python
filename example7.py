#!/usr/bin/env python
"""
An example of how to walk a RINEX data set and use SatID and ObsID,
building an obsEpochMap of the data along the way.
"""
from __future__ import print_function
import gpstk

fn = gpstk.getPathData() + '/arlm200z.15o'

# read in header and get a generator for the data
header, data = gpstk.readRinex3Obs(fn)
print(header)

oem = gpstk.ObsEpochMap()
for d in data:
    print(gpstk.CivilTime(d.time))
    oe = gpstk.ObsEpoch()
    oe.time = d.time
    for sv in list(d.obs.keys()):
        # sv is an SatID object
        print(sv, end=' ')
        epoch = d.obs[sv]
        soe = gpstk.SvObsEpoch()
        soe.svid = sv
        for i in range(len(epoch)):
            rinex2_obs_type = header.R2ObsTypes[i]
            oid = header.mapObsTypes['G'][i]
            print("{}({})={}".format(oid, rinex2_obs_type, epoch[i].data), end=' ')
            soe[oid] = epoch[i].data
        oe[sv] = soe
        print()
    oem[d.time] = oe
