from conversion import Conversion
from prices import Price
from item_model import Items


def main(sku: str) -> None:

    price = Price()
    item_data = price.get_price(sku, 1, 1, "DESC")
    item = Items(**item_data)

    key_buy = item.items[0].buy_keys
    key_sell = item.items[0].sell_keys

    ref_buy = Conversion.do(item.items[0].buy_half_scrap)
    ref_sell = Conversion.do(item.items[0].sell_half_scrap)

    return print(
        f"\n{sku}",
        f"SELL:\t{key_sell} key {ref_sell} ref",
        f"BUY:\t{key_buy} key {ref_buy} ref\n",
        sep="\n"
    )


if __name__ == "__main__":
    while True:
        data = input("Enter SKU: ")
        main(str(data))
