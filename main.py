import matplotlib.pyplot as plt
dv = 0.0001
V = 0.001
nu = 2
R = 8.31
T = 320
#пусть А = 1
A = 1
B = nu * R
p0 = B * T / V
p = p0
i = 1
while V < 0.0025:
    V = V+dv
    i = i+1
    p = p0
    T = p*V/B
    A = A + p * dv
    plt.scatter(V, p)
    plt.pause(0.05)
while V < 0.007:
    V = V + dv
    i = i + 1
    p = B * T / V
    A = A + p * dv
    plt.scatter(V, p)
    plt.pause(0.05)
    plt.grid(True)
    plt.title("p(V)")
plt.show()
V = 0.001
while V < 0.0025:
    V = V+dv
    i = i+1
    p = p0
    T = p*V/B
    A = A + p * dv
    plt.scatter(T, V)
    plt.pause(0.05)
while V < 0.007:
    V = V + dv
    i = i + 1
    p = B * T / V
    A = A + p * dv
    plt.scatter(T, V)
    plt.pause(0.05)
    plt.grid(True)
    plt.title("V(T)")
plt.show()

V = 0.001
while V < 0.0025:
    V = V+dv
    i = i+1
    p = p0
    T = p*V/B
    A = A + p * dv
    plt.scatter(T, p)
    plt.pause(0.05)
while V < 0.007:
    V = V + dv
    i = i + 1
    p = B * T / V
    A = A + p * dv
    plt.scatter(T, p)
    plt.pause(0.05)
    plt.grid(True)
    plt.title("p(T)")
plt.show()


