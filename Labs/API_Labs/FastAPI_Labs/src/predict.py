import pickle
from data import WineData

def load_model():
    with open("../model/wine_model.pkl", "rb") as f:
        return pickle.load(f)

def predict_wine(data: WineData):
    model = load_model()
    features = [[
        data.alcohol, data.malic_acid, data.ash,
        data.alcalinity_of_ash, data.magnesium, data.total_phenols,
        data.flavanoids, data.nonflavanoid_phenols, data.proanthocyanins,
        data.color_intensity, data.hue, data.od280_od315, data.proline
    ]]
    result = model.predict(features)[0]
    wine_types = {
        0: "Barolo",
        1: "Grignolino",
        2: "Barbera"
    }
    return {"predicted_class": int(result), "wine_type": wine_types[result]}