//==============================================================================
//         Copyright 2003 - 2011   LASMEA UMR 6602 CNRS/Univ. Clermont II
//         Copyright 2009 - 2011   LRI    UMR 8623 CNRS/Univ Paris Sud XI
//
//          Distributed under the Boost Software License, Version 1.0.
//                 See accompanying file LICENSE.txt or copy at
//                     http://www.boost.org/LICENSE_1_0.txt
//==============================================================================
#ifndef NT2_IEEE_FUNCTIONS_MINNUMMAG_HPP_INCLUDED
#define NT2_IEEE_FUNCTIONS_MINNUMMAG_HPP_INCLUDED

#include <boost/simd/ieee/include/functions/minnummag.hpp>
#include <nt2/include/functor.hpp>

/* Automatically generated for module core.base */

namespace nt2
{
  namespace tag
  {
    #ifdef DOXYGEN_ONLY
    /*! \brief Same as \classref{boost::simd::tag::minnummag_} **/
    struct minnummag_ {};
    #endif
    using boost::simd::tag::minnummag_;
  }

  #ifdef DOXYGEN_ONLY
  /*! \brief Same as \funcref{boost::simd::minnummag} **/
  template<class... Args>
  details::unspecified minnummag(Args&&... args);
  #endif
  using boost::simd::minnummag;
}

#endif
