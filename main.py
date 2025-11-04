from typing import Dict, Optional
from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field

app = FastAPI(
    title="Restaurant POS API",
    description="API for managing restaurant point of sale operations",
    version="1.0.0"
)


#In Memory Store

STORE: Dict[int, dict] = {}
NEXT_ID = 1


class Menu(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    category: Optional[str] = None


class MenuPatch(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    price: Optional[float] = Field(None, gt=0)
    category: Optional[str] = None


@app.get('/')
def health_check():
    return {
        'status': True,
        'message': 'Service is up and running'
    }


@app.get('/menu/')
def menu_by_category(category: str, limit: int = 10, page: int = 1):
    """List menu items with query params 
       category, 
       limit and 
       pagination (page)"""

    results = [item for item in STORE.values() if item.get('category') == category]
    start = (page - 1) * limit
    end = start + limit
    return {
        'status': True,
        'data': results[start:end],
        'total': len(results),
        'page': page,
        'limit': limit
    }


@app.get('/menu/{item_id}')
def menu_by_id(item_id: int = Path(..., gt=0)):
    """Get menu item by ID"""
    item = STORE.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item


@app.post('/menu/')
def create_menu_item(menu: Menu):
    """Create item with POST (body)"""
    global NEXT_ID
    STORE[NEXT_ID] = menu.model_dump()
    NEXT_ID += 1
    return {
        'status': True,
        'message': 'Menu item created successfully',
        'id': NEXT_ID - 1,
        "menu": STORE[NEXT_ID - 1]
    }


@app.put('/menu/{item_id}')
def update_menu_item(item_id: int, menu: Menu):
    """Replace item with PUT (path + full body)"""
    if item_id not in STORE:
        raise HTTPException(status_code=404, detail="Menu item not found")
    STORE[item_id] = menu.model_dump()
    return {
        'status': True,
        'message': 'Menu item updated successfully',
        'id': item_id,
        "menu": STORE[item_id]
    }


@app.patch('/menu/{item_id}')
def partial_update_menu_item(item_id: int, menu: MenuPatch):
    """Update item with PATCH (path + partial body)"""
    if item_id not in STORE:
        raise HTTPException(status_code=404, detail="Menu item not found")

    update_data = menu.model_dump(exclude_unset=True)

    STORE[item_id].update(update_data)
    return {
        'status': True,
        'message': 'Menu item updated successfully',
        'id': item_id,
        "menu": STORE[item_id]
    }

