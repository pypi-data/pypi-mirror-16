
Patch conda dylibs with @rpath/name. Most conda packages have this,
but some old packages not built with conda-build (python itself, mkl) don't have this,
which causes many runtime compilation tools to fail.


