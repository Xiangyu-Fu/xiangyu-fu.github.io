import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 定义系统参数
m = 1.0   # 质量 (kg)
k = 20.0  # 刚度 (N/m)
c = 1.0   # 阻尼系数 (Ns/m)

# 计算固有频率和阻尼比
omega_n = np.sqrt(k / m)
zeta = c / (2 * np.sqrt(m * k))

# 定义二阶线性动力学系统的微分方程
def mass_spring_damper(t, y):
    x, v = y
    dxdt = v
    dvdt = -(c/m) * v - (k/m) * x
    return [dxdt, dvdt]

# 初始条件
x0 = 1.0  # 初始位移 (m)
v0 = 0.0  # 初始速度 (m/s)

# 时间范围
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# 使用 solve_ivp 求解微分方程
sol = solve_ivp(mass_spring_damper, t_span, [x0, v0], t_eval=t_eval)

# 提取解
t = sol.t
x = sol.y[0]
v = sol.y[1]

# 绘制结果
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='POS (x)')
plt.plot(t, v, label='VEL (v)')
plt.xlabel('TIME (s)')
plt.ylabel('response')
plt.title('Second Order System Response')
plt.legend()
plt.grid(True)
plt.show()
