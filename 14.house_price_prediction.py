import numpy as np

house_size = np.array([500, 800, 1000, 1200, 1500])
price = np.array([2000000, 3000000, 3800000, 4500000, 5500000])

mean_x = np.mean(house_size)
mean_y = np.mean(price)

b1 = np.sum((house_size - mean_x) * (price - mean_y)) / np.sum((house_size - mean_x) ** 2)
b0 = mean_y - b1 * mean_x

predicted_price = b0 + b1 * house_size

new_house_size = 1000
new_price = b0 + b1 * new_house_size

print("Intercept:", int(b0))
print("Slope:", int(b1))
print("Predicted Prices:")
print(predicted_price.astype(int))
print("Predicted Price for house size", new_house_size, "sqft:", int(new_price))
