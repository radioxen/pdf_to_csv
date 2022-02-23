import tabula

dfs = tabula.read_pdf("input.pdf", multiple_tables=False, pages="all")

df = dfs[0].dropna().copy()

df.loc[max(df.index)+1, :] = df.columns.tolist()

df.rename(columns={'IMPERIAL COUNTY':"County",
                   'Brawley city':"Jurisdiction",
                   '25,800': "Population2012",
                   '34,600': "Population2020",
                   '40,600': "Population2035",
                   '42,900': "Population2040",
                   '7,600': "Household2012",
                   '11,400': "Household2020",
                   '14,100': "Household2035",
                   '15,000': "Household2040",
                   '8,000': "Employment2012",
                   '13,700': "Employment2020",
                   '16,300': "Employment2035",
                   '16,800': "Employment2040"}, inplace=True)

df.sort_values(by="County", inplace=True)