count = 0
s = "ВЕРОНИКА"
for x1 in s:
    for x2 in s:
        for x3 in s:
            for x4 in s:
                for x5 in s:
                    for x6 in s:
                        a = x1 + x2 + x3 + x4 + x5 + x6
                        gl = a.count("Е") + a.count("О") + a.count("И") + a.count("А")
                        sogl = a.count("В") + a.count("Р") + a.count("Н") + a.count("К")
                        if gl > sogl:
                            count += 1
print(count)
