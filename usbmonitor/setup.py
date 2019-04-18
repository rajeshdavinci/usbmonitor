from setuptools import setup
setup(name='usbmonitor',
      version='0.1',
      description='script to monitor adding usb devices',
      author='gs',
      author_email='rajeshdavinci@gmail.com',
      license='MIT',
      packages=['usbmonitor'],
      entry_points = {
          'console_scripts': ['usbmonitor=usbmonitor.command_line:main'],
          },
      zip_safe=False)
