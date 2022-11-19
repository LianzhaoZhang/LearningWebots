from controller import Robot, Motor

# Parameters
TIME_STEP = 64
MAX_VELOCITY=6.28

robot = Robot()

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.1*MAX_VELOCITY)
rightMotor.setVelocity(0.1*MAX_VELOCITY)

while robot.step(TIME_STEP) != -1:
    pass
    