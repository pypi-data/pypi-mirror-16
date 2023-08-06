# HF XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# HF X
# HF X   f90wrap: F90 to Python interface generator with derived type support
# HF X
# HF X   Copyright James Kermode 2011
# HF X
# HF X   These portions of the source code are released under the GNU General
# HF X   Public License, version 2, http://www.gnu.org/copyleft/gpl.html
# HF X
# HF X   If you would like to license the source code under different terms,
# HF X   please contact James Kermode, james.kermode@gmail.com
# HF X
# HF X   When using this software, please cite the following reference:
# HF X
# HF X   http://www.jrkermode.co.uk/f90wrap
# HF X
# HF XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

"""
f90wrap.runtime

Contains everything needed by f90wrap generated Python modules at runtime
"""

from f90wrap.fortrantype import (FortranDerivedType,
                                FortranDerivedTypeArray,
                                FortranModule)
from f90wrap.arraydata import get_array
from f90wrap.sizeof_fortran_t import sizeof_fortran_t as _sizeof_fortran_t

sizeof_fortran_t = _sizeof_fortran_t()
empty_handle = [0]*sizeof_fortran_t
empty_type = FortranDerivedType.from_handle(empty_handle)
