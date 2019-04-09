// As yet unused pitiful attempt at writing a biginteger type

#include <stdint.h>
#include <stdlib.h>

typedef uint32_t bigint_digit;
typedef uint64_t bigint_carry;

typedef struct bigint {
    size_t size;
    bigint_digit* digits;
} bigint;
