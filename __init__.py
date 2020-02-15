def f(integer):
    """
    factorcalc.f(int > 0) -> list of int -- provides a list of all the factors of the first argument
    """

    if type(integer)==int:
        if integer>0:
            possible_factors=[integer]
            possible_factor=integer-1
            for i in range(integer):
                possible_factors.append(possible_factor)
                possible_factor-=1

            possible_factors.remove(0)
            index=0
            factors=[]

            for i in possible_factors:
                if str(integer/possible_factors[index]).endswith('0'):
                    factors.append(possible_factors[index])
                index+=1

            return factors


        else:
            raise ValueError('first argument must be > 0')


    else:
        raise TypeError('first argument must be <class \'int\'> (not '+str(type(integer))+')')



def gcf(num1,num2):
    """
    factorcalc.gcf(translatable to int, translatable to int) -> int -- provides the greatest common factor of the integers in the first argument
    """

    try:
        num1=int(num1)
    except:
        raise TypeError('first argument must be translatable to <class \'int\'>')

    try:
        num2=int(num2)
    except:
        raise TypeError('second argument must be translatable to <class \'int\'>')

    if num2>num1:
        num2copy=num2
        num2=num1
        num1=num2copy


    possible_greatest_common_factors=[]
    possible_greatest_common_factor=num1

    for i in range(num1):
        possible_greatest_common_factors.append(possible_greatest_common_factor)
        possible_greatest_common_factor-=1

    index=0

    for i in possible_greatest_common_factors:
        if possible_greatest_common_factors[index]in f(num1)and possible_greatest_common_factors[index]in f(num2):
            return possible_greatest_common_factors[index]
        index+=1



def prime(integer):
    """
    factorcalc.prime(int) -> bool -- checks if the first argument is prime
    """

    if type(integer)==int:
        if f(integer)==[integer,1]:
            return True
        else:
            return False


    else:
        raise TypeError('first argument must be <class \'int\'> (not '+str(type(integer))+')')



def primes(minimum,maximum):
    """
    factorcalc.primes(int,int) -> list of int -- returns all prime numbers within the range of the first and second arguments including the arguments themselves
    """

    if type(minimum)==int and type(maximum)==int:
        output=[]

        for target in range(minimum,maximum+1):
            if prime(target):
                output.append(target)

        return output


    if type(minimum)!=int:
        raise TypeError('first argument must be <class \'int\'> (not '+str(type(minimum))+')')

    else:
        raise TypeError('second argument must be <class \'int\'> (not '+str(type(minimum))+')')



def mult(number,quantity):
    """
    factorcalc.mult(int, int > 0) -> list of int -- returns a list containing, in order, multiples of the first argument with the second argument being its length
    This module does not relate to factor calculation but to multiple calculation. It has been added beause it might be of use.
    """

    if (type(number)==int or type(number)==float) and type(quantity)==int:
        if quantity>0:
            mults=[number]

            for i in range(quantity-1):
                mults.append(mults[-1]+number)

            return mults


        else:
            raise ValueError('second argument must be > 0')


    else:
        if type(number)!=int:
            raise TypeError('first argument must be <class \'int\'> or <class \'float\'> (not '+str(type(minimum))+')')
        else:
            raise TypeError('second argument must be <class \'int\'> (not '+str(type(minimum))+')')
