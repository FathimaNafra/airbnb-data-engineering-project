import pandas as pd
from datetime import datetime


def log_metadata(
        dataset,
        status,
        rows
):

    metadata = pd.DataFrame(
        [{
            "dataset": dataset,
            "status": status,
            "rows": rows,
            "timestamp":
                datetime.now()
        }]
    )

    metadata.to_csv(
        "data/metadata/metadata_log.csv",
        mode="a",
        index=False,
        header=False
    )