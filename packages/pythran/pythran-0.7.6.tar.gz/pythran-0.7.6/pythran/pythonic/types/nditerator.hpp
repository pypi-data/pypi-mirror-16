#ifndef PYTHONIC_TYPES_NDITERATOR_HPP
#define PYTHONIC_TYPES_NDITERATOR_HPP

#include "pythonic/include/types/nditerator.hpp"

#include <iterator>

namespace pythonic
{

  namespace types
  {
    // FIXME: should use the same structure as the numpy_expr iterators
    /* Iterator over whatever provides a fast(long) method to access its element
     */
    template <class E>
    nditerator<E>::nditerator(E &data, long index)
        : data(data), index(index)
    {
    }

    template <class E>
    auto nditerator<E>::operator*() -> decltype(data.fast(index))
    {
      return data.fast(index);
    }

    template <class E>
    auto nditerator<E>::operator*() const -> decltype(data.fast(index))
    {
      return data.fast(index);
    }

    template <class E>
    nditerator<E> &nditerator<E>::operator++()
    {
      ++index;
      return *this;
    }

    template <class E>
    nditerator<E> &nditerator<E>::operator--()
    {
      --index;
      return *this;
    }

    template <class E>
    nditerator<E> &nditerator<E>::operator+=(long i)
    {
      index += i;
      return *this;
    }

    template <class E>
    nditerator<E> &nditerator<E>::operator-=(long i)
    {
      index -= i;
      return *this;
    }

    template <class E>
    nditerator<E> nditerator<E>::operator+(long i) const
    {
      nditerator<E> other(*this);
      other += i;
      return other;
    }

    template <class E>
    nditerator<E> nditerator<E>::operator-(long i) const
    {
      nditerator<E> other(*this);
      other -= i;
      return other;
    }

    template <class E>
    long nditerator<E>::operator-(nditerator<E> const &other) const
    {
      return index - other.index;
    }

    template <class E>
    bool nditerator<E>::operator!=(nditerator<E> const &other) const
    {
      return index != other.index;
    }

    template <class E>
    bool nditerator<E>::operator==(nditerator<E> const &other) const
    {
      return index == other.index;
    }

    template <class E>
    bool nditerator<E>::operator<(nditerator<E> const &other) const
    {
      return index < other.index;
    }

    template <class E>
    nditerator<E> &nditerator<E>::operator=(nditerator<E> const &other)
    {
      assert(&data == &other.data);
      index = other.index;
      return *this;
    }

    /* Const iterator over whatever provides a fast(long) method to access its
     * element
     */
    template <class E>
    const_nditerator<E>::const_nditerator(E const &data, long index)
        : data(data), index(index)
    {
    }

    template <class E>
    auto const_nditerator<E>::operator*() const -> decltype(data.fast(index))
    {
      return data.fast(index);
    }

    template <class E>
    const_nditerator<E> &const_nditerator<E>::operator++()
    {
      ++index;
      return *this;
    }

    template <class E>
    const_nditerator<E> &const_nditerator<E>::operator--()
    {
      --index;
      return *this;
    }

    template <class E>
    const_nditerator<E> &const_nditerator<E>::operator+=(long i)
    {
      index += i;
      return *this;
    }

    template <class E>
    const_nditerator<E> &const_nditerator<E>::operator-=(long i)
    {
      index -= i;
      return *this;
    }

    template <class E>
    const_nditerator<E> const_nditerator<E>::operator+(long i) const
    {
      const_nditerator<E> other(*this);
      other += i;
      return other;
    }

    template <class E>
    const_nditerator<E> const_nditerator<E>::operator-(long i) const
    {
      const_nditerator<E> other(*this);
      other -= i;
      return other;
    }

    template <class E>
    long const_nditerator<E>::operator-(const_nditerator<E> const &other) const
    {
      return index - other.index;
    }

    template <class E>
    bool const_nditerator<E>::operator!=(const_nditerator<E> const &other) const
    {
      return index != other.index;
    }

    template <class E>
    bool const_nditerator<E>::operator==(const_nditerator<E> const &other) const
    {
      return index == other.index;
    }

    template <class E>
    bool const_nditerator<E>::operator<(const_nditerator<E> const &other) const
    {
      return index < other.index;
    }

    template <class E>
    const_nditerator<E> &const_nditerator<E>::
    operator=(const_nditerator const &other)
    {
      index = other.index;
      return *this;
    }
#ifdef USE_BOOST_SIMD
    template <class E>
    const_simd_nditerator<E>::const_simd_nditerator(E const &data, long index)
        : data(data), index(index)
    {
    }

    template <class E>
    auto const_simd_nditerator<E>::operator*() const
        -> decltype(data.load(index))
    {
      return data.load(index);
    }

    template <class E>
    const_simd_nditerator<E> &const_simd_nditerator<E>::operator++()
    {
      index += vector_size;
      return *this;
    }

    template <class E>
    const_simd_nditerator<E> &const_simd_nditerator<E>::operator--()
    {
      index -= vector_size;
      return *this;
    }

    template <class E>
    const_simd_nditerator<E> &const_simd_nditerator<E>::operator+=(long i)
    {
      index += i * vector_size;
      return *this;
    }

    template <class E>
    const_simd_nditerator<E> &const_simd_nditerator<E>::operator-=(long i)
    {
      index -= i * vector_size;
      return *this;
    }

    template <class E>
    const_simd_nditerator<E> const_simd_nditerator<E>::operator+(long i) const
    {
      const_simd_nditerator<E> other(*this);
      other += i;
      return other;
    }

    template <class E>
    const_simd_nditerator<E> const_simd_nditerator<E>::operator-(long i) const
    {
      const_simd_nditerator<E> other(*this);
      other -= i;
      return other;
    }

    template <class E>
    long const_simd_nditerator<E>::
    operator-(const_simd_nditerator<E> const &other) const
    {
      return (index - other.index) / vector_size;
    }

    template <class E>
    bool const_simd_nditerator<E>::
    operator!=(const_simd_nditerator<E> const &other) const
    {
      return index != other.index;
    }

    template <class E>
    bool const_simd_nditerator<E>::
    operator==(const_simd_nditerator<E> const &other) const
    {
      return index == other.index;
    }

    template <class E>
    bool const_simd_nditerator<E>::
    operator<(const_simd_nditerator<E> const &other) const
    {
      return index < other.index;
    }

    template <class E>
    const_simd_nditerator<E> &const_simd_nditerator<E>::
    operator=(const_simd_nditerator const &other)
    {
      index = other.index;
      return *this;
    }
#endif

    // build an iterator over T, selecting a raw pointer if possible
    template <bool is_strided>
    template <class T>
    auto make_nditerator<is_strided>::operator()(T &self, long i)
        -> decltype(nditerator<T>(self, i)) const
    {
      return nditerator<T>(self, i);
    }

    template <class T>
    typename T::dtype *make_nditerator<false>::operator()(T &self, long i) const
    {
      return self.buffer + i;
    }

    template <bool is_strided>
    template <class T>
    auto make_const_nditerator<is_strided>::operator()(T const &self, long i)
        -> decltype(const_nditerator<T>(self, i)) const
    {
      return const_nditerator<T>(self, i);
    }

    template <class T>
    typename T::dtype const *make_const_nditerator<false>::
    operator()(T const &self, long i) const
    {
      return self.buffer + i;
    }
  }
}

#endif
