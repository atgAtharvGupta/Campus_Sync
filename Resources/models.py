from django.db import models
# Create your models here.

DEFAULT_PROFILE = "/9j/4AAQSkZJRgABAQEASABIAAD/4QAiRXhpZgAATU0AKgAAAAgAAQESAAMAAAABAAEAAAAAAAD/2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEBAMFBwYHBwcGBwcICQsJCAgKCAcHCg0KCgsMDAwMBwkODw0MDgsMDAz/2wBDAQICAgMDAwYDAwYMCAcIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAz/wAARCAD6APoDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDDooor+xj+BwooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACijNGcUAFFGaM5oAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKbJIsSMzMqqoySTgAUAOJwK93/AGYP+Cc/xI/aksoNVsbKDw74XuAHj1jVg0aXScfNbxAeZMMEENhYm5AkyMV9J/8ABN3/AIJc2eoaRY/EH4oaetzJdKtxo3hy6izFDGeVuLtD96RhgrAw2opy4Zzsh/QxE2d81+T8UeI6w85YXKrSktHN6pPtFdbd3p2T3P23gzwoeLpRxucNxhLWMFpJrvJ9E+y97u09D4x+Fv8AwRF+Gvhi1ik8Va14k8XXm0CVBMNNsnPqqQ/vlz7zt07V6XZf8ErfgNY24iXwDAyqMZk1W/kb/vppyf1r6For8uxHE+b1pc1TEz+Uml9yaX4H7LheDciw8eSnhKfzipP75Xb+bPlPxx/wRq+Cfim0ZNNsfEXhWZsnztN1iaZif927M6Y9go4r5T/aE/4I2+PvhnbXGpeCdQtPHumwgu1osYstTjXk/LGzGObCjna6uxICxkmv1Yor0Mt44znByTVZzXVT95P5v3l8mjy828N8gx8GvYKnLvT91r5L3X80z+eu+srjStRuLO8t7izvLOVoLi3uImimt5FOGR0YBkdTwVYAgjBGajr9if27f+CfPhv9rTw4+oWcdronj61jxZawE2rdgDAt7vbzJEezYLxHlcrvjk/Irxx4I1j4ZeMtS8O+INPuNK1rR5zbXlpMPmhcAHqMhlZSrK6kq6srKSrAn9w4X4rw2c0m4LlqR+KLf4p9V59Ho+l/5z4w4LxmQV0qnv0pfDNK1/JrpLyu01qm7O2XRRRX1J8aFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABX09/wSv/ZMg/aQ+Osms65apceFfA4jvLiGVN0eoXjFvs8DDoyAo0rjkfu40YFZTXzDX7Ff8Ep/hRD8K/2K/C8gjRbzxYreJLt1/wCW32nBgb8LVbZf+A9q+J4+zmeAyqSpO06j5E+qTV2/uVvJtM/QvDPIIZpnUfbq9Okudro2mlFfe7+aTR9HUUUV/N5/WwUUUUAFFFFABXw7/wAFlP2TYfGvw0T4o6TCo1zwnEItWCLg3mm7h85HOWgdi+TgCN5s52oB9xVn+LPCth448Naho+q2sN9perWstleW0y7o7mCRSkkbD0ZSQfrXqZNmlXLsbTxlLeL1XddV81/nujxeIclo5tl9XAVtpLR9pLVP5P71psz+fcdKKp67ptz8KPin4k8B6vcPdX/hXV7vRVvJBtN4bed4Qx6cvsDKf4gw743XM1/VmHxEK9NVab0dn95/FOKwtTD1XRqqzTsFFFFbHOFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUARX0vk2Uz/3UY/pX76/BfRI/DHwm8MabDtEOn6RZ20YUcBUhRRj8BX4GzR+dCyf3lIr92P2UvGSfEP9mzwFrisrHVPDthcSYbJWQ26b1Pur7gfcGvyPxYjJ0MNJbJy/FRt+TP3HwRlH61iovflhb0Tlf80ehUUUV+Kn9DhRRRQAUUUUAFFFFAH4Gf8ABWDR4dD/AOCjPxWt4F2xtf2VyQP78+mWc7/m8rH8a8y8EeNf7R22d43+kDiOUn/W+x/2vfv9evaf8FIPHMfxG/b3+LWqRncq+IZdNyB3skjsT+ttXihH1/wr+l8hqTpYGhffkjf/AMBR/IvElGniMwxDjs6k2v8AwJ2PX80VzPgnxp/am20um/0oDEch/wCWw9D/ALX866avrKdSM1zRPhatKVOXLIKKKKszCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooADX6hf8EV/j9D4w+AWpeBbqbOq+CbxpLdGPzS2Ny7yowJ5OyYzoQOFXyhn5gB+Xtd7+zJ+0Nq/7LXxq0nxlo6NcfY91vf2W/YupWchHmwE9idqupOQskcbEEKQfmeLsjea5bPDw+Ne9H/EunzTa+dz67gfiJZLm0MVU/hv3Z/4XbX5NJ+drH7t0Vznwl+K2h/G74d6V4q8N3seoaLrMAntpl64yVZGXqsiMGRkPKsrKcEGujr+YZxlCThNWadmnumt0f2NSqwqwVSm7xkk01s09U15MKKKKk0CiiigArzf9rb4/wBn+y7+zz4q8d3vkuvh7T3mtoJMhby6YrHbQZHTzJ3iTPbfngAmvSGbaK/Fz/gsb+3/AGv7UXxItvAvg/UI77wD4NuWmkvLcgw63qW1kaVGH34IVZ0jYfK7PK43p5T17vDuTzzLGRo29xayfZf5vZffsmfM8WZ9DKsBKtf35aQXd9/Rbv7t2j4wur251O6mury4mvLy6kaa4uJDl55GJZ3b3ZiSfc1H/wB9Uf8AfVH/AH1X9D7aI/l/fUASjbl3KV5BHBBru/BnjNdXVbW5YLeKPlY8Ccf/ABQ7jv1HfHCf99UI7RuGUsrKchgcFT2INbUa0qcro5sTho1o8r36M9ezmiuf8GeMhrcYt7hlW8UdcYE4Hcf7Q7j8RxkDoAc17NOpGcVKJ81VpSpy5JbhRRRVmYUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFB5oooA9c/ZF/bX8YfsZ+KZ7rQkh1jQdSkEmq6BdTGOC9YAKJopMHyLkKAvmBSrqqrIrBY2i/Vz9lf9un4c/tiaI0/g/WVOqW8e++0K+xb6tpuMBvNgycqGIXzIy8RbIDkivxHrF8Q+HppdRttW0yeax1rT3E1tdQSmGVHX7rLIpDJIP4XBBHTOOR8LxRwPhc0bxFL3KvVpaS9V1fnv67H6Twb4jY3JksJV/eUeibs4/4X0XlZrta5/RlRX4RfCT/AIK9fH/4NRR2h8YR+KbO1AjW18T2K37DGch5x5d0x9d8xIx2r1W2/wCDg34uizVbnwf8NprgDmSO1vY0z67Tcsfw3V+U1uAc0hK0OWS8nb80j9rw/ibk9SN580X2av8Ak2fsRXNfFf4w+Gfgb4Qn8QeLtc0vw7otvxJeX9wsMe7GQi55eRsEKi5ZjwoJ4r8bviB/wXO/aA8b2Rgsb7wf4S5O2bRtD3zYJ7m8kuFJ7ZCCvl/4mfFjxT8afEg1jxh4i1zxRqihljudTvJLloFY5KR7iRGmediBV9q7MD4d4ycr4qaivLV/ovnd+hwZl4pYOEXHA05Tl3l7sf1b9LL1Ps3/AIKRf8Fj779o7S9Q8C/DNb7Q/BNzvt9R1eVTDqGvxH5TFGvDW9s45YNiWVSFYRL5kcnwkBtHAI+lAGP71H/fVfqGV5Thsvo+ww0bLq+rfdvv/SPyDNs4xWZYh4nFyu+i6Jdkui/Pd3Yf99Uf99Uf99Uf99V6R5Yf99Uf99Uf99Uf99UALHI0Lq0bMjqQysOCpHQg+1d/4M8Xrr0PkTbVvYxk44Ew/vD39R+I44Hn/wD31TopWt5VkjZ0dDuVgcFT6itqNaVKV1t1RzYrDRrRs9+jPXKKw/B/i5fEEHly7UvYx8ygYEg/vD+o7fStwHIr2qc1Nc0T5mpTlCXLLcKKKKogKKKKACiiigAooooAKKKKACiiigAoooJxQAUZrpvhF8FvFnx78U/2N4O0G/17UECmZbdQsVqpzhppWIjiU4OC7DJGBk8V90/s8f8ABEG1Ty734neJprmZQrHSNBby4QeflkuXG9wR1EaRkEcOwrwc44my7K9MXUtL+VayfyW3k3ZeZ9LkPCOa5w/9ipNx6yekV83v6K78j87JrmODbvdV3kKuTjcTwAPc+lekeA/2QPit8T1jbRPh34uuoZQDHcT6e9nbyA91mn8uMj3DYr9kPg7+yl8PfgDCg8I+EdD0WZI/K+2RW+++kXnh7ly0z9T95z1PrXolfm+O8V53tgqC9Zu/4Rtb/wACP1nLfBONlLMMS79oL/26V/8A0lH4u3n/AARb+OXjuNbr/hH9D0G94DDUNagIcf7X2cy8j1GeOPTbIv8AwQF+O4h3Sav8K4WI4R9cvt36WJH61+z1FfMVvELNak+b3F6R/wA2z7LDeFuTUYcl5y9ZL9Io/EbX/wDghr+0DokbNDp/g3WCv8NhrwBP/f8AjiH615d49/4Js/H34aQ+Zq3wn8XSJ66XFFrGR64snmI/EDHfFf0FUVdHxCzKP8SMJfJp/g7fgTiPC3K5r91OcX6pr8Y3/E/mN1Oyn0PVptPvobix1C2OJrW4jMU8J/2kYBl/EVHn/er+kv4p/A/wj8cdEXTfGXhnQPFFiuSkGq6fFdpExx8yeYDsbgfMuCCAc5Ar4u/aQ/4IFfDnxtbXF98O9Z1TwHqrfOtnKzanpTnqfklfz4yxPVZiqDOIzwK+my/xDwlV8uKg6fn8S/BJ/gz5HNPC/H0U54OaqLs/df4tr72j8hf++qP++q9e/al/YR+KH7HN3u8beH2j0d5BFBrunSG70m4Y4AUTbQY2YnCpMsbtg4UgZryHOP71fdYXFUcRTVWhJSi+q1R+c4rCVsNVdHEQcZLo1Z/12fUP++qP++qP++qP++q6DnD/AL6o/wC+qP8Avqj/AL6oAdBO9pOssTNHJGdysOqmvQvCXiyPxFAVbbHeRjMiDo4/vL7e3b8jXnf/AH1T7a5ksriOaF3jljO5HHVTW1Cu6cr9DlxWFjWj59D1sHIorH8KeKY/EVtg7Y7qMfvIx0I/vL7dPcd+oJ2Ac17UJRlHmjsfNVKcoS5ZbhRRRVEBRRRQAUUUUAFFFFABRRSMwRSx4CjJJ7UADuI0ZmIVVGSSegr6+/Yc/wCCVmsfHqCy8VePmvPDng2YCa1soz5epawnUPyD5EDdmI8x1yVCKySn0f8A4Jk/8Ez4dWsdP+JXxGsUl8wLdaBoVzHuRVPKXlyh6sfvRxHhRh2yxUR/opX4/wAYeIEqcpYHKparSU/zUf8A5L7u5+6cA+GEa8I5lnEfdesaffs5+XaPXrpo+d+Fnwm8O/BTwdbeH/Cuj2Gh6PagbLa0i2KWwAXY8l5GwCzsSzHkknmuioor8bnUlOTnNtt6tvVs/oCnShTgqdNJRWiS0SXZIKKKKk0CiiigAooooAKKKKAKeuaHa+JNLuLG+ggvLG8ieC5tp4xJDcRsMMjqeGUrkFTwQSDkV+bn7fn/AAQ1s9RiufFXwRjjsNQYvNdeE5Zljs7jv/oUjnEDZJxC58o5ARoQoV/0vor0srzbFZfV9rhpW7ro/Jrr+a6NHj5xkeDzSj7HFwv2fVeafT8n1TP5kNV0q60DVbrT9QtbzT9QsZntrq0uoWhuLWVCVeOSNgGR1YEMrAFSCCARUH/fVftd/wAFQP8Aglvpf7Xvh6fxZ4TitdK+KGnQfu5TiOHxDGigLb3B6CQABY5jyuArEpjb+LWtaLe+GdavNN1Kzu9P1LTp5LW7tLmMxz2syMVeN1PKsrAgg9CK/cuH+IaGaUeaHuzXxR7ea7p9/kz+duJeGcTk+I9nU96Evhl0fk+zXVfNFb/vqj/vqj/vqj/vqvoD5oP++qP++qP++qP++qAJLS8l0+5jmhdo5IzlWHb/AD0x3Br0Twr4oi8R2mfljuox+9j/APZl/wBn9R0PYnzf/vqpbG+m0y7jnt3aOWM5Vh/np7V0Yeu6UvLqceKwqrR8+h6zRWX4Y8Sw+I7PcuI54x+9iz933H+yf/rVqV7EZKSUo7Hzc4ShJxlugoooqiQooooAKKKKACvrL/gld+xNF+0T8QJvGXiayW48F+FLgJHbTDMer34AdY2X+KGIFXcHh2aNDuXzVr5h8DeCNU+JvjbSPDmiwifVtevIrC0Rs7PMkYKC5AJCLnczY+VVY9BX7q/AX4NaX+z58IdB8G6Mp/s/QbUW6uy7WuJCS0szAcb5JGeRsfxOa/O/EPiKWAwawmHdqlW+vWMer9Xsvm90j9S8LeE45pj3jMSr0qNnZ7Sl0Xmlu/knozrwMCiiiv59P6mCiiigAooooAKKKKACiiigAooooAKKKKACvzn/AOC4X/BP2Pxn4PuvjV4UtUXXfD1sP+Eot4o8NqVhGoUXhxwZbZR8xOC0CnLfuI1P6MVHdWsd7A0UqLJHICrowyrg9QR3B9K9DK8yq4DExxNHdbruuqfr/wAE8nO8noZng5YSvs9n1T6Nen4rTqfzG/8AfVH/AH1XuP8AwUW/ZRH7HP7VWueF7ONo/DWoKus+HjnO2xnZwsOck/uZElhG4lmWJHP368O/76r+jMHiqeJoQxFL4ZJNfM/lnGYOrha88NWVpRbT+X6dvIP++qP++qP++qP++q6DlD/vqj/vqj/vqj/vqgCbT9Qm0m7S4t2ZJY+hxwR3BHcH0rsIvilbGNd9pch8DcFI2g+1cT/31R/31W1OtOnpFnPWwtKq7zR69RRRXuHyoUUUUAFBOBRQelAH2T/wRV+DKeNv2gtb8Y3UIkt/BenCG1ZlI23d2HQOp9VgjuFI/wCm6mv1Pr5D/wCCKngePw1+yDNq3ytN4q1y7vt3G4RxFbML67Q9tIQD3ZvWvryv5n45x7xWdVnfSD5F5cuj/wDJrv5n9feG+WLBcP0F1qLnfnzar/yXlXyCiiivkT7oKKKKACiiigAooooAKKKKACiiigAooooAKKKKAPgX/g4B+AUXjL9mjQfiBbw51HwHqiwXMu7H+gXrJA4x/ERcizI/ugyHuTX5Bjp/FX9E37avw2/4XB+yX8SPDKxJLcav4bv4rXcN2y5EDNA+O+2VY2x6qK/nXgmW4hWRd211DD6Gv2Tw8xjqYGeHf/LuWnpLX87n4H4oYBUsyhiY/wDLyOvrHT8uUd/31R/31R/31R/31X6Afmof99Uf99Uf99Uf99UAH/fVH/fVH/fVH/fVAHr1FFFfRHxoUUUUAFB6UUHkUAfs5/wTC0tdI/YW+H0Uf3ZLOe4PHeW7nkP6sa98r8CT+0R8VPCvhW107wx8SPG2h2emoUt7Gy1qe3tgmSxVUVgqnJJGMDJweMFeVf8Abs+N8bFW+LnxIVlJDA6/cgqR2Pz1+HZt4d42pjKlf2kbTlKS+Lq2+25/RmReKeApYCjhVRk3ThGL1X2UlffZ20P6IKK/nf8A+G7vjd/0Vz4kf+FBc/8AxdH/AA3d8bv+iufEj/woLn/4uvO/4hzjf+fsPx/yPX/4itgv+fE/vj/mf0QUV/O//wAN3fG7/ornxI/8KC5/+Lo/4bu+N3/RXPiR/wCFBc//ABdH/EOcb/z9h+P+Qf8AEVsF/wA+J/fH/M/ogor+d/8A4bu+N3/RXPiR/wCFBc//ABdH/Dd3xu/6K58SP/Cguf8A4uj/AIhzjf8An7D8f8g/4itgv+fE/vj/AJn9EFFfzv8A/Dd3xu/6K58SP/Cguf8A4uj/AIbu+N3/AEVz4kf+FBc//F0f8Q5xv/P2H4/5B/xFbBf8+J/fH/M/ogor+d//AIbu+N3/AEVz4kf+FBc//F0f8N3fG7/ornxI/wDCguf/AIuj/iHON/5+w/H/ACD/AIitgv8AnxP74/5n9EFFfzv/APDd3xu/6K58SP8AwoLn/wCLo/4bu+N3/RXPiR/4UFz/APF0f8Q5xv8Az9h+P+Qf8RWwX/Pif3x/zP6IKK/nf/4bu+N3/RXPiR/4UFz/APF0f8N3fG7/AKK58SP/AAoLn/4uj/iHON/5+w/H/IP+IrYL/nxP74/5n9EFFfzv/wDDd3xu/wCiufEj/wAKC5/+Lo/4bu+N3/RXPiR/4UFz/wDF0f8AEOcb/wA/Yfj/AJB/xFbBf8+J/fH/ADP6HpI1lXayhlPBB6EV/MLYWn9n2MNvuZvs8Yi3eu0Y/pXrg/bv+NwP/JXPiR/4P7n/AOKryn/vqvruFOG6+VOr7aSlz8u1+l97pdz4bjPiujnXsfYwceTmve2vNy9vQP8Avqj/AL6o/wC+qP8Avqvsj4cP++qP++qP++qP++qAD/vqj/vqj/vqj/vqgD16iiivoj40KKKKACiiigArnPGngxdXVrq1VVvFHzKOBOB/7N79xgeldHQeaipTjOPLI0pVZU5c8TyHlThtykcEdxR/31XceNvBf9qBru1X/SgMyIP+W30/2v5/WuGBx6141ajKm7M+mw2JjWjdC/8AfVH/AH1R/wB9Uf8AfVYnQH/fVH/fVH/fVH/fVAB/31R/31R/31R/31QAf99Uf99Uf99Uf99UAH/fVH/fVH/fVH/fVAB/31R/31R/31R/31QAf99Uf99Uf99Uf99UAH/fVH/fVH/fVH/fVAB/31R/31R/31R/31QAf99Uf99Uf99Uf99UAH/fVH/fVH/fVH/fVAHr1FFFfRHxoUUUUAFFFFABRRRQAHmuW8b+Cf7QLXlmn+kdZYx/y1/2h/teo/i+v3upoIzWdSnGceWRpRrSpy5onkAb/Ipf++q7Pxz4L+1772zj/fctNEv/AC09WX/a9R369c54wHI43H6V41ak6cuVn02GxEaseaIf99Uf99Uf99Uf99VkdAf99Uf99Uf99Uf99UAH/fVH/fVH/fVH/fVAB/31R/31R/31R/31QAf99Uf99Uf99Uf99UAH/fVH/fVH/fVH/fVAB/31R/31R/31R/31QAf99Uf99Uf99Uf99UAH/fVH/fVH/fVH/fVAB/31R/31R/31R/31QB69RRRX0R8aFFFFABRRRQAUUUUAFFFFABXI+OPBW8yX1mvzfemiUfe9WX39R369c566gnArOpSjUjyyNqFeVKXNE8hByP4qP++qv+LI1g8S3yoqoomOAowB0rO3V4UlZ2Pq4u6THf8AfVH/AH1Td1G6kMd/31R/31Td1G6gB3/fVH/fVN3UbqAHf99Uf99U3dRuoAd/31R/31Td1G6gB3/fVH/fVN3UbqAHf99Uf99U3dRuoAd/31R/31Td1G6gB3/fVH/fVN3UbqAP/9k"

DEFAULT_MidTerm1Total = 20
DEFAULT_MidTerm2Total = 20
DEFAULT_Viva1Total = 10
DEFAULT_Viva2Total = 10
DEFAULT_Quiz1Total = 10
DEFAULT_Quiz2Total = 10



class RightsSupport(models.Model):

    class Meta:

        managed = False  # No database table creation or deletion  \
        # operations will be performed for this model.

        default_permissions = ()  # disable "add", "change", "delete"
        # and "view" default permissions

        permissions = (
            ('department_course_rights', 'Manage Department and Courses'),
            ('faculty_rights', 'Manage Faculties'),
            ('student_rights', 'Manage Students'),
            ('marks_rights', 'Manage Marks'),
            ('marks_view_rights', 'View Marks'),
            ('attendance_rights', 'Manage Attendance'),
            ('attendance_view_rights', 'View Attendance'),
            ('email_rights', 'Send Emails'),
            ('sms_rights', 'Send SMS'),
            ('api_rights', 'Add Send Grid and Twilio API Key'),
            ('permission_rights', 'Grant Permissions'),
        )


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=128, unique=True)

    def __str__(self):

        return self.Name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=128)
    Department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):

        return self.Name


class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=128)
    Course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):

        return self.Name


class Semester(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=128)
    Branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):

        return self.Name


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=256)
    Theory_Lectures = models.IntegerField()
    Lab_Lectures = models.IntegerField()
    Semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):

        return self.Name


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    First = models.CharField(max_length=150)
    Last = models.CharField(max_length=150)
    Email = models.EmailField(unique=True)
    Enrollment = models.CharField(max_length=64, unique=True)
    Contact = models.CharField(max_length=10)
    DOB = models.DateField()
    Category = models.CharField(max_length=7)
    Address = models.CharField(max_length=1024)
    Photo = models.TextField(default=DEFAULT_PROFILE)
    Department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    Course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    Branch_id = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)
    Semester_id = models.ForeignKey(Semester, on_delete=models.DO_NOTHING)
    Password = models.CharField(max_length=128, default="abc123")

    def __str__(self):

        return str(self.First) + " " + str(self.Last) + " - " + str(self.Enrollment)


class Attendence(models.Model):
    id = models.AutoField(primary_key=True)
    Theory_Lectures = models.BooleanField(default=False)
    Lab_Lectures = models.BooleanField(default=False)
    Student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Timestamp = models.DateTimeField()

    def __str__(self):

        return str(self.Student_id)


class SendGridAPIKey(models.Model):
    Key = models.CharField(max_length=512)

    def __str__(self):

        return self.Key


class TwilioAPIKey(models.Model):
    SID = models.CharField(max_length=512)
    Token = models.CharField(max_length=512)
    Notify = models.CharField(max_length=512)

    def __str__(self):

        return self.SID


class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    First = models.CharField(max_length=150)
    Last = models.CharField(max_length=150)
    Email = models.EmailField(unique=True)
    Post = models.CharField(max_length=256)
    Qualification = models.CharField(max_length=1024)
    FacultyCollegeID = models.CharField(max_length=64, unique=True)
    Contact = models.CharField(max_length=10)
    Address = models.CharField(max_length=1024)
    Photo = models.TextField(default=DEFAULT_PROFILE)
    DOB = models.DateField()
    JoiningDate = models.DateField()
    Verified = models.BooleanField(default=False)
    Password = models.CharField(max_length=128, default="mnb098")

    def __str__(self):

        return self.FacultyCollegeID


class Marks(models.Model):
    id = models.AutoField(primary_key=True)
    MidTerm1 = models.IntegerField()
    MidTerm1Total = models.IntegerField(default=DEFAULT_MidTerm1Total)
    MidTerm2 = models.IntegerField()
    MidTerm2Total = models.IntegerField(default=DEFAULT_MidTerm2Total)
    Viva1 = models.IntegerField()
    Viva1Total = models.IntegerField(default=DEFAULT_Viva1Total)
    Viva2 = models.IntegerField()
    Viva2Total = models.IntegerField(default=DEFAULT_Viva2Total)
    Quiz1 = models.IntegerField()
    Quiz1Total = models.IntegerField(default=DEFAULT_Quiz1Total)
    Quiz2 = models.IntegerField()
    Quiz2Total = models.IntegerField(default=DEFAULT_Quiz2Total)
    Student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    Timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return str(self.Student_id.First) + " " + str(self.Student_id.Last) + " - " + str(self.Subject_id.Name)


class FacultyAssigned(models.Model):
    Faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    Subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):

        return str(self.Faculty_id.First) + " " + str(self.Faculty_id.Last) + " - " + str(self.Subject_id.Name)