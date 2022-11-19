"""my_controller controller."""

from controller import Robot, Motor, DistanceSensor

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

ds=[]
ds_name=['left distance sensor','right distance sensor']
for i in range(2):
    ds.append(robot.getDevice(ds_name[i]))
    ds[i].enable(timestep)

wheel=[]
wheel_name=['wheel1','wheel2','wheel3','wheel4']
for i in range(4):
    wheel.append(robot.getDevice(wheel_name[i]))
    wheel[i].setPosition(float('inf'))
    wheel[i].setVelocity(0.0)
    
avoid=0
while robot.step(timestep) != -1:
    left_speed=2.
    right_speed=2.
    if avoid>0:
        avoid-=1
        right_speed=-2.
    else:
        for i in range(2):
            if ds[i].getValue()<800:
                avoid=50
    wheel[0].setVelocity(right_speed)
    wheel[1].setVelocity(left_speed)
    wheel[2].setVelocity(right_speed)
    wheel[3].setVelocity(left_speed)
# Enter here exit cleanup code.
