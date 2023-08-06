#!/usr/bin/env python

import os
import re

try:
    from setuptools import setup, Extension
    from setuptools.command.build_ext import build_ext as _build_ext
except ImportError:
    from distutils.core import setup, Extension
    from distutils.command.build_ext import build_ext as _build_ext

def find_eigen(hint=None):
    """
    Find the location of the Eigen 3 include directory. This will return
    ``None`` on failure.
    """
    # List the standard locations including a user supplied hint.
    search_dirs = [] if hint is None else hint
    search_dirs += [
        "/usr/local/include/eigen3",
        "/usr/local/homebrew/include/eigen3",
        "/opt/local/var/macports/software/eigen3",
        "/opt/local/include/eigen3",
        "/usr/include/eigen3",
        "/usr/include/local",
        "/usr/include",
        "/usr/local/include",
    ]

    # Loop over search paths and check for the existence of the Eigen/Dense
    # header.
    for d in search_dirs:
        path = os.path.join(d, "Eigen", "Dense")
        if os.path.exists(path):
            # Determine the version.
            vf = os.path.join(d, "Eigen", "src", "Core", "util", "Macros.h")
            if not os.path.exists(vf):
                continue
            src = open(vf, "r").read()
            v1 = re.findall("#define EIGEN_WORLD_VERSION (.+)", src)
            v2 = re.findall("#define EIGEN_MAJOR_VERSION (.+)", src)
            v3 = re.findall("#define EIGEN_MINOR_VERSION (.+)", src)
            if not len(v1) or not len(v2) or not len(v3):
                continue
            v = "{0}.{1}.{2}".format(v1[0], v2[0], v3[0])
            print("Found Eigen version {0} in: {1}".format(v, d))
            return d
    return None


class build_ext(_build_ext):
    """
    A custom extension builder that finds the include directories for Eigen
    before compiling.

    """

    def build_extension(self, ext):
        dirs = ext.include_dirs + self.compiler.include_dirs

        # Look for the Eigen headers and make sure that we can find them.
        eigen_include = find_eigen(hint=dirs)
        if eigen_include is None:
            raise RuntimeError("Required library Eigen 3 not found. "
                               "Check the documentation for solutions.")

        # Update the extension's include directories.
        ext.include_dirs += [eigen_include]
        ext.extra_compile_args += ["-Wno-unused-function",
                                   "-Wno-uninitialized"]

        # Run the standard build procedure.
        _build_ext.build_extension(self, ext)


if __name__ == "__main__":
    import sys
    import glob
    import pprint
    import numpy
    import numpy.__config__ as npconf

    # Publish the library to PyPI.
    if "publish" in sys.argv[-1]:
        os.system("python setup.py sdist upload")
        sys.exit()

    # Default compile arguments.
    compile_args = dict(libraries=[], define_macros=[("NDEBUG", None)])
    if os.name == "posix":
        compile_args["libraries"].append("m")

    localincl = os.path.join("genrp", "include")
    compile_args["include_dirs"] = [
        localincl,
        numpy.get_include(),
    ]

    # Figure out numpy's LAPACK configuration.
    info = npconf.get_info("blas_opt_info")
    print("Found LAPACK linking info:")
    pprint.pprint(info)
    for k, v in info.items():
        try:
            compile_args[k] = compile_args.get(k, []) + v
        except TypeError:
            continue

    # Check for the Cython source (development mode) and compile it if it
    # exists.
    solver_fn = os.path.join("genrp", "_genrp")
    if os.path.exists(solver_fn + ".pyx"):
        import shutil
        from Cython.Build import cythonize
        print("In dev mode...")

        solver_fn += ".pyx"

        # Copy the header files to this directory.
        dn = os.path.dirname
        incldir = os.path.join(dn(dn(os.path.abspath(__file__))), "cpp",
                               "include")
        headers = (
            glob.glob(os.path.join(incldir, "*", "*.h")) +
            glob.glob(os.path.join(incldir, "*", "*", "*.h"))
        )
        for fn in headers:
            dst = os.path.join(localincl, fn[len(incldir)+1:])
            try:
                os.makedirs(os.path.split(dst)[0])
            except os.error:
                pass
            shutil.copyfile(fn, dst)

    else:
        solver_fn += ".cpp"
        cythonize = lambda x: x

    ext = Extension("genrp._genrp",
                    sources=[solver_fn],
                    **compile_args)
    extensions = cythonize([ext])

    # Hackishly inject a constant into builtins to enable importing of the
    # package before the library is built.
    if sys.version_info[0] < 3:
        import __builtin__ as builtins
    else:
        import builtins
    builtins.__GENRP_SETUP__ = True
    import genrp

    print(glob.glob("genrp/include/genrp/*.h"))

    setup(
        name="genrp",
        version=genrp.__version__,
        author="Daniel Foreman-Mackey",
        author_email="foreman.mackey@gmail.com",
        url="https://github.com/dfm/genrp",
        license="MIT",
        packages=["genrp"],
        ext_modules=extensions,
        description="",
        long_description=open("README.rst").read(),
        cmdclass=dict(build_ext=build_ext),
        classifiers=[
            # "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
        ],
    )
