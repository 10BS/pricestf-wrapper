from pydantic import BaseModel, Field
from datetime import datetime


class Item(BaseModel):
    sku: str
    buy_half_scrap: int = Field(alias="buyHalfScrap")
    buy_keys: int = Field(alias="buyKeys")
    sell_half_scrap: int = Field(alias="sellHalfScrap")
    sell_keys: int = Field(alias="sellKeys")
    created_at: datetime = Field(alias="createdAt")


class Metadata(BaseModel):
    total_items: int = Field(alias="totalItems")
    item_count: int = Field(alias="itemCount")
    items_per_page: int = Field(alias="itemsPerPage")
    total_pages: int = Field(alias="totalPages")
    current_page: int = Field(alias="currentPage")


class Items(BaseModel):
    items: list[Item]
    metadata: Metadata = Field(alias="meta")
