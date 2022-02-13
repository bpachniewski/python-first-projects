import pandas as pd
from pathlib import Path

data_folder = Path("data")
file_to_open = Path("data\CONTENT_INTERACTION\ViewingActivity.csv")
df = pd.read_csv(file_to_open)

df.shape

df = df.drop(["Attributes", "Supplemental Video Type", "Device Type", "Bookmark", "Latest Bookmark", "Country"], axis = 1)

df["Start Time"] = pd.to_datetime(df["Start Time"], utc = True)

df = df.set_index("Start Time")

df.index = df.index.tz_convert ("Europe/Warsaw")

df = df.reset_index()
