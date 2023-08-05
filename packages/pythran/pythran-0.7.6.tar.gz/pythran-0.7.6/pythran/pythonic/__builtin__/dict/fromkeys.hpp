#ifndef PYTHONIC_BUILTIN_DICT_FROMKEYS_HPP
#define PYTHONIC_BUILTIN_DICT_FROMKEYS_HPP

#include "pythonic/include/__builtin__/dict/fromkeys.hpp"

#include "pythonic/types/dict.hpp"
#include "pythonic/utils/functor.hpp"

#include <type_traits>

namespace pythonic
{

  namespace __builtin__
  {

    namespace dict
    {

      template <class Iterable, class V>
      types::dict<typename std::remove_reference<Iterable>::type::value_type, V>
      fromkeys(Iterable &&iter, V const &v)
      {
        types::dict<typename std::remove_reference<Iterable>::type::value_type,
                    V> D =
            types::empty_dict(); // Allocate default capacity to dict
        for (auto const &i : iter)
          D[i] = v;
        return D;
      }

      DEFINE_FUNCTOR(pythonic::__builtin__::dict, fromkeys);
    }
  }
}

#endif
