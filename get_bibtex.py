import sys

if __name__ == "__main__":
    import ads
    bibcode = sys.argv[1]
    q = ads.ExportQuery(bibcode, format='bibtex')
    sys.stdout.write(q().strip())
