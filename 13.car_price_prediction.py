import numpy as np

car_age = np.array([1, 2, 3, 4, 5])
price = np.array([800000, 700000, 600000, 500000, 400000])

mean_x = np.mean(car_age)
mean_y = np.mean(price)

b1 = np.sum((car_age - mean_x) * (price - mean_y)) / np.sum((car_age - mean_x) ** 2)
b0 = mean_y - b1 * mean_x

predicted_price = b0 + b1 * car_age

new_car_age = 3
new_price = b0 + b1 * new_car_age

print("Intercept:", int(b0))
print("Slope:", int(b1))
print("Predicted Prices:")
print(predicted_price.astype(int))
print("Predicted Price for car age", new_car_age, ":", int(new_price))
