__copyright__ = 'Copyright (c) 2014-2016 SSPA Sweden AB'

import setuptools
from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration
from distutils.extension import Extension
from Cython.Build import cythonize
import sys
import numpy
import os

config = Configuration()
config.add_include_dirs(['pysim/cppsource', numpy.get_include()])

extracompileargs = []
if sys.platform == "win32":
    config.add_include_dirs([os.environ.get('BOOST_ROOT')])
        
elif sys.platform in ("linux","darwin"):
    extracompileargs.append("-std=c++11")

config.add_installed_library("cppsystemlib",
                    ['pysim/cppsource/CppSystem.cpp',
                     'pysim/cppsource/StoreHandler.cpp',
                     'pysim/cppsource/CommonSystemImpl.cpp',
                     'pysim/cppsource/Variable.cpp',
                    ],
                    build_info = {
                    "extra_compiler_args":extracompileargs,
                    "language":"c++"},
                    install_dir = "pysim/lib",
                    )

                                
extensions = [Extension("pysim.cppsystem",
                        ['pysim/cppsystem.pyx',],
                        language="c++",
                        extra_compile_args=extracompileargs,
                        libraries=["cppsystemlib",]
                        ),
              Extension("pysim.cythonsystem",
                        ['pysim/cythonsystem.pyx','pysim/cppsource/CythonSystemImpl.cpp'],
                        language="c++",
                        extra_compile_args=extracompileargs,
                        libraries=["cppsystemlib",]
                        ),
              Extension("pysim.commonsystem",
                        ['pysim/commonsystem.pyx'],
                        language="c++",
                        extra_compile_args=extracompileargs,
                        libraries=["cppsystemlib",]
                        ),
              Extension("pysim.simulation",
                        ['pysim/simulation.pyx', 'pysim/cppsource/CppSimulation.cpp'],
                        language="c++",
                        extra_compile_args=extracompileargs,
                        ),
              Extension("pysim.systems.defaultsystemcollection1",
                         ['pysim/systems/defaultsystemcollection1/defaultsystemcollection1.pyx',
                          'pysim/systems/defaultsystemcollection1/cppsource/factory.cpp',
                          'pysim/systems/defaultsystemcollection1/cppsource/MassSpringDamper.cpp',
                          'pysim/systems/defaultsystemcollection1/cppsource/PredatorPrey.cpp',
                          'pysim/systems/defaultsystemcollection1/cppsource/VanDerPol.cpp',
                          'pysim/systems/defaultsystemcollection1/cppsource/Adder3D.cpp',
                          'pysim/systems/defaultsystemcollection1/cppsource/Adder.cpp',
                          'pysim/systems/defaultsystemcollection1/cppsource/ScalarAdder.cpp',
                          'pysim/systems/defaultsystemcollection1/cppsource/SquareWave.cpp',
                          'pysim/systems/defaultsystemcollection1/cppsource/DiscretePID.cpp',
                          'pysim/systems/defaultsystemcollection1/cppsource/ReadTextInput.cpp',
                          'pysim/systems/defaultsystemcollection1/cppsource/RigidBody.cpp',
                          'pysim/systems/defaultsystemcollection1/cppsource/LogisticMap.cpp',
                          ],
                          language="c++",
                          extra_compile_args=extracompileargs,
                          include_dirs=['pysim/systems/defaultsystemcollection1',],
                          libraries=["cppsystemlib",],
                          ),
             ]
             
setup(
    name="pysim",
    version="2.0.0",
    author="Linus Aldebjer",
    author_email="aldebjer@gmail.com",
    url="http://pys.im",
    ext_modules=cythonize(extensions),

    data_files=[('pysim/include',['pysim/cppsource/SimulatableSystem.hpp',
                                  'pysim/cppsource/CppSystem.hpp',
                                  'pysim/cppsource/PysimTypes.hpp',
                                  'pysim/cppsource/CommonSystemImpl.hpp',
                                  'pysim/cppsource/Variable.hpp',
                                  'pysim/cppsource/StoreHandler.hpp',
                                  'pysim/cppsource/CythonSystemImpl.hpp']),
                ('pysim',['pysim/cppsystem.pxd',
                          'pysim/commonsystem.pxd',
                          'pysim/simulatablesystem.pxd',
                          'pysim/cythonsystem.pxd']),
                ],
    packages=['pysim', 'pysim.systems','pysim.tests'],
    install_requires = ['numpy>=1.8.1',],
    description = "package for dynamical system modelling",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    **config.todict()
)
