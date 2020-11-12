#include <stdio.h>
#include "../utils.h"


int main(void)
{
	unsigned long long p, n = 10000000;
	int i = 0;
	bool *primes = sieve_of_eratosthenes(n);
	
	for (p = 103301; i < 100; p += 2)
		if (primes[p]) {
			printf("%Lu ", p);
			i++, p += 3301;
		}


	free(primes);
	return 0;
}
