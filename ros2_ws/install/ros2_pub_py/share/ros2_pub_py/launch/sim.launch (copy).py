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

def get_launch_argument():
    launch_argument = [launch.actions.DeclareLaunchArgument(
            'node_prefix',
            default_value=[launch.substitutions.EnvironmentVariable('USER'), 'love'],
            description='Prefix for node names'),

    launch.actions.DeclareLaunchArgument('name', default_value ='obi own'),

    launch.actions.DeclareLaunchArgument(eval_node_name, default_value='sos_publisher2')]
    return launch_argument



def get_nodes():
    ls=[
        launch_ros.actions.Node(
            package='ros2_pub_py', 
            node_executable=[launch.substitutions.LaunchConfiguration(eval_node_name)], 
            output='screen',
            parameters=['./myparams.yml'],
            node_name=[launch.substitutions.LaunchConfiguration(eval_node_name)]),

        launch_ros.actions.Node(
            package='ros2_pub_py',
            node_executable= 'driver_control',
            output='screen',
            parameters=['./myparams.yml'],
            node_name='driver_control'),

        launch_ros.actions.Node(
            package='ros2_pub_py',
            node_executable='driver_control_sub',
            output='screen',
            parameters=['./myparams.yml'],
            node_name='driver_control_sub'),]
    return ls



def generate_launch_description():
    ls=['driver_control']
    launch_argument=get_launch_argument()
    nodes=get_nodes()
    launch_description=launch.LaunchDescription([])
    #[x._Node__node_name for x in nodes.entities if isinstance(x,launch_ros.actions.Node) and not isinstance(x._Node__node_name,list)]
    launch_description.entities.extend(nodes)
    launch_description.entities.extend(launch_argument)
    print([x._Node__node_name for x in launch_description.entities if isinstance(x,launch_ros.actions.Node)])
    import pdb;pdb.set_trace()
    return launch_description
