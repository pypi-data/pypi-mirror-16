//==============================================================================
//         Copyright 2003 - 2011 LASMEA UMR 6602 CNRS/Univ. Clermont II
//         Copyright 2009 - 2011 LRI    UMR 8623 CNRS/Univ Paris Sud XI
//
//          Distributed under the Boost Software License, Version 1.0.
//                 See accompanying file LICENSE.txt or copy at
//                     http://www.boost.org/LICENSE_1_0.txt
//==============================================================================
#ifndef NT2_EXPONENTIAL_FUNCTIONS_COMPLEX_GENERIC_EXPIPI_HPP_INCLUDED
#define NT2_EXPONENTIAL_FUNCTIONS_COMPLEX_GENERIC_EXPIPI_HPP_INCLUDED

#include <nt2/exponential/functions/expipi.hpp>
#include <nt2/include/functions/real.hpp>
#include <nt2/include/functions/imag.hpp>
#include <nt2/include/functions/is_imag.hpp>
#include <nt2/include/functions/multiplies.hpp>
#include <nt2/include/functions/bitwise_cast.hpp>
#include <nt2/include/functions/simd/exp.hpp>
#include <nt2/include/functions/simd/logical_or.hpp>
#include <nt2/include/functions/simd/exp.hpp>
#include <nt2/include/functions/simd/is_equal.hpp>
#include <nt2/include/functions/simd/sincospi.hpp>
#include <nt2/include/functions/simd/if_else.hpp>
#include <nt2/include/functions/simd/unary_minus.hpp>
#include <nt2/include/functions/simd/mul_i.hpp>
#include <nt2/include/constants/pi.hpp>
#include <nt2/include/constants/inf.hpp>
#include <nt2/include/constants/zero.hpp>
#include <nt2/sdk/complex/meta/as_complex.hpp>
#include <nt2/sdk/complex/meta/as_real.hpp>
#include <nt2/sdk/complex/meta/as_dry.hpp>

namespace nt2 { namespace ext
{
  NT2_FUNCTOR_IMPLEMENTATION( nt2::tag::expipi_, tag::cpu_
                            , (A0)
                            , (generic_< complex_<floating_<A0> > >)
                            )
  {
    typedef A0 result_type;
    NT2_FUNCTOR_CALL(1)
    {
      typedef typename meta::as_real<A0>::type rtype;
      rtype c, s;
      sincospi(nt2::real(a0), s, c);
      rtype rho = nt2::exp(-nt2::Pi<rtype>()*nt2::imag(a0));
      return  nt2::if_else(logical_or(is_imag(a0), eq(nt2::imag(a0), nt2::Inf<rtype>())),
                     result_type(rho, Zero<rtype>()),
                     result_type(rho*c, rho*s));
    }
  };

  NT2_FUNCTOR_IMPLEMENTATION( nt2::tag::expipi_, tag::cpu_
                            , (A0)
                            , (generic_< floating_<A0 > >)
                            )
  {
    typedef typename meta::as_real<A0>::type             rtype;
    typedef typename meta::as_complex<rtype>::type result_type;
    NT2_FUNCTOR_CALL(1)
    {
      rtype c, s;
      nt2::sincospi(a0, s, c);
      return result_type(c, s);
    }
  };

  NT2_FUNCTOR_IMPLEMENTATION( nt2::tag::expipi_, tag::cpu_
                            , (A0)
                            , (generic_< dry_<floating_<A0> > >)
                            )
  {
    typedef A0 result_type;
    NT2_FUNCTOR_CALL(1)
    {
      return bitwise_cast<result_type>(nt2::expipi(nt2::real(a0)));
    }
  };
} }


#endif
