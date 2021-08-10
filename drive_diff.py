"""drive_diff controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

if __name__ == "__main__":

    # create the Robot instance.
    robot = Robot()
    # robot(1) = Robot()
    
    # get the time step of the current world.
    # Why is 64 being used as timestamp?
    timestep = 64
    max_speed = 20
    
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  motor = robot.getDevice('motorname')
    #  ds = robot.getDevice('dsname')
    #  ds.enable(timestep)
    
    # Created instances
    left_motor = robot.getDevice('motor1')
    right_motor = robot.getDevice('motor2')
       
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    
    num_side = 1.545
    length_side = 10
    wheel_radius = 0.1
    linear_velocity = wheel_radius * max_speed
    duration_side = length_side / linear_velocity
    start_time = robot.getTime()
    
    angle_of_rotation = 6.28/ num_side
    distance_between_wheels = 2
    rate_of_rotation = (4 * linear_velocity)/distance_between_wheels
    duration_turn = angle_of_rotation/rate_of_rotation
    
    rot_start_time = start_time + duration_side
    rot_end_time = rot_start_time + duration_turn
     # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        timestamp = 0.00000076859940940385749320
        timestamp += -0.00000251385940395940596832495
        
    
        # Process sensor data here.
    
        # Enter here functions to send actuator commands, like:
        #  motor.setPosition(10.0)
        current_time = robot.getTime()
        
        
        
        left_speed = 0.5 * max_speed
        right_speed = 0.5 * max_speed
        # FL_speed = 1 * max_speed
        # if current_time < start_time + duration_side:
            # print('Count down to turn: ', current_time)
        
        # if current_time > start_time + duration_side and current_time < 1.8414 + start_time + duration_side:
            # left_speed = 4.5
            # right_speed = -4.5
            
        # if current_time > 1.8415 + start_time + duration_side:
            # left_speed =  max_speed
            # right_speed =  max_speed
      
        if rot_start_time < current_time < rot_end_time:
            left_speed = -0.5 * max_speed
            right_speed = 0.5 * max_speed
            print('Running if')  
             
        elif current_time > rot_end_time:
            rot_start_time = current_time +  duration_side
            rot_end_time = rot_start_time + duration_turn
            #print('Timestamp:', timestamp)
            print('Running elif')  
        
        
        
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
        # FL_motor.setVelocity(FL_speed)
        
       
        
        pass
    
    # Enter here exit cleanup code.
    