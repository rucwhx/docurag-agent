import argparse, pandas as pd
from pathlib import Path
def make_chunks(df: pd.DataFrame, chunk_size: int = 800, chunk_overlap: int = 200):
    rows=[]
    for i,r in df.iterrows():
        doc_id=str(r.get('id',i)); title=str(r.get('title','')); url=str(r.get('url','')); text=str(r.get('text',''))
        if not text: continue
        start=0; n=len(text)
        while start<n:
            end=min(n,start+chunk_size); chunk=text[start:end]
            rows.append({'doc_id':doc_id,'chunk_id':f'{doc_id}_{start}_{end}','title':title,'url':url,'text':chunk})
            if end==n: break
            start=max(end-chunk_overlap,start+1)
    return pd.DataFrame(rows)
if __name__=='__main__':
    import sys
    ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--output',required=True)
    ap.add_argument('--chunk_size',type=int,default=800); ap.add_argument('--chunk_overlap',type=int,default=200); a=ap.parse_args()
    df=pd.read_csv(a.input); out=make_chunks(df,a.chunk_size,a.chunk_overlap); Path(a.output).parent.mkdir(parents=True,exist_ok=True); out.to_parquet(a.output,index=False); print(len(out))