import java.util.ArrayList;

public class GoldbachConjecture {
	
	private static ArrayList<Integer> getPrimes (int n) {
		ArrayList<Integer> primes = new ArrayList<>();
		
		for (int i = 2; i < n; i++) {
			boolean isPrime = true;
			for (int j = 2; j < i; j++) {
				if (i % j == 0) {
					isPrime = false;
				}
			}
			if (isPrime) {
				primes.add(i);
			}
		}
		return primes;
	}
	
	public static void goldbachWeakConjecure(int n) {
		ArrayList<Integer> primes = getPrimes(n);
		
		for (int i = 0; i < primes.size(); i++) {
			for (int j = i; j < primes.size(); j++) {
				for (int k = j; k < primes.size(); k++) {
					if (primes.get(i) + primes.get(j) + primes.get(k) == n) {
						System.out.println(n + " = " + primes.get(i) + " + " + primes.get(j) + " + " + primes.get(k));
					}
				}
			}
		}
		// System.out.println(primes);
	}
}