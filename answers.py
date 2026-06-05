import numpy as np

# Parameters for the Gaussian patch contact model (given)
n = 100
y = np.linspace(0, 10, n)
y_c = 5.0  # Contact center position
sigma = 0.4  # Width of the Gaussian contact patch
total_load = 1.0  # Total contact load

# ASSIGNMENT 1a: Solution for the Gaussian patch contact model ####################
p_gauss = np.exp(-0.5 * ((y - y_c) / sigma) ** 2)
p_gauss = total_load * p_gauss / np.sum(p_gauss)
###################################################################################

# ASSIGNMENT 1b: Solution for building the forward model matrix H
z_sensor = 1.0
H = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance = abs(y[i] - y[j])
        H[i, j] = 1.0 / (1.0 + (distance / z_sensor) ** 2) ** 2
        
# Normalize H so that each row sums to 1
H = H / H.sum(axis=1, keepdims=True)
####################################################################################

# ASSIGNMENT 1c: Solution for generating the sensor signal for the Gaussian patch ##
s_gauss = H @ p_gauss
####################################################################################

# Compare point contact and Gaussian patch models
p_point = np.zeros(n)
idx_c = np.argmin(np.abs(y - y_c))
p_point[idx_c] = total_load

# ASSIGNMENT 2: Solution for computing sensor signals for both models #############
s_point = H @ p_point
s_gauss = H @ p_gauss
###################################################################################

noise_level = 0.02  # 2% noise
rng = np.random.default_rng(0)
s_point_noisy = s_point + rng.normal(0, noise_level * np.max(s_point), size=n)
s_gauss_noisy = s_gauss + rng.normal(0, noise_level * np.max(s_gauss), size=n)

# ASSIGNMENT 3: Solution for implementing regularized least squares reconstruction #
lambda_reg = 0.01
I = np.eye(n)
p_point_reg = np.linalg.solve(H.T @ H + lambda_reg * I, H.T @ s_point_noisy)
p_gauss_reg = np.linalg.solve(H.T @ H + lambda_reg * I, H.T @ s_gauss_noisy)
####################################################################################