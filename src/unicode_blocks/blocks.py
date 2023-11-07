import re


class UnicodeBlocks:
    def __init__(self, block_file: str):
        with open(block_file) as f:
            blocks = []

            for next_line in f.readlines():
                # NOTE: match example
                # 3040..309F; Hiragana -> (3040, 309F, Hiragana)
                found = re.findall(
                    r"^([0-9A-Za-z]+)?\.\.([0-9A-Za-z]+).*?;(.+)?$", next_line
                )
                if not found:
                    continue

                begin, end, name = found[0]
                begin, end, name = int(begin, base=16), int(end, base=16), name.strip()

                blocks.append({"begin": begin, "end": end, "name": name})

        self.blocks = blocks

    def get_block_name(self, chr: str) -> str | None:
        if len(chr) > 1:
            raise

        codepoint = ord(chr)

        for next_block in self.blocks:
            if next_block["begin"] <= codepoint <= next_block["end"]:
                return next_block["name"]

        return None
