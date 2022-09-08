def day_parse(className, day):

    # remove headers and 0. class
    if day[0].get('class') == ['KuvHeaderNadpis']:
        day.pop(0)
        day.pop(0)
        day.pop(0)
    day.pop(0)


    # delete copies in table 
    classes = []
    for d in range(len(day)):
        clsThis = day[d].get('class')
        clsNext = day[d+1].get('class') if d+1 < len(day) else None

        # class
        if clsThis == ['DctInnerTableType10DataTD'] and clsNext == ['DctCell'] or clsThis == ['DctInnerTableType10DataTD'] and clsNext == ['DctCellBottom', 'DctCell']:
            classes.append(day[d])

        # free time
        elif clsThis == ['DctCell'] and clsNext == ['DctCell'] or clsThis == ['DctCellBottom', 'DctCell'] and clsNext == ['DctCellBottom', 'DctCell']:
            classes.append(day[d])


    # ODV exception
    if classes[0].text.startswith("Odv"):
        odv = classes[0]
        odvNone = classes[1]
        classes.clear()

        for index in range(13):
            if index != 4 and index < 7:
                classes.append(odv)
            else:
                classes.append(odvNone)


    # parse to json
    parsed = []
    index = 0
    for d in classes:
        if d.text != None and d.text != "":
            # class
            spl = d.text.split(".")
            spl2 = spl[0].split(className)
           
            template = {
                "pauza": False,
                "hodina": index,
                "ucitel" : spl2[1],
                "predmet" : spl2[0],
                "ucebna" : spl[1],
            }
            parsed.append(template)
        
        else:
            # pauza
            template = {
                "pauza": True,
                "hodina": index,
            }
            parsed.append(template)

        index += 1

    return parsed



def days_to_json(className, dayTop, dayBottom=None):
    # parse days top and bottom if exists
    dt = day_parse(className, dayTop)
    
    if dayBottom != None:
        db = day_parse(className, dayBottom)
    else: 
        db = None


    # combine top and bottom of day
    day = {
        "top": dt,
        "bottom": db
    }

    return day

    

    
   

    

