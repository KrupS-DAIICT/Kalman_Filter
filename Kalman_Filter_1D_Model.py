import numpy as np
import matplotlib.pyplot as plt

ini_estimate = 0
ini_err_estimate = 20
ini_masurement = 100
ini_err_masurement = 30


def Kalman_Gain(err_estimate, err_masurement):
    return err_estimate / (err_estimate + err_masurement)


def curr_estimate(K_gain, mesurement, prev_estimate):
    return prev_estimate + K_gain*(mesurement - prev_estimate)


def curr_err_estimate(K_gain, prev_err_estimate):
    return (1 - K_gain)*prev_err_estimate


itr = 1000

# Generates Random values according to ini_measurement and error in initial measurement
kalman_values = np.array([])
measurements = np.random.randint(
    ini_masurement-ini_err_masurement, ini_masurement+ini_err_masurement, itr)
# print(measurements)
calculated_values = np.zeros(itr)

for curr_itr in range(itr):
    if curr_itr == 0:
        # Calculate following values for the first iteration from initial values
        curr_gain = Kalman_Gain(ini_err_estimate, ini_err_masurement)
        curr_esti = curr_estimate(curr_gain, ini_masurement, ini_estimate)
        curr_err = curr_err_estimate(curr_gain, ini_err_estimate)

    else:
        # Calculate following values from the previous values
        curr_gain = Kalman_Gain(prev_err, ini_err_masurement)
        curr_esti = curr_estimate(
            prev_gain, measurements[curr_itr], prev_esti)
        curr_err = curr_err_estimate(curr_gain, prev_err)

    prev_gain = curr_gain
    prev_esti = curr_esti
    prev_err = curr_err

    kalman_values = np.append(kalman_values, prev_gain)

    calculated_values[curr_itr] = prev_esti

# print(calculated_values)
estimated_temp = np.zeros(itr)
temp_range = np.arange(0, 150, 1)
temp = np.mean(temp_range)
print(temp)
for i in range(itr):
    estimated_temp[i] = temp

plt.plot(range(1, itr+1), calculated_values, label="Calculated Values")
# plt.scatter(range(1, itr+1), measurements, label="Measurements")
plt.plot(range(itr), estimated_temp, label="Estimated Temprature")
plt.legend()
plt.xlabel("Number of iterations")
plt.ylabel("Temprature Values")
plt.show()


# plt.plot(kalman_values)
# plt.show()
