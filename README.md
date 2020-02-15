## factorcalc
### several (currently 5) modules relating to factor and multiple calculation<br/><br/>

### VERSION: 0.1.2<br/>
##### What's new?<br/>&nbsp;&nbsp;&nbsp;&nbsp;changed the description on PyPI<br/>&nbsp;&nbsp;&nbsp;&nbsp;added mult()<br/>&nbsp;&nbsp;&nbsp;&nbsp;added README.md<br/><br/><br/>


*factor.f(integer)*<br/>&nbsp;&nbsp;&nbsp;&nbsp;factor.f(int) -> list of int -- provides a list of all the factors of the first argument

*factor.gcf(num1, num2)*<br/>&nbsp;&nbsp;&nbsp;&nbsp;factor.gcf(translatable to int, translatable to int) -> int -- provides the greatest common factor of the integers in the first argument

*factor.prime(integer)*<br/>&nbsp;&nbsp;&nbsp;&nbsp;factor.prime(int) -> bool -- checks if the first argument is prime

*factor.primes(minimum, maximum)*<br/>&nbsp;&nbsp;&nbsp;&nbsp;factor.primes(int, int) -> list of int -- returns all prime numbers within the range of the first and second arguments including the arguments themselves

*mult(number, quantity)*<br/>&nbsp;&nbsp;&nbsp;&nbsp;factorcalc.mult(int, int > 0) -> list of int -- returns a list containing, in order, multiples of the first argument with the second argument being its length<br/>&nbsp;&nbsp;&nbsp;&nbsp;This module does not relate to factor calculation but to multiple calculation. It has been added beause it might be of use.
