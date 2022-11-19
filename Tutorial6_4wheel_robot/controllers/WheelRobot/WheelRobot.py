"""WheelRobot controller."""

from controller import Robot,Motor

robot=Robot()

# Parameters
MAX_SPEED=6
STEP_TIME=16

# 获取距离传感器
distanceSensors=[]
distanceSensorsName=['left distance sensor','right distance sensor']
for i in range(2):
    distanceSensors.append(robot.getDevice(distanceSensorsName[i]))
    distanceSensors[i].enable(STEP_TIME)

# 获取关节电机
motors=[]
motorName=['wheel1','wheel2','wheel3','wheel4']
for i in range(4):
    motors.append(robot.getDevice(motorName[i]))
    motors[i].setPosition(float('inf'))
    motors[i].setVelocity(0.0)

avoidObstacleCounter=0
while robot.step(STEP_TIME)!=-1:
    leftSpeed=3.
    rightSpeed=3.
    if avoidObstacleCounter>0:
        avoidObstacleCounter-=1
        rightSpeed=-3.
    else:
        for i in range(2):
            if distanceSensors[i].getValue()<900:
                avoidObstacleCounter=100
    motors[0].setVelocity(leftSpeed)
    motors[1].setVelocity(rightSpeed)
    motors[2].setVelocity(leftSpeed)
    motors[3].setVelocity(rightSpeed)

