from conversion import Conversion
from prices import Price


def main(sku: str) -> None:
    price = Price()
    item = price.get_price(sku, 1, 1, "DESC")["items"][0]
    ref_buy = Conversion.do(item["buyHalfScrap"])
    ref_sell = Conversion.do(item["sellHalfScrap"])
    print(
        "\nMann Co. Supply Crate Key", f"SELL:\t{ref_sell}", f"BUY:\t{ref_buy}", sep="\n"
    )


if __name__ == "__main__":
    data = input("Enter SKU: ")
    main(str(data))
