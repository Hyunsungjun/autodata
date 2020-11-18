for i in fire:
    for j in year:
        for n in min:
            sleep(1)
            selectFilter()
            textClear()
            writeContext()
            sleep(5) # 불러오는시간

            makeShape()
            sleep(2)
            exportFile(len(n))
