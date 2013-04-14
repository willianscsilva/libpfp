from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import commands,re,sys
if len(sys.argv) == 2:
    arg = sys.argv[1]
    if arg == "build" or arg == "install":
        ext_modules = [Extension("pfp_string", ["pfp_string.pyx"]),]
        for e in ext_modules:
            e.pyrex_directives = {"boundscheck": False}
            setup(
                name = "LibPFP",
                cmdclass = {"build_ext": build_ext},
                ext_modules = ext_modules
            )