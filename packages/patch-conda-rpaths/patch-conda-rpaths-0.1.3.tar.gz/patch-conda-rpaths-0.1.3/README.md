# patch-conda-rpaths

Patch conda dylibs with @rpath/name. Most conda packages have this,
but some old packages not built with conda-build (python itself, mkl) don't,
which causes many runtime compilation tools to fail to link properly.

Usage:

    patch-conda-rpaths $PREFIX/lib

Hardlinks are broken, to avoid modifying the original conda files,
so only the given env is affected.

Only for use on OS X.

conda install:

    conda install -c minrk patch-conda-rpaths

