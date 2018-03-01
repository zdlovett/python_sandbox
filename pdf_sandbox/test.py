
def pdf2df(pdf):
    rows = []
    page = 0
    for result in pdf.pq("*"):
        layout = result.layout
        if layout is not None:
            try:
                page = layout.pageid
            except AttributeError:
                pass
            d = {}
            d['x0'] = layout.x0
            d['x1'] = layout.x1
            d['y0'] = layout.y0
            d['y1'] = layout.y1
            try:
                d['text'] = layout.get_text()
            except AttributeError:
                d['text'] = ""
            d['layout'] = layout
            d['page'] = page
            rows.append(d)
    return pd.DataFrame(rows)

df = pdf2df(pdf) 
df.sort_values( by=['page', 'y0'], inplace=True ) 

def select_column(df, x0, x1, invert=True):
    "return everthing in the given column"
    if invert:
        x0 = 792 - x0
        x1 = 792 - x1
    col_df = df[ df['x0'] > x0 ][ df['x1'] < x1 ]
    return col_df

seq_col = select_column(df, 730, 498)
xcor_col = select_column(df, 500, 475)
delcn_col = select_column(df, 440, 410)
raw_seq = select_column(df, 350, 329)
fil_seq = select_column(df, 262, 241)
raw_ref = select_column(df, 175, 148)
fil_ref = select_column(df, 87, 67)

# select the gi| values
gil_df = df[ df['text'].str.contains('gi\|') ]
gil_df = gil_df[ gil_df['x0'] == 39.72 ]


def strip_column(col):
    "strip the duplicated values from the column and return a numeric version of the text field"
    col = col.drop_duplicates( subset=['page', 'y0', 'y1'] )
    col = col.loc[ col['y1'] - col['y0'] < 15, :  ]
    return col

fil_ref = strip_column(fil_ref)
gil_df = strip_column(gil_df)

output_df = pd.concat( [ gil_df, fil_ref ] )
output_df['inv_page'] = (1 + output_df['page'].max()) - output_df['page']
output_df.sort_values( ['inv_page', 'y0'], inplace=True, ascending=False)


