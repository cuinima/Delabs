import random


async def random_line(filepath: str, delete: bool = True):
    with open(filepath, 'r') as file:
        keys = file.readlines()

    if not keys:
        return False
    random_key = random.choice(keys)
    if delete:
        keys.remove(random_key)

        with open(filepath, 'w') as file:
            file.writelines(keys)

    return random_key.split("----")[1].strip()


def get_all_lines(filepath: str):
    with open(filepath, 'r') as file:
        keys = file.readlines()

    return [k.split("----")[1].strip() for k in keys]
