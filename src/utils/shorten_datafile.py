DATAFILE_PATH: str = "data/rockyou.txt"
SAMPLE_PATH: str = "data/small_sample.txt"


def take_sample(
    source_path: str,
    destination_path: str,
    fraction: int,
) -> None:
    with open(source_path) as source:
        with open(destination_path, mode="w+") as destination:
            for line_num, line in enumerate(source):
                is_even: bool = line_num % fraction == 0 
                if is_even:
                    destination.write(line)


if __name__ == "__main__":
    take_sample(
        source_path=DATAFILE_PATH,
        destination_path=SAMPLE_PATH,
        fraction=1000
    )