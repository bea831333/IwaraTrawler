#!/usr/bin/env python3
#usage: trawl.py <node number start> <node number end>
#example: trawl.py 100000 100001

# both ends are inclusive, outputs to list.txt
import requests, zipfile, io, sys, re, base64, os

if __name__ == "__main__":

  f = open("list.txt", "w+")
  for x in range(int(sys.argv[1]),int(sys.argv[2]) + 1):
    file_url = ''.join(["https://ecchi.iwara.tv/node/", str(x)])

    page = requests.get(file_url)
    lines = page.text.splitlines()
    title = lines[3]
    canonical = lines[12]
    
    # print(title)
    matcher_1 = re.search('^.*title>(.*)</title>.*$', title)
    matcher_2 = re.search('^.*href="(.*)".*$', canonical)
    if (matcher_1 != None and matcher_2 != None):
      result = ''.join([str(x), ": ", matcher_1.group(1), " | ", matcher_2.group(1)])
      f.write(result + "\n")
    else:
      print("Error parsing node " + str(x))
  
  f.close()