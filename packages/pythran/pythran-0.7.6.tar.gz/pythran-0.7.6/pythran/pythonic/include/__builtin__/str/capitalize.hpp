#ifndef PYTHONIC_INCLUDE_BUILTIN_STR_CAPITALIZE_HPP
#define PYTHONIC_INCLUDE_BUILTIN_STR_CAPITALIZE_HPP

#include "pythonic/include/types/str.hpp"
#include "pythonic/include/utils/functor.hpp"

namespace pythonic
{

  namespace __builtin__
  {

    namespace str
    {

      types::str capitalize(types::str const &s);

      DECLARE_FUNCTOR(pythonic::__builtin__::str, capitalize);
    }
  }
}
#endif
