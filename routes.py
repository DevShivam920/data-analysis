from fastapi import APIRouter, UploadFile, File
from app.services.csv_service import process_csv, items  # absolute import

router = APIRouter()

# Get all items
@router.get("/items")
def get_items():
    return items

# Get single item by ID
@router.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id in items:
        return items[item_id]
    return {"error": "Item not found"}

# Upload CSV endpoint
@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    return await process_csv(file)