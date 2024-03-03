import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

# Define the Logger node


def main(args=None):
    rclpy.init(args=args)

    logger = Logger("log.txt")

    rclpy.spin(logger)

    logger.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
