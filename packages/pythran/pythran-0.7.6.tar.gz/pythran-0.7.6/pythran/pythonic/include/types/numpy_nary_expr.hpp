#ifndef NUMPY_NARY_FUNC_NAME
#error NUMPY_NARY_FUNC_NAME undefined
#endif

#ifndef NUMPY_NARY_FUNC_SYM
#error NUMPY_NARY_FUNC_SYM undefined
#endif

#ifndef NUMPY_NARY_RESHAPE_MODE
#define NUMPY_NARY_RESHAPE_MODE adapt_type
#endif

#ifndef NUMPY_NARY_EXTRA_METHOD
#define NUMPY_NARY_EXTRA_METHOD
#endif

#define STR_(a) #a
#define STR(a) STR_(a)

namespace functor
{

  struct NUMPY_NARY_FUNC_NAME {
    using callable = void;

    // We accept implementation here
    NUMPY_NARY_EXTRA_METHOD

    template <typename... T>
    auto operator()(T &&... args) const -> typename std::enable_if<
        utils::all_of<not types::is_numexpr_arg<typename std::remove_cv<
            typename std::remove_reference<T>::type>::type>::value...>::value,
        decltype(NUMPY_NARY_FUNC_SYM(std::forward<T>(args)...))>::type;

    template <class... E>
    typename std::enable_if<
        types::valid_numexpr_parameters<E...>::value,
        types::numpy_expr<
            NUMPY_NARY_FUNC_NAME,
            typename types::NUMPY_NARY_RESHAPE_MODE<E, E...>::type...>>::type
    operator()(E const &... args) const;
    friend std::ostream &operator<<(std::ostream &os, NUMPY_NARY_FUNC_NAME)
    {
      return os << STR(NUMPY_NARY_FUNC_NAME);
    }
  };
}

#undef NUMPY_NARY_FUNC_NAME
#undef NUMPY_NARY_FUNC_SYM
#undef NUMPY_NARY_RESHAPE_MODE
#undef NUMPY_NARY_EXTRA_METHOD
#undef STR
#undef STR_
