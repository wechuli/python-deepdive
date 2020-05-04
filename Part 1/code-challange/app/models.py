import re


class BouqetDesign:
    def __init__(self, bouqet_design_raw: str):

        self._bouqet_design_raw = bouqet_design_raw
        self.parse_bouqet_string()

    def parse_bouqet_string(self) -> dict:

        self._bouqet_name = self._bouqet_design_raw[0]
        self._bouqet_size = self._bouqet_design_raw[1]
        number = re.compile(r"(?P<flower_q>\d+)$")
        res = number.search(self._bouqet_design_raw)

        self._flower_quantity = int(res.group("flower_q"))

        flower_reg = re.compile(r"\d+[a-z]")

        all_flowers_raw = flower_reg.findall(self._bouqet_design_raw)

        self._flowers = {}

        for raw_flower in all_flowers_raw:
            parsed_flower = BouqetDesign.extract_flower_and_quantity(
                raw_flower, self._bouqet_size)
            self._flowers[parsed_flower[0]] = parsed_flower[1]

    def get_bouqet_design(self):
        return {
            "raw_design_string": self._bouqet_design_raw,
            "bouqet_name": self._bouqet_name,
            "bouqet_size": self._bouqet_size,
            "flowers": self._flowers,
            "flower_quantity": self._flower_quantity
        }

    @classmethod
    def extract_flower_and_quantity(cls, flower_with_quantity: str, flower_size: str) -> tuple:
        flower_regex = re.compile(r"(?P<quantity>\d+)(?P<species>[a-z]{1})")
        matches = flower_regex.search(flower_with_quantity)
        quantity = int(matches.group("quantity"))
        species = matches.group("species")
        return (species+flower_size, quantity)


buoqet_design = BouqetDesign("BS10b5c16")
print(buoqet_design.get_bouqet_design())
