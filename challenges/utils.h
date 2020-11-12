#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

/* isprime: determines if n is prime */
bool isprime(unsigned long long n)
{
	if (!(n & 1) || n == 1) return false;

	unsigned int sqrt_n = sqrt(n) + 1;

	for (int i = 3; i <= sqrt_n; i += 2)
		if (!(n % i)) return false;

	return true;
}


/* isprime_cons_odd: checks if n is a prime number
 *
 * Similar to Standard primality test
 * but with optimizations for constantly ascending odd inputs.
 * Inputs must be odd, starting from 3 and skip no primes. */
bool isprime_cons_odd(int n, int *p)
{
	static int *q;
	int sqrt_n = sqrt(n) + 1;

	while (*p && *p < sqrt_n) {
		if (!(n % *p++)) return false;
	}

	if (!*p) q = p; // Only first time
	*q++ = n;
	return true;
}


/* sieve_of_eratosthenes: returns a pointer to (the first element of)
 * an array denoting primes (and composites) 0 <= p <= n
 * according to the original algorithm */
bool *sieve_of_eratosthenes(int n)
{
	bool *arr = malloc((n+1) * sizeof(bool));
	int p = 2, q, sqrt_n = sqrt(n) + 1;

	arr[0] = arr[1] = false;
	while (p <= n) arr[p++] = true;

	if (2 <= n)
		for (q = 4; q <= n; q += 2)
			arr[q] = false;
	for (p = 3; p <= sqrt_n; p += 2)
		if (arr[p])
			for (q = p*p; q <= n; q += p)
				arr[q] = false;

	return arr;
}


/* itoa: converts integer to character string */
char *itoa(long long n)
{
	char *num = malloc(50), *p = num, *q;
	bool sign = (n < 0) ? 1 : 0;

	if (sign) *p++ = '-';

	// Convert digits to characters
	do {
		*p++ = n % 10 + '0';
		n /= 10;
	}
	while (n);
	*p = '\0';

	// Reverse string
	q = p - 1, p = num + sign;
	while (p < q) {
		char temp = *p;
		*p++ = *q;
		*q-- = temp;
	}

	return num;
}


/* itoa_128: converts 128-bit integer to character string */
char *itoa_128(__int128 n)
{
	char *num = malloc(50), *p = num, *q;
	bool sign = (n < 0) ? 1 : 0;

	if (sign) *p++ = '-';

	// Convert digits to characters
	do {
		*p++ = n % 10 + '0';
		n /= 10;
	}
	while (n);
	*p = '\0';

	// Reverse string
	q = p - 1, p = num + sign;
	while (p < q) {
		char temp = *p;
		*p++ = *q;
		*q-- = temp;
	}

	return num;
}
