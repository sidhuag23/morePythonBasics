from sympy import *
x = symbols('x')
y = symbols('y')

def firstEquation(p,q):
    equationLHS = (p>>q)
    equationRHS = (~p|q)
    test_equavalance = Equivalent(equationLHS,equationRHS)
    test_equals = equationLHS.equals(equationRHS)
    print(test_equals)
    print(test_equavalance)
    print(simplify(test_equavalance))
    print(simplify_logic(test_equavalance))

def secondEquation(p,q):
    equationLHS = Equivalent(p,q)
    equationRHS = ( (p & q) | (~p & ~q) )
    test_equavalance = Equivalent(equationLHS,equationRHS)
    test_equals = equationLHS.equals(equationRHS)
    print(test_equals)
    print(test_equavalance)
    print(simplify(test_equavalance))
    print(simplify_logic(test_equavalance))

def thirdEquation(p,q):
    equationLHS = (~( p & q))
    equationRHS = (~p | ~q)
    test_equavalance = Equivalent(equationLHS,equationRHS)
    print(test_equavalance)
    print(simplify(test_equavalance))
    print(simplify_logic(test_equavalance))

    
firstEquation(x,y)
secondEquation(x,y)
thirdEquation(x,y)
