def data_schemas(data) -> dict:
    return {"id": str(data["_id"]),
            "name": data["name"],
            "node": data["node"],
            "data": data["data"],
            "time": data["time"]}
