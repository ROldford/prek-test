import polars as pl
from loguru import logger

PENGUINS_DATASET_URL = (
    "https://raw.githubusercontent.com/openwashdata/"
    + "palmerpenguins/main/inst/extdata/penguins.csv"
)


def main():
    lf = pl.scan_csv(PENGUINS_DATASET_URL)
    lf = lf.with_columns(
        (pl.col("bill_length_mm") / pl.col("bill_depth_mm")).alias(
            "bill_length_to_depth_ratio"
        )
    )
    group_by_lf = lf.group_by("species", "sex").agg(
        pl.mean("bill_length_to_depth_ratio").alias("mean_bill_length_to_depth_ratio")
    )
    logger.info(group_by_lf.collect())


if __name__ == "__main__":
    main()
