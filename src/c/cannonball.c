// Finding cannonball numbers that are equal to a polygonal number of the same
// base. See https://www.youtube.com/watch?v=q6L06pyt9CA

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Macro to calculate the n-th polygonal number of side s. It's a macro so I
// don't have to keep typing it but it stays efficient.
// There also also some other macros with the nth term of a cannonball number
#define POLYGONAL(s, n) ((n * n * (s - 2) - n * (s - 4)) >> 1)
#define CANNON(s, n) n * (n + 1) * ((s - 2) * (2 * n + 1) - 6 * (s - 4)) / 12
// Symbolic constants for the default values of the parameters
#define MAX_CHECK_DEFAULT ipow(10, 11)
#define MAX_BASE_DEFAULT 31265
// How many numbers to check before giving an update
#define INNER_UPDATE ipow(10, 6) * 5

// integer type being used to represent cannonball numbers
typedef __int128_t cannonball_int;
// maximum possible amount of memory needing to be allocated to represent a
// cannonball_int in base 10 (in an ASCII-encoded string)
#define CANNON_INT_STR_LEN (int)(sizeof(cannonball_int) * log10(0xff) + 2)

// custom function to format a cannonball int into a base 10 string, as printf
// doesn't know how.
void fmt_c(cannonball_int n, char *target) {
    ssize_t i = 0;
    ssize_t size;
    cannonball_int tmp;
    while (n != 0) {
        target[i++] = '0' + (n % 10);
        n = n / 10;
    }
    size = i;
    target[size--] = '\0';
    // reverse it because we built the string back to front
    for (i--; i > size - i; i--) {
        tmp = target[i];
        target[i] = target[size - i];
        target[size - i] = tmp;
    }
}

// Integer exponentiation by squaring - basically just so I can write integers
// in standard form.
cannonball_int ipow(cannonball_int base, cannonball_int exp) {
    cannonball_int result = 1;
    while (exp) {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }
    return result;
}

// Find the integer square root, with the bit-shifting algorithm. This is used
// when applying the quadratic formula to see if there are rational solutions.
cannonball_int isqrt(cannonball_int n) {
    cannonball_int small, large;
    if (n < 2) {
        return n;
    } else {
        small = isqrt(n >> 2) << 1;
        large = small + 1;
        if (large * large > n) {
            return small;
        } else {
            return large;
        }
    }
}

// Routine to check all cannonball numbers of side `base` up to `max` to see if
// they are also a polyhedral number of side `base`.
void check_base(cannonball_int base, cannonball_int max_check,
                cannonball_int max_base) {
    char *c_1 = malloc(CANNON_INT_STR_LEN),
         *c_2 = malloc(CANNON_INT_STR_LEN),
         *c_3 = malloc(CANNON_INT_STR_LEN),
         *c_4 = malloc(CANNON_INT_STR_LEN);
    cannonball_int i, cannonballs;
    cannonball_int discriminant, discriminant_sqrt, numerator, denominator;
    denominator = 2 * base - 4;
    for (  i = 2, cannonballs = 1 + POLYGONAL(base, 2);
           cannonballs <= max_check;
           i++, cannonballs += POLYGONAL(base, i)) {
        if ((i - 2) % INNER_UPDATE == 0) {
            fmt_c(base, c_1);
            fprintf(stderr, "\r%3.0f%% %3.0f%% %s",
                    100.0 * base / max_base,
                    100.0 * pow(1.0 * cannonballs / max_check, 1.0 / 3),
                    c_1);
            fflush(stderr);
        }
        discriminant = (base - 4) * (base - 4) + 8 * (base - 2) * cannonballs;
        discriminant_sqrt = isqrt(discriminant);
        if (discriminant_sqrt * discriminant_sqrt == discriminant) {
            numerator = base - 4 + discriminant_sqrt;
            if (numerator % denominator == 0) {
                // not using %n$ syntax but just passing the same argument twice
                // because of something something ISO C
                fmt_c(cannonballs, c_1);
                fmt_c(base, c_2);
                fmt_c(numerator / denominator, c_3);
                fmt_c(i, c_4);
                fprintf(stderr, "\r");
                printf(">%s == P(%s, %s) == C(%s, %s)\n",
                       c_1, c_2, c_3, c_2, c_4);
            }
        }
    }
    free(c_1); free(c_2); free(c_3); free(c_4);
}

int main(int argc, char **argv) {
    cannonball_int base,
                   max_check = MAX_CHECK_DEFAULT,
                   max_base = MAX_BASE_DEFAULT;
    char *c_1 = malloc(CANNON_INT_STR_LEN),
         *c_2 = malloc(CANNON_INT_STR_LEN);
    if (argc >= 2) {
        max_check = (cannonball_int)strtold(argv[1], NULL);
    }
    if (argc >= 3) {
        max_base = (cannonball_int)strtold(argv[2], NULL);
    }
    fmt_c(max_check, c_1);
    fmt_c(max_base, c_2);
    printf("Finding polygonal cannonball numbers <= %s, with base <= %s\n",
           c_1, c_2);
    printf("Using integers of width %zu bytes, which go up to about %.5e\n",
           sizeof(cannonball_int), exp(log(0xff) * sizeof(cannonball_int)));
    for (base = 3; base <= max_base; base++) {
        check_base(base, max_check, max_base);
    }
    free(c_1); free(c_2);
    return 0;
}
