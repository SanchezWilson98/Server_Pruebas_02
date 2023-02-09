def data_schemas(data) -> dict:
    return {"id": str(data["_id"]),
            "name": data["name"],
            "data": data["data"]}
