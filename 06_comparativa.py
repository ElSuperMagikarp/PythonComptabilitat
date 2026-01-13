def iteratiu(b, n):
    resultat = b
    for i in range(1,n):
        resultat = resultat * b
    return resultat

def recursiu(b, n):
    if n == 0:
        return 1
    else:
        subresultat = recursiu(b, n-1)
        return b * subresultat
    
def recursiuMillorat(b, n):
    if n == 0:
        return 1
    elif n%2 == 0:
        subresultat = recursiu(b, n/2)
        return subresultat * subresultat
    else:
        subresultat = recursiu(b, (n-1)/2)
        return subresultat * subresultat * b


# PROGRAMA PRINCIPAL
import time

b = int(input("Valor de b: "))
n = int(input("Valor de n: "))

tempsIniciIteratiu = time.perf_counter_ns()
iteratiu(b, n)
tempsFiIteratiu = time.perf_counter_ns()

tempsIniciRecursiu = time.perf_counter_ns()
recursiu(b, n)
tempsFiRecursiu = time.perf_counter_ns()

tempsIniciRecursiuMillorat = time.perf_counter_ns()
recursiuMillorat(b, n)
tempsFiRecursiuMillorat = time.perf_counter_ns()

print("Iteratiu: ", tempsFiIteratiu-tempsIniciIteratiu, "nanosegons")
print("Rescursiu:", tempsFiRecursiu-tempsIniciRecursiu, "nanosegons")
print("Rescursiu Millorat:", tempsFiRecursiuMillorat-tempsIniciRecursiuMillorat, "nanosegons")