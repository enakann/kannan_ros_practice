import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            'node_prefix',
            default_value=[launch.substitutions.EnvironmentVariable('USER'), 'love'],
            description='Prefix for node names'),
        launch_ros.actions.Node(
            package='ros2_pub_py', node_executable='sos_publisher', output='screen',
            node_name=[launch.substitutions.LaunchConfiguration('node_prefix'), 'talker']),
    ])
