def data_schemas(data) -> dict:
    return {"id": str(data["_id"]),
            "name": data["name"],
            "data0": data["data0"],
            "data1": data["data1"],
            "data2": data["data2"],
            "data3": data["data3"],
            "time": data["time"]}
