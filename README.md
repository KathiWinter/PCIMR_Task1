# PCIMR_Task1

You can run this task by the following commands: 
`roscore` 
`rosrun pcimr_simulation simple_sim_node`
`rosrun pcimr_findgoal navigation`

The subscribers, publisher, service, as well as the algorithm are located in **navigation_node**. 
It has the following functions:
`def run(self, rate: float = 1)`
This method runs the node. 

`def __init(self)`
This method initializes the node and its publisher, subscribers and the service.

The following methods are callbackfunctions: 

`def init_pos(request)` 
This handles the request to initialize the position and returns true or false, depending on if its input is 2,0 or not.

`def move(self, date)` 
This method is the callback of the subscriber to the scan. It checks the range of the robot an depending on that, the robot either moves north, east, or realizes that it has reached the goal. 


`def callback(self, date)`
This method is a callback of the subscriber to the robot position. It saves the robot position in global variables. 


