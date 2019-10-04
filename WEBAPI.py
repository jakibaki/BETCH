import BETCH
import hug
import pickle

@hug.get("/API/BETCH/ERRCODE")
async def betch_api(module_int: int, description_int: int):
    with open(f"data/errcodes.pkl", "rb") as betch:
        modules = pickle.load(betch)
    
    response = {"module_int": module_int, 
                "module_name": "Unknown",
                "description_int": description_int,
                "description_str": "Unknown"}
    
    if module_int in modules:
        if "name" in modules[module_int]:
            response["module_name"] = modules[module_int]["name"]
        if description_int in modules[module_int]:
            response["description_str"] = modules[module_int][description_int]
    
    return response

@hug.get("/API/BETCH/ALL")
async def all_errorcodes():
    with open(f"data/errcodes.pkl", "rb") as betch:
        modules = pickle.load(betch)
            
    return modules