//==============================================================================
//         Copyright 2003 - 2012   LASMEA UMR 6602 CNRS/Univ. Clermont II
//         Copyright 2009 - 2012   LRI    UMR 8623 CNRS/Univ Paris Sud XI
//
//          Distributed under the Boost Software License, Version 1.0.
//                 See accompanying file LICENSE.txt or copy at
//                     http://www.boost.org/LICENSE_1_0.txt
//==============================================================================
#ifndef NT2_TRIGONOMETRIC_FUNCTIONS_COTD_HPP_INCLUDED
#define NT2_TRIGONOMETRIC_FUNCTIONS_COTD_HPP_INCLUDED
#include <nt2/include/functor.hpp>


namespace nt2 { namespace tag
  {
   /*!
     @brief cotd generic tag

     Represents the cotd function in generic contexts.

     @par Models:
        Hierarchy
   **/
    struct cotd_ : ext::elementwise_<cotd_>
    {
      /// @brief Parent hierarchy
      typedef ext::elementwise_<cotd_> parent;
    };
  }
  /*!
    cotangent of input in degree.

    @par Semantic:

    For every parameter of floating type T0

    @code
    T0 r = cotd(x);
    @endcode

    is similar to:

    @code
    T0 r = cot(Deginrad<T0>()*x);
    @endcode

    @see @funcref{cot}, @funcref{cotangent}, @funcref{fast_cotd},
    @param a0

    @return a value of the same type as the parameter
  **/
  NT2_FUNCTION_IMPLEMENTATION(tag::cotd_, cotd, 1)
}

#endif


