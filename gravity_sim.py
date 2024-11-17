from decimal import Decimal, getcontext
import time
class gravitation():
    # Setting the precision of Decimal up to 25 digits
    getcontext().prec = 100
    
    def celestial_calculations(mAs1, mAs2, r, s):
        g = Decimal("0.00000000006673")
        m1 = gravitation.celestial_power(mAs1[0], mAs1[1])
        m2 = gravitation.celestial_power(mAs2[0], mAs2[1])
        # This code keeps the distance value within 100
        divider = Decimal((100 / r))
        # Settings the velocity for the acceleration calculations
        velocity = Decimal(0)
        cTime = time.perf_counter()
        while r > 0:
            # Calculating the force in newtons
            f = Decimal((g * m1 * m2) / (r * r))
            
            # This is the acceleration for the second object
            a = Decimal((f/m2) / 10)
            
            
            # Here I'm updating the velocity and distance over the simulated time
            velocity += a * s
            r -= velocity * s
            if r < 0:
                r = 0
            if cTime - time.perf_counter() <= -5:
                cTime = time.perf_counter()
                print(f"Velocity: {velocity:.2f} R Distance: {r:.2f}")
                
        main()
    
    def celestial_power(n, s):
        return Decimal(n) ** Decimal(s)
        
def main():
    mass1 = int(input("Gravity Simulater: SUPERSCRIPT 1: "))
    mass2 = int(input("Gravity Simulater: SUPERSCRIPT 2: "))
    r = int(input("Gravity Simulater: DISTANCE: "))
    simSpeed = int(input("Gravity Simulater: SPEED Multiplier for Simulation: "))
    gravitation.celestial_calculations([10, mass1], [10, mass2], r, simSpeed)
    
    
if __name__ == "__main__":
    main()
