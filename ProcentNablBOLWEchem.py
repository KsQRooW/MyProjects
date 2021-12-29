from scipy.stats import norm
# Считается, что значение IQ (уровень интеллекта) у людей имеет нормальное распределение
# со средним значением равным 100 и стандартным отклонением равным 15 (M = 100, sd = 15).
# Какой приблизительно процент людей обладает IQ > 125?
mean = 100
std = 15
IQ = 125
# cdf - Cumulative distribution function
result = (1 - norm(mean, std).cdf(IQ)) * 100
print(f"{result:.2f}%")

# Какой приблизительно процент людей обладает IQ  на промежутке от 70 до 112
result = norm(mean, std).cdf(112) * 100 - norm(mean, std).cdf(70) * 100
print(f"{result:.2f}%")
