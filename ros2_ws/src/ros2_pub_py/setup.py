import os
from glob import glob
from setuptools import setup

package_name = 'ros2_pub_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    py_modules=[
        'sos_publisher',
        'driver_control',
        'driver_control_sub',
    ],
     data_files=[
        # ... Other data files
        # Include all launch files. This is the most important line here!
        (os.path.join( package_name, 'launch'), glob('*.launch.py'))
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    author='user',
    author_email="user@todo.todo",
    maintainer='user',
    maintainer_email="user@todo.todo",
    keywords=['ROS', 'ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='TODO: Package description.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sos_publisher = sos_publisher:main',
            'driver_control = driver_control:main',
            'driver_control_sub = driver_control_sub:main',
        ],
    },
)
