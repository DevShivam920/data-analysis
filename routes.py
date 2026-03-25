from fastapi import APIRouter, UploadFile, File
from ..services.csv_service import process_csv, items

router = APIRouter()

@router.get("/items")
def get_items():
    return items

@router.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id in items:
        return items[item_id]
    return {"error": "Item not found"}

@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    return await process_csv(file)