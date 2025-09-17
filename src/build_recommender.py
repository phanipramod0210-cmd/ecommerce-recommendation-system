#!/usr/bin/env python3
import argparse, pandas as pd, os, joblib

def main(args):
    df = pd.read_csv(args.data)
    pop = df.groupby('item_id').agg({'qty':'sum'}).sort_values('qty', ascending=False)
    top_items = pop.index.tolist()
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    joblib.dump(top_items, args.out)
    print('Saved popularity model with', len(top_items),'items.')

if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--data', required=True)
    p.add_argument('--out', default='model/als_model.joblib')
    args=p.parse_args()
    main(args)
