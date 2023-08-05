#ifndef PYTHONIC_INCLUDE_DISPATCH_COUNT_HPP
#define PYTHONIC_INCLUDE_DISPATCH_COUNT_HPP

#include "pythonic/include/utils/functor.hpp"

namespace pythonic
{

  namespace __dispatch__
  {
    template <class Any, class Value>
    auto count(Any &&any, Value &&value)
        -> decltype(any.count(std::forward<Value>(value)));

    DECLARE_FUNCTOR(pythonic::__dispatch__, count);
  }
}

#endif
