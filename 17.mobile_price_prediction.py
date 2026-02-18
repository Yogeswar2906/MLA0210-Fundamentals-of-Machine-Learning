import numpy as np

ram = np.array([2, 3, 4, 6, 8])
price = np.array([8000, 12000, 16000, 22000, 30000])

mean_x = np.mean(ram)
mean_y = np.mean(price)

b1 = np.sum((ram - mean_x) * (price - mean_y)) / np.sum((ram - mean_x) ** 2)
b0 = mean_y - b1 * mean_x

predicted_prices = b0 + b1 * ram

new_ram = 6
predicted_price = b0 + b1 * new_ram

print("Intercept:", int(b0))
print("Slope:", int(b1))
print("Predicted Prices:")
print(predicted_prices.astype(int))
print("Predicted Price for", new_ram, "GB RAM mobile:", int(predicted_price))
