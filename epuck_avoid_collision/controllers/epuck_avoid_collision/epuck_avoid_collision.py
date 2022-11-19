from controller import Robot, Motor, DistanceSensor

# Parameters
TIME_STEP = 64
MAX_SPEED = 6.2

# 创建机器人实例
robot = Robot()

# 初始化硬件
ps = []
psName = ['ps0', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7']
for i in range(8):
    ps.append(robot.getDevice(psName[i]))
    ps[i].enable(TIME_STEP)

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

while robot.step(TIME_STEP) != -1:
    # 获取传感器输出
    psValues = []
    for i in range(8):
        psValues.append(ps[i].getValue())
    # 判断是否有障碍
    rightObstacle = psValues[0] > 200 or psValues[1] > 200 or psValues[2] > 200 or psValues[3] > 200
    leftObstacle = psValues[4] > 200 or psValues[5] > 200 or psValues[6] > 200 or psValues[7] > 200
    # 初始化电机转速
    leftSpeed = 0.6 * MAX_SPEED
    rightSpeed = 0.6 * MAX_SPEED
    if leftObstacle:
        rightSpeed = -0.4 * MAX_SPEED
    if rightObstacle:
        leftSpeed = -0.4 * MAX_SPEED
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)
