import math


class Conversion:
    @classmethod
    def __make_round(cls, num: float) -> int:
        is_positive = num >= 0
        do = round if num + 0.001 > math.ceil(num) else math.floor
        result = do(abs(num))
        return result if is_positive else -result

    @classmethod
    def __make_truncate(cls, num: float) -> float:
        factor = math.pow(10, 2)
        result = cls.__make_round(num * factor) / factor
        return result

    @classmethod
    def do(cls, half_scrap: float) -> float:
        return cls.__make_truncate(half_scrap * (1 / 18))
