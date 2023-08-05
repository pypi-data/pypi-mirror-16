#ifndef PYTHONIC_INCLUDE_NUMPY_EQUAL_HPP
#define PYTHONIC_INCLUDE_NUMPY_EQUAL_HPP

#include "pythonic/include/utils/functor.hpp"
#include "pythonic/include/types/ndarray.hpp"
#include "pythonic/include/types/numpy_broadcast.hpp"
#include "pythonic/include/utils/numpy_traits.hpp"
#include "pythonic/include/operator_/eq.hpp"

namespace pythonic
{

  namespace numpy
  {

#define NUMPY_NARY_FUNC_NAME equal
#define NUMPY_NARY_FUNC_SYM pythonic::operator_::eq
#include "pythonic/include/types/numpy_nary_expr.hpp"
  }
}

#endif
