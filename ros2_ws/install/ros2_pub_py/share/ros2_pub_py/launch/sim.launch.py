import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
import os
#from yaml_parser import YAML
import yaml
import pathlib

#name='name'
#DeclareLaunchArgument(eval_node_name, default_value='lca_evaluation_node.py'),
#Node(package=PACKAGE_NAME, node_executable=LaunchConfiguration(eval_node_name), output='screen'),

CONFIG_PATH="/home/navi/Desktop/ros2_demo_1_1547429184/ros2_ws/install/ros2_pub_py/share/ros2_pub_py/launch"
class YAML:
    def __init__(self,filename=None):
        self.__filenane=filename
        self.__config_path=os.path.join(CONFIG_PATH,self.__filenane)
        self.__config=self.__load_config()
    def __load_config(self):
        try:
           with open (self.__config_path) as f:
               config = yaml.safe_load(f)
        except Exception as e:
            raise e
        return config
    def get_config(self,name):
        return self.__config[name]

    def get_all_data(self):
        return self.__config

cur_dir = pathlib.Path(__file__).resolve().parent
print(cur_dir)


def get_params_for(file_name, dir_path, env_name):
    params_file_path = dir_path / file_name
    os.environ[env_name] = str(dir_path)
    params = [
        params_file_path,
        str(params_file_path),
        [os.environ.get(env_name), os.sep, file_name],
    ]
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



def get_eval_node():
        eval_node=launch_ros.actions.Node(
            package='ros2_pub_py',
            node_executable=[launch.substitutions.LaunchConfiguration(eval_node_name)],
            output='screen',
            #parameters=['./myparams.yml'],
            parameters=get_params_for(file_name="myparams.yml",dir_path=cur_dir,env_name="LAUNCH_DIR_PATH"),
            node_name=[launch.substitutions.LaunchConfiguration(eval_node_name)])
        return eval_node


def get_service_nodes(service_file,nodes_file,service_name):
    ls=[]
    service_config = YAML(service_file)
    nodes_config = YAML(nodes_file)
    nodes = service_config.get_config(service_name)
    for node in nodes:
        config = nodes_config.get_config(node)
        config['parameters']=get_params_for(file_name="myparams.yml",dir_path=cur_dir,env_name="LAUNCH_DIR_PATH")
        nodeobj = launch_ros.actions.Node(**config)
        ls.append(nodeobj)
    return ls



def generate_launch_description():
    launch_argument=get_launch_argument()
    eval_node=get_eval_node()
    nodes=get_service_nodes('services','nodes','serviceb')
    nodes.append(eval_node)
    launch_description=launch.LaunchDescription([])
    #[x._Node__node_name for x in nodes.entities if isinstance(x,launch_ros.actions.Node) and not isinstance(x._Node__node_name,list)]
    launch_description.entities.extend(nodes)
    launch_description.entities.extend(launch_argument)
    print([x._Node__node_name for x in launch_description.entities if isinstance(x,launch_ros.actions.Node)])
    #import pdb;pdb.set_trace()
    return launch_description
