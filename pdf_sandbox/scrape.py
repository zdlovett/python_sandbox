import pdfquery
from pdfquery.cache import FileCache
import sys
import time
from tqdm import tqdm
import pandas as pd

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

def select_column(df, x0, x1):
    "return everthing in the given column"
    col_df = df[ df['x0'] > x0 ][ df['x1'] < x1 ]
    return col_df

def strip_column(col):
    "strip the duplicated values from the column and return a numeric version of the text field"
    col = col.drop_duplicates( subset=['page', 'y0', 'y1'] )
    col = col.loc[ col['y1'] - col['y0'] < 15, :  ]
    return col

def main():
    filepath = sys.argv[1]
    
    print(f"reading pdf from:{filepath}")
    pdf = pdfquery.PDFQuery(filepath) # parse_tree_cacher=FileCache("./")
    s = time.monotonic()
    pdf.load()
    e = time.monotonic()
    print(f"Loaded file in {e-s} seconds.")

    from IPython import embed; embed()
    sys.exit(0)

    df = pdf2df(pdf)

    # select the gi| values
    gil_df = df[ df['text'].str.contains('gi\|') ]
    gil_df = gil_df[ gil_df['x0'] == 39.72 ]

    seq_df = select_column(df, 96, 300 )
    xcor_df = select_column(df, 350, 450)

if __name__ == "__main__":
    main()
    
