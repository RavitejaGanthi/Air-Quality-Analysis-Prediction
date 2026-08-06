from src.model_loader import label_encoders


def encode_input(data: dict):
    """
    Encode categorical columns using saved LabelEncoders.
    """

    data["state"] = label_encoders["state"].transform(
        [data["state"]]
    )[0]

    data["city"] = label_encoders["city"].transform(
        [data["city"]]
    )[0]

    data["pollutant_id"] = label_encoders["pollutant_id"].transform(
        [data["pollutant_id"]]
    )[0]

    return data