# ITASEC23 - CTF Workshop Udine

# Spider - Writeup

Riuscirai a trovare i miei segreti?

La flag è divisa in due parti, dovrai trovarle entrambe e concatenarle per ottenere la flag.

Site: [http://spider.challs.cyberhighschools.it](http://spider.challs.cyberhighschools.it)

---
### Solution

The site consists of a static page with no apparent vulnerabilities, but it contains the following hint:

> Think like a [spider](https://en.wikipedia.org/wiki/Web_crawler)

This suggests that the two parts of the flag are located in paths that a web crawler (spider) would typically discover.

Specifically:

- The [robots.txt](https://en.wikipedia.org/wiki/Robots_exclusion_standard) file reveals the existence of `supe3s3cretf0lder/flag1.txt`, which contains the first part.  
- The [sitemap.xml](https://en.wikipedia.org/wiki/Sitemaps) file points to the second part at `standardNonSecretFolder/flag2.txt`.
---
Concatenating both parts of the flag gives:  
```
flag{s3mbr1_un0_sp1d3R}
```
