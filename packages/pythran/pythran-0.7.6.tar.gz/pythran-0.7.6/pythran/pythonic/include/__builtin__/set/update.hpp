#ifndef PYTHONIC_INCLUDE_BUILTIN_SET_UPDATE_HPP
#define PYTHONIC_INCLUDE_BUILTIN_SET_UPDATE_HPP

#include "pythonic/include/__dispatch__/update.hpp"
#include "pythonic/include/utils/functor.hpp"

namespace pythonic
{
  namespace __builtin__
  {
    namespace set
    {
      USING_FUNCTOR(update, pythonic::__dispatch__::functor::update);
    }
  }
}
#endif
