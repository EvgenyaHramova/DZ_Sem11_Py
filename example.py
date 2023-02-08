import numpy as np
import matplotlib.pyplot as plt

a, b, c, d, e = -12, -18, 5, 10, -30
limit = 10
step = 0.01
step_acr = 0.00001
line_style ='-'
color ='b'
direct_up = True


def switch_line():
    global line_style
    if line_style =='-':
        line_style = '--'
    else:
        line_style = '-'
    return line_style


def switch_color():
    global color
    if color =='b':
        color = 'r'
    else:
        color = 'b'
    return color

def func(x):
    f = a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 +d*x + e
    return f


#x = np.arange(-limit, limit, step)
x = np.arange(-limit, limit + step, step) # во избежание разрыва графика добавляем +step
#x_change = [-limit]
x_change = [(-limit, 'limit')]

#цикл для определения корней
for i in range(len(x) - 1):
    if func(x[i]) > 0 and func(x[i+1]) < 0 or func(x[i]) < 0 and func(x[i+1]) > 0:
        # для точности нахождения точек пересечения графика с осью х
        x_acr = np.arange(x[i], x[i+1] + step_acr, step_acr)
        for j in range(len(x_acr) - 1):
            if func(x_acr[j]) > 0 and func(x_acr[j + 1]) < 0 or func(x_acr[j]) < 0 and func(x_acr[j+1]) > 0:
        # добавляем точки пересечения с осью х в виде кортежа (координата, 0)
                x_change.append((x_acr[j], 'zero')) 
    if direct_up:
        if func(x[i]) > func(x[i+1]):
            direct_up = False
            x_change.append((x[i], 'dir')) # добавление точек изменения направления
    else:
        if func(x[i]) < func(x[i+1]):
            direct_up = True
            x_change.append((x[i], 'dir'))

x_change.append((limit, 'limit'))
print(x_change)

for i in range(len(x_change) - 1):
    cur_x = np.arange(x_change[i][0], x_change[i + 1][0] + step, step) # во избежание разрыва графика добавляем +step
    if x_change[i][1] == 'zero':
        plt.plot(x_change[i][0], func(x_change[i][0]), 'go') # обозначаем корни
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), color)
        #x_change.append(x[i])
    else:
        plt.plot(cur_x, func(cur_x), switch_color())


#plt.plot(x, func(x), 'b') #отрисовка графика
plt.grid()
plt.show()