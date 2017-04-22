from setuptools import setup, Extension

try:
    from Cython.Build import cythonize

    ext = cythonize([
        Extension("cyrandom.cyrandom",
                  sources=["cyrandom/cyrandom.pyx",
                           "cyrandom/_mersenne.c",
                           "cyrandom/_seed.c"])],
        compiler_directives={'language_level': 3})
except ImportError:
    ext = [Extension("cyrandom.cyrandom",
                     sources=["cyrandom/cyrandom.c",
                              "cyrandom/_mersenne.c",
                              "cyrandom/_seed.c"],
                     language='C')]

setup(
    name="cyrandom",
    version='0.2.1',
    description='Fast random number generation.',
    long_description="A fast cython replacement for the standard library's random module.",
    url='https://github.com/Noctem/cyrandom',
    author='David Christenson',
    author_email='mail@noctem.xyz',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Cython',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License'
    ],
    keywords='cyrandom random rng cython',
    packages=['cyrandom'],
    package_data={'cyrandom': ['cyrandom.pxd']},
    ext_modules=ext)
