import numpy as np
import matplotlib.pyplot as plt


c = 3e8


d1 = 1
p1 = -121


d2 = 36
p2 = -119


d3 = 101
p3 = -138


d1 = d1 * 1000
d2 = d2 * 1000
d3 = d3 * 1000


t1 = d1 / c * 1000000
t2 = d2 / c * 1000000
t3 = d3 / c * 1000000


t2_rel = t2 - t1
t3_rel = t3 - t1


print("Задержки:")
print("Прямой луч:", round(t1, 1), "мкс")
print("Первое отражение:", round(t2, 1), "мкс")
print("Второе отражение:", round(t3, 1), "мкс")


a1 = 1
a2 = 10 ** ((p2 - p1) / 20)
a3 = 10 ** ((p3 - p1) / 20)


print("\nАмплитуды:")
print("Прямой луч:", round(a1, 3))
print("Первое отражение:", round(a2, 3))
print("Второе отражение:", round(a3, 3))


N = 450
t = np.arange(N)


h = np.zeros(N)
h[0] = a1
h[round(t2_rel)] = a2
h[round(t3_rel)] = a3


x = np.zeros(N)
x[0] = 1


y = np.zeros(N)


for i in range(N):
    for j in range(N):
        if i + j < N:
            y[i + j] = y[i + j] + x[i] * h[j]


print("\nВыход совпадает с h:", np.allclose(y, h))


np.random.seed(0)
noise = np.random.normal(0, 0.05, N)
y_noisy = y + noise



x_rect = np.zeros(N)


for i in range(150):
    x_rect[i] = 1


dt = 1.0
y_rect = np.zeros(N)

for i in range(N):
    for k in range(N):
        j = i - k

        if 0 <= j < N:
            y_rect[i] += x_rect[k] * h[j] * dt


plt.subplot(2, 2, 1)
plt.stem(t, x, markerfmt=" ")
plt.title("Входной дельта-импульс")
plt.xlabel("Время, мкс")
plt.grid(True)


plt.subplot(2, 2, 2)
plt.stem(t, h)
plt.title("Импульсная характеристика канала")
plt.xlabel("Время, мкс")
plt.grid(True)


plt.subplot(2, 2, 3)
plt.plot(t, y_noisy)
plt.title("Выходной сигнал с шумом")
plt.xlabel("Время, мкс")
plt.grid(True)


plt.subplot(2, 2, 4)
plt.plot(t, x_rect, label="Вход")
plt.plot(t, y_rect, label="Выход")
plt.title("Прямоугольный импульс и эхо")
plt.xlabel("Время, мкс")
plt.legend()
plt.grid(True)


plt.tight_layout()
plt.show()