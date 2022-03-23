from setuptools import setup


package_name = 'fleet_adapter_mir'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['mir_config.yaml']),
    #     ('share/' + package_name, ['rosi_config.yaml']),
    #     ('share/' + package_name, ['nav_graph.yaml'])
    ],
    
        
    
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Eric Dong',
    maintainer_email='eric.dongxx@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['main=fleet_adapter_mir.main:main'],
                           
    },
)
