import tabula
from column_values import columns
from typing import Dict
import os


def convert_to_csv(file_name: str, columns: Dict = columns, rename_columns=False):
    path = "pdf_inputs/" + file_name
    dfs = tabula.read_pdf(path, multiple_tables=False, pages="all")
    df = dfs[0].dropna().copy()
    if rename_columns:
        df.loc[max(df.index) + 1, :] = df.columns.tolist()
        df.rename(columns=columns, inplace=True)
        df.sort_values(by="County", inplace=True)

    df.to_csv("csv_outputs/" + file_name.split(".")[0] + "csv", index=False)

    return df


if __name__ == "__main__":
    df_list = []
    if not os.path.isdir("pdf_inputs"):
        print("create a directory named pdf_inputs and copy your pdf files into it")
        raise FileNotFoundError
    if not os.path.isdir("csv_inputs"):
        os.mkdir("csv_outputs")
    for file_name in os.listdir("pdf_inputs"):
        df_obj = convert_to_csv(file_name, rename_columns=True, columns=columns)
        df_list.append(df_obj)
