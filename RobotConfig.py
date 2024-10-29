class RobotDimensions: 
    "This Class Contains All Robot Dimensions"
    trackWidth = 0.5715
    wheelBase = 0.5969
    
class SwerveID:
    "This Contains Swerve CAN ID's"
    class frontLeft:
        driveMotorID = 1
        turnMotorID = 2
        
    class frontRight:
        driveMotorID = 3
        turnMotorID = 4
        
    class rearRight:
        driveMotorID = 5
        turnMotorID = 6
        
    class rearLeft: 
        driveMotorID = 7
        turnMotorID = 8
        
SwerveID = SwerveID() # Annotation 
