from setuptools import find_packages, setup

package_name = 'gui_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tasneem',
    maintainer_email='tasneemyosry700@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        "main = gui_pkg.main_window:main",
        "sensors = gui_pkg.sensors_pub:main",
        ],
    },
)
