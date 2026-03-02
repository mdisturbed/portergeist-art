#!/usr/bin/env python3
import urllib.request, os, concurrent.futures

urls = [
    # Halloween flash page 2 (Peanuts, Hex Girls, mummy)
    ("flash-halloween-1.jpg", "https://scontent-ord5-1.cdninstagram.com/v/t51.82787-15/558307495_18418815493110564_7691277576078794404_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=111&ig_cache_key=MzczNTM2MTgzMzc2NDI0MjEzNA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=YlvWAqKH5UAQ7kNvwHvqkEZ&_nc_oc=AdkM7w7x4S96m0RhU_5q-aWgpQDohrWJ3LO-9MfvmyVR8nrTwKz_JJc9lV__EtATH3g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ord5-1.cdninstagram.com&_nc_gid=7hq5hGuSuRb6V9UbUTcRQQ&_nc_ss=8&oh=00_Afw0Mzp-HZvpeyoxpbcP_Shzh2lKK4MJZaSjpmp_UclCrA&oe=69AAD65B"),
    # Halloween flash page 2 slide 2
    ("flash-halloween-2.jpg", "https://scontent-ord5-2.cdninstagram.com/v/t51.82787-15/559741728_18418815502110564_4610801476720932849_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=MzczNTM2MTgzMzc4MTAwMzYzOQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=VdyJede4AuMQ7kNvwE8qFv_&_nc_oc=AdlxCk8WSU_POdiIo8ip8tMioy39A5gpRJqwksWwZjuBEYaFnDOouRt-WyOrmsZsr7w&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ord5-2.cdninstagram.com&_nc_gid=7hq5hGuSuRb6V9UbUTcRQQ&_nc_ss=8&oh=00_AfwGiHgw9UpTMUbVUDWlsTA9X0U05Qc7Iv9F69NfCdxrWA&oe=69AAB2DC"),
]

outdir = os.path.expanduser("~/clawd/portergeist-art/images")
def download(item):
    name, url = item
    path = os.path.join(outdir, name)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=15).read()
        if len(data) > 1000:
            with open(path, "wb") as f: f.write(data)
            return f"OK {name}: {len(data)} bytes"
        return f"FAIL {name}: {len(data)} bytes"
    except Exception as e:
        return f"ERR {name}: {e}"

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
    for r in ex.map(download, urls): print(r)
