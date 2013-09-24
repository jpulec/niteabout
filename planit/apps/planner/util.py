import math
from decimal import Decimal

def distance_in_miles(lat1, long1, lat2, long2):

    # Convert latitude and longitude to 
# spherical coordinates in radians.
    degrees_to_radians = Decimal(math.pi/180.0)

# phi = 90 - latitude
    phi1 = (Decimal(90.0) - lat1)*degrees_to_radians
    phi2 = (Decimal(90.0) - Decimal(lat2[1:]))*degrees_to_radians

# theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = Decimal(long2[:-1])*degrees_to_radians

# Compute spherical
# distance from
# spherical coordinates.

# For two locations
# in spherical
# coordinates 
# (1, theta,
# phi) and (1,
# theta, phi)
# cosine(
# arc length
# ) = 
#    sin
#    phi
#    sin
#    phi'
#    cos(theta-theta')
#    +
#    cos
#    phi
#    cos
#    phi'
# distance
# =
# rho
# *
# arc
# length

    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
            math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

# Remember
# to
# multiply
# arc by the radius of the earth 
    # in
    # your
    # favorite
    # set
    # of
    # units
    # to
    # get
    # length.
    return arc*3960
