#ifndef PYTHONIC_INCLUDE_NUMPY_FLOAT_HPP
#define PYTHONIC_INCLUDE_NUMPY_FLOAT_HPP

#include "pythonic/include/numpy/float64.hpp"

namespace pythonic
{

  namespace numpy
  {
#define NUMPY_NARY_FUNC_NAME float_
#define NUMPY_NARY_FUNC_SYM details::float64
#define NUMPY_NARY_EXTRA_METHOD using type = double;
#include "pythonic/include/types/numpy_nary_expr.hpp"
  }
}

#endif
