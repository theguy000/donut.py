import math
import time

ANGLE1_SPEED = 0.04
ANGLE2_SPEED = 0.02

def run():
    angle1 = 0
    angle2 = 0
    while True:
        z_buffer = [0]*1760
        output = [' ']*1760
        for theta in range(0,628,int(0.07*100)):
            for phi in range(0,628,int(0.02*100)):
                sin_phi = math.sin(phi)
                cos_theta = math.cos(theta)
                sin_angle1 = math.sin(angle1)
                sin_theta = math.sin(theta)
                cos_angle1 = math.cos(angle1)
                cos_theta_plus_2 = cos_theta + 2
                distance = 1 / (sin_phi * cos_theta_plus_2 * sin_angle1 + sin_theta * cos_angle1 + 5)
                cos_phi = math.cos(phi)
                cos_angle2 = math.cos(angle2)
                sin_angle2 = math.sin(angle2)
                term = sin_phi * cos_theta_plus_2 * cos_angle1 - sin_theta * sin_angle1
                x = int(40 + 30 * distance * (cos_phi * cos_theta_plus_2 * cos_angle2 - term * sin_angle2))
                y = int(12 + 15 * distance * (cos_phi * cos_theta_plus_2 * sin_angle2 + term * cos_angle2))
                index = x + 80 * y
                illumination_index = int(8 * ((sin_theta * sin_angle1 - sin_phi * cos_theta * cos_angle1) * cos_angle2 - sin_phi * cos_theta * sin_angle1 - sin_theta * cos_angle1 - cos_phi * cos_theta * sin_angle2))
                if 0 <= y < 22 and 0 <= x < 80 and distance > z_buffer[index]:
                    z_buffer[index] = distance
                    output[index] = ".,-~:;=!*#$@"[illumination_index if illumination_index > 0 else 0]

        print('\033[0;0H' + ''.join(output))
        time.sleep(0.01)
        angle1 += ANGLE1_SPEED
        angle2 += ANGLE2_SPEED

if __name__ == "__main__":
    run()