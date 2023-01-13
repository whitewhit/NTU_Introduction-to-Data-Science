import math

def estimate_pi():
    pi_count = 0
    i = 0
    pi_reciprocal = 0
    const =  2*math.sqrt(2)/9801
    while abs(math.pi - pi_count) >= math.pow(10,-15):
        k1 = math.factorial(i)
        k2 = math.factorial(4*i)
        pi_reciprocal += k2*(1103 + 26390*i)/(math.pow(k1,4)*math.pow(396, 4*i))
        pi_count = 1/(pi_reciprocal*const)
        i+=1
        print(i, pi_count)
    print('k = ', i, 'pi = ', pi_count)

a = estimate_pi()