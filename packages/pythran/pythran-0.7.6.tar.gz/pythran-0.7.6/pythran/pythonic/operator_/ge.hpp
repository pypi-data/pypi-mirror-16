#ifndef PYTHONIC_OPERATOR_GE_HPP
#define PYTHONIC_OPERATOR_GE_HPP

#include "pythonic/include/operator_/ge.hpp"

#include "pythonic/utils/functor.hpp"

namespace pythonic
{

  namespace operator_
  {
    template <class A, class B>
    auto ge(A const &a, B const &b) -> decltype(a >= b)
    {
      return a >= b;
    }

    DEFINE_FUNCTOR(pythonic::operator_, ge);
  }
}

#endif
