from fastapi import FastAPI,Path,HTTPException,Query
import json
app = FastAPI()

def load_data():
    with open("data.json", "r",encoding="utf-8") as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {'message':'my API management system'}

@app.get("/about")
def about():
    return {'message':'a fully functional API to manage infomation'}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/info/{id}")
def view_id(id : str = Path(..., description="ID of an person in DB",example="NV001")):
    data = load_data()
    if id in data:
        return data[id]
    raise HTTPException(status_code =404, detail="ID not found")


@app.get("/sort")
def sort_id(sort_by: str = Query(..., description="sort by info,work detail,management detail,.."), order: str = Query("asc", description="sort by asc or desc order")):
    valid_field = ['thong_tin_co_ban', 'chi_tiet_cong_viec', 'chi_tiet_quan_ly', 'du_lieu_mua_hang']
    
    
    if sort_by not in valid_field:
        raise HTTPException(status_code=400, detail=f"invalid selection from {valid_field}")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="invalid select asc or desc")
    
    data = load_data()
    
    sort_oder = True if order == "desc" else False

    sorted_by_info = sorted(
        data.values(),

        key=lambda x: x.get('thong_tin_co_ban', {}).get(sort_by, 0),
        reverse=sort_oder
    )
    
    return sorted_by_info

#http://127.0.0.1:8000/sort?sort_by=thong_tin_co_ban&order=asc
