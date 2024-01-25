import matplotlib.pyplot as plt

def chemical_reactor(A, B, C, k1, k2, end_time, dt): 
    time = 0
    substance_A = []
    substance_B = []
    substance_C = []
    time_points = []

    while (time <= end_time):
        substance_A.append(A)
        substance_B.append(B)
        substance_C.append(C)
        time_points.append(time)
        time += dt

        k1AB = k1 * A * B;
        k2C = k2 * C;
        A += (k2C - k1AB) * dt
        B += (k2C - k1AB) * dt
        C += (2 * k1AB - 2 * k2C) * dt

        plt.clf()
        plt.title("Simulation of a Chemical Reactor")
        plt.xlabel("Time (s)")
        plt.ylabel("Quantity (gm)")
        plt.xlim(0, end_time)
        plt.plot(time_points, substance_A, label = "Substance A")
        plt.plot(time_points, substance_B, label = "Substance B")
        plt.plot(time_points, substance_C, label = "Substance C")
        plt.legend()
        plt.grid()
        plt.pause(0.001)
        
    plt.show()

def main():
    chemical_reactor(100, 50, 0, 0.008, 0.002, 10, 0.1)
    
if __name__ == "__main__":
    main()