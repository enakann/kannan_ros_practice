import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
import os
#name='name'
#DeclareLaunchArgument(eval_node_name, default_value='lca_evaluation_node.py'),
#Node(package=PACKAGE_NAME, node_executable=LaunchConfiguration(eval_node_name), output='screen'),

def get_params_for(file_name, dir_path, env_name):
        """Function to create a ros2 launch system compatible parameter array for a given parameter file location.

        Keyword Arguments:
            file_name : The name of the launch file, e.g 'param.yaml'

            dir_path : The path to the directory containing the parameter file

            env_name : Arbitrary environment variable name for temporarily storing the dir_path

        As of now, the dcrt launch system does not provide a simple way to use launch files. This function is a
        workaround and can be removed once a simpler API is available for loading parameter files.

        Returns:
            The ros2 launch system compatible params array
        """
        params_file_path = os.path.join(dir_path,file_name)
        os.environ['name'] ='kannan'

        return params

eval_node_name='eval_node_name'

#print(os.curdir)
#params=get_params_for("myparams.yml",".","name")
#print(params)


def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            'node_prefix',
            default_value=[launch.substitutions.EnvironmentVariable('USER'), 'love'],
            description='Prefix for node names'),

        launch.actions.DeclareLaunchArgument('name', default_value ='obi own'),

        launch.actions.DeclareLaunchArgument(eval_node_name, default_value='sos_publisher2'),  #set wrong data on purpose

        launch_ros.actions.Node(
            package='ros2_pub_py', 
            node_executable=[launch.substitutions.LaunchConfiguration(eval_node_name)], 
            output='screen',
            parameters=['./myparams.yml'],
            node_name=[launch.substitutions.LaunchConfiguration(eval_node_name)]),
    ])
