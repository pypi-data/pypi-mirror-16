#ifndef PYTHONIC_OPERATOR_ISNOT_HPP
#define PYTHONIC_OPERATOR_ISNOT_HPP

#include "pythonic/include/operator_/is_not.hpp"

#include "pythonic/utils/functor.hpp"

namespace pythonic
{

  namespace operator_
  {

    template <class A, class B>
    auto is_not(A const &a, B const &b) -> decltype(a != b)
    {
      return a != b;
    }

    DEFINE_FUNCTOR(pythonic::operator_, is_not);
  }
}

#endif
