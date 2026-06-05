A simple script to determine if a number is prime and then if not, output the number's divisors.

What it does

- Accepts a number from user
- Checks whether the number has divisors other than 1 and itself
- Uses the square root of the number as the upper limit for checking divisibility. This reduces unnecessary processing time
- When a number is found to be a divisor, that number plus the number/divisor are added to a list
- Returns whether the number is prime
- If the number is not prime, returns a sorted list of divisors with duplicates removed.

Concepts practiced
- User input
- Type conversion
- Conditional logic
- lists
- for loops
- modulo operator
- Integer division

What I Improved
- Initial version checked every number up to the input
- Added input validation (only numbers above 2 or greater can be prime)

Future Improvements
- Visualization of numbers and their divisors
- Graphical visualization of the occurrence of prime numbers on a number line
