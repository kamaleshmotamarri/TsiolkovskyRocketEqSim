import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.gridspec as gridspec

def get_float(prompt, default):
    while True:
        try:
            val = input(f"{prompt} [{default}]: ")
            if val.strip() == "":
                print("Invalid input, using default.")
                return default
            return float(val)
        except Exception:
            print("Invalid input, using default.")
            continue

print("Choose simulation mode:")
print("1. Tsiolkovsky Rocket Equation (ideal, no gravity or drag)")
print("2. Realistic Simulation (gravity and drag included)")
mode = input("Enter 1 or 2 [2]: ") or "2"

while mode not in ["1", "2"]:
    print("Invalid choice. Please enter 1 or 2.")
    mode = input("Enter 1 or 2 [2]: ") or "2"


if mode == "1":
    #Tsiolkovsky Rocket Equation 
    ve = get_float("Exhaust velocity (m/s)", 2500)
    mi = get_float("Initial mass (kg)", 500)
    mf = get_float("Final mass (kg)", 100)
    delta_v = ve * np.log(mi / mf)
    print(f"\nΔv (change in velocity) = {delta_v:.2f} m/s")
    print("This is the ideal rocket equation result (no gravity, no drag).")

    # Animation: velocity increases linearly from 0 to delta_v over "burn" time
    burn_time = 10  # seconds, just for animation effect
    times = np.linspace(0, burn_time, 200)
    velocities = np.linspace(0, delta_v, 200)

    fig, ax = plt.subplots()
    ax.set_xlim(0, burn_time)
    ax.set_ylim(0, delta_v * 1.1)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Velocity (m/s)")
    ax.set_title("Tsiolkovsky Rocket Equation: Δv Animation")
    line, = ax.plot([], [], 'orange', lw=2, label="Velocity")
    ax.legend()

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        line.set_data(times[:frame], velocities[:frame])
        return line,

    ani = FuncAnimation(fig, update, frames=len(times), init_func=init, blit=True, interval=20)
    plt.tight_layout()
    plt.show()


else:
    #Realistic Simulation
    ve = get_float("Exhaust velocity (m/s)", 2500)
    mi = get_float("Initial mass (kg)", 500)
    mf = get_float("Final mass (kg)", 100)
    burn_time = get_float("Burn time (s)", 50)
    A = get_float("Cross-sectional area (m^2)", 0.3)
    Cd = get_float("Drag coefficient", 0.5)

    g = 9.81
    rho = 1.225
    mass_flow_rate = (mi - mf) / burn_time
    dt = 0.1
    total_time = 100
    times = np.arange(0, total_time, dt)

    velocities, altitudes, accelerations, masses = [], [], [], []
    v, h, m = 0, 0, mi

    for t in times:
        if m > mf:
            thrust = ve * mass_flow_rate
            m -= mass_flow_rate * dt
        else:
            thrust = 0

        drag = 0.5 * rho * v**2 * Cd * A * np.sign(v)
        net_force = thrust - drag - m * g
        a = net_force / m
        v += a * dt
        h += v * dt

        velocities.append(v)
        altitudes.append(h)
        accelerations.append(a)
        masses.append(m)

        if h < 0:
            break  # Stop sim if rocket hits ground

    # Trim arrays to actual simulation length
    times = times[:len(altitudes)]

    # Animation setup
    fig = plt.figure(figsize=(10, 8))
    gs = gridspec.GridSpec(3, 1, height_ratios=[1, 1, 1])
    ax1, ax2, ax3 = plt.subplot(gs[0]), plt.subplot(gs[1]), plt.subplot(gs[2])
    line1, = ax1.plot([], [], 'r-', label="Altitude")
    line2, = ax2.plot([], [], 'b-', label="Velocity")
    line3, = ax3.plot([], [], 'g-', label="Acceleration")

    ax1.set_xlim(0, times[-1])
    ax2.set_xlim(0, times[-1])
    ax3.set_xlim(0, times[-1])

    ax1.set_ylim(0, max(altitudes) * 1.1)
    ax2.set_ylim(min(velocities) * 1.1, max(velocities) * 1.1)
    ax3.set_ylim(min(accelerations) * 1.1, max(accelerations) * 1.1)

    ax1.set_ylabel("Altitude (m)")
    ax2.set_ylabel("Velocity (m/s)")
    ax3.set_ylabel("Acceleration (m/s²)")
    ax3.set_xlabel("Time (s)")

    ax1.legend()
    ax2.legend()
    ax3.legend()

    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        line3.set_data([], [])
        return line1, line2, line3

    def update(frame):
        x = times[:frame]
        line1.set_data(x, altitudes[:frame])
        line2.set_data(x, velocities[:frame])
        line3.set_data(x, accelerations[:frame])
        return line1, line2, line3

    ani = FuncAnimation(fig, update, frames=len(times), init_func=init, blit=True, interval=30)
    plt.tight_layout()
    plt.show()
