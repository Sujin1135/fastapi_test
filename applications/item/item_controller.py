from fastapi import APIRouter
from starlette.status import HTTP_200_OK

from applications.commons.CONST_VARS import responses
from applications.domains.dtos.item import Item

item_router = APIRouter()


@item_router.get('/item',
                 status_code=HTTP_200_OK,
                 responses={**responses},
                 response_model_exclude_unset=True,
                 tags=['item controller', 'get'])
def get_all_items():
    """
    Get all of items
    \f
    :return: all of item list
    """
    items = [
        Item(
            name='long_sword',
            damage=500,
            capacity=10,
            repairable=True
        ),
        Item(
            name='wood_wand',
            damage=350,
            capacity=10,
            repairable=True
        )
    ]
    return items
