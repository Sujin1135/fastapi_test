from fastapi import APIRouter

from applications.item.item_controller import item_router

router = APIRouter()
router.include_router(item_router)
