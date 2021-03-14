import pickle
import numpy as np

scaler = pickle.load(open('scaler.pkl', 'rb'))

def prepare_to_model(features):
	categorical = []

	for i in range(5):
		categorical += list(features.values())[i]

	categorical = np.array(list(map(int, categorical))).reshape(1, 11)

	numeric = list(features.values())[5:8]
	numeric = np.array(list(map(float, numeric)))
	numeric = scaler.transform(numeric.reshape(1, 3))

	to_model = np.concatenate((categorical, numeric), axis=1).reshape(1, 14)
	
	return to_model


def prepare_to_html(features):
	input_data = []

	# Кузов
	if features['body']=="10000":
		input_data.append("Внедорожник")
	elif features['body']=="01000":
		input_data.append("Кроссовер")
	elif features['body']=="00100":
		input_data.append("Минивэн")
	elif features['body']=="00010":
		input_data.append("Седан")
	elif features['body']=="00001":
		input_data.append("Универсал")
	elif features['body']=="00000":
		input_data.append("Хэтчбек")

	# Коробка передач
	if features['transmission'] == "1":
		input_data.append("Автомат")
	elif features['transmission'] == "0":
		input_data.append("Механика")

	# Руль
	if features['wheel'] == "1":
		input_data.append("Слева")
	elif features['wheel'] == "0":
		input_data.append("Справа")

	# Привод
	if features['drive']=="10":
		input_data.append("Задний привод")
	elif features['drive']=="01":
		input_data.append("Передний привод")
	elif features['drive']=="00":
		input_data.append("Полный привод")

	# Топливо
	if features['fuel']=="10":
		input_data.append("Бензин")
	elif features['fuel']=="01":
		input_data.append("Газ-Бензин")
	elif features['fuel']=="00":
		input_data.append("Дизель")

	input_data.extend([features['year'], features['mileage'], features['volume']])

	return input_data

# {'body': '00010', 'transmission': '0', 
# 'wheel': '1', 'drive': '01', 'fuel': '10', 'year': '2014', 
# 'mileage': '330000', 'volume': '1.6'}