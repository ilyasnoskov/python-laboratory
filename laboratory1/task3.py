print('Введіть будь-яке значення x')
import func

x = func.func("x:", float, None)
if x >= 3.5:
    var = 4 * x ** 2 + 2 * x - 19
elif x < 3.5:
    var = -2 * x / (-4 * x + 1)
print("Відповідь:", var)