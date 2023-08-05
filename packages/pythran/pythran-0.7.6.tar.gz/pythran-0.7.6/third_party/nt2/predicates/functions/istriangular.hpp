//==============================================================================
//         Copyright 2003 - 2012   LASMEA UMR 6602 CNRS/Univ. Clermont II
//         Copyright 2009 - 2012   LRI    UMR 8623 CNRS/Univ Paris Sud XI
//         Copyright 2011 - 2012   MetaScale SAS
//
//          Distributed under the Boost Software License, Version 1.0.
//                 See accompanying file LICENSE.txt or copy at
//                     http://www.boost.org/LICENSE_1_0.txt
//==============================================================================
#ifndef NT2_PREDICATES_FUNCTIONS_ISTRIANGULAR_HPP_INCLUDED
#define NT2_PREDICATES_FUNCTIONS_ISTRIANGULAR_HPP_INCLUDED

/*!
  @file
  @brief Defines the istriangular function
**/

#include <nt2/include/functor.hpp>

namespace nt2
{
  namespace tag
  {
    /*!
      @brief Tag for istriangular functor
    **/
    struct istriangular_ : boost::dispatch::tag::formal_
    {
      typedef boost::dispatch::tag::formal_ parent;
    };
  }

  /*!
    @brief Is an expression triangular ?

    Checks if an expression is a triangular matrix.

    @param a0 Expression to inspect

    @return Boolean value evaluating to the result of the test
  **/
  NT2_FUNCTION_IMPLEMENTATION(nt2::tag::istriangular_, istriangular, 1)
}

#endif

