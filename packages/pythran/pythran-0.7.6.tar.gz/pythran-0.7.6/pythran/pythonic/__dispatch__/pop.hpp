#ifndef PYTHONIC_DISPATCH_POP_HPP
#define PYTHONIC_DISPATCH_POP_HPP

#include "pythonic/include/__dispatch__/pop.hpp"

#include "pythonic/utils/functor.hpp"

namespace pythonic
{

  namespace __dispatch__
  {
    template <class Any, class... Arg0>
    auto pop(Any &&any, Arg0 &&... arg0)
        -> decltype(any.pop(std::forward<Arg0>(arg0)...))
    {
      return any.pop(std::forward<Arg0>(arg0)...);
    }

    DEFINE_FUNCTOR(pythonic::__dispatch__, pop);
  }
}

#endif
