# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
import os
from std_msgs.msg import String

#name=os.environ['name']
#print(os.environ)

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('sos_publisher')
    #import pdb;pdb.set_trace()
    print(node._parameters)
    publisher = node.create_publisher(String, 'sos')

    msg = String()
    
    def timer_callback():
        name1=node.get_parameter('kannan')._value
        name2=node.get_parameter('divi')._value

        msg.data = 'kannan {}  divi but,but divi {} kannan'.format(name1,name2)
        node.get_logger().info('Publishing sos message: "%s"' % msg.data)
        #node.get_logger().info(str(os.environ))
        publisher.publish(msg)

    timer_period = 0.5  # seconds
    timer = node.create_timer(timer_period, timer_callback)

    rclpy.spin(node)

    # Destroy the timer attached to the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_timer(timer)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    #name='name'
    main()
