#ifndef PYTHONIC_INCLUDE_NUMPY_RANDOM_CHOICE_HPP
#define PYTHONIC_INCLUDE_NUMPY_RANDOM_CHOICE_HPP

#include "pythonic/include/utils/functor.hpp"
#include "pythonic/include/numpy/random/randint.hpp"
#include "pythonic/include/types/ndarray.hpp"
#include "pythonic/include/types/tuple.hpp"

namespace pythonic
{
  namespace numpy
  {
    namespace random
    {
      template <size_t S, class P>
      types::ndarray<long, S> choice(long max,
                                     types::array<long, S> const &shape,
                                     bool replace, P const &p);

      template <class P>
      types::ndarray<long, 1> choice(long max, long size, bool replace, P &&p);

      template <class T>
      auto choice(long max, T &&size)
          -> decltype(randint(0, max, std::forward<T>(size)));

      long choice(long max);

      template <class T>
      typename T::dtype choice(T const &a);

      template <class T, size_t S>
      types::ndarray<typename T::dtype, S>
      choice(T const &a, types::array<long, S> const &shape);

      template <class T>
      types::ndarray<typename T::dtype, 1> choice(T &&a, long size);

      template <class T, size_t S, class P>
      types::ndarray<typename T::dtype, S>
      choice(T const &a, types::array<long, S> const &shape, bool replace,
             P const &p);

      template <class T, class P>
      types::ndarray<typename T::dtype, 1> choice(T &&a, long size,
                                                  bool replace, P &&p);

      DECLARE_FUNCTOR(pythonic::numpy::random, choice);
    }
  }
}

#endif
