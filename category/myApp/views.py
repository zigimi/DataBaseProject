from django.shortcuts import render
from django.db import connection


def display2(request):
    if request.method == "POST":
        outputCategories1 = []
        outputCategories2 = []
        outputCategories3 = []
        outputCategories4 = []

        if request.POST.get("create")!=None:
            with connection.cursor() as cursor:
                drop1 = "DROP TABLE IF EXISTS product"
                cursor.execute(drop1)
                sqlQueryCategories1 = "CREATE TABLE IF NOT EXISTS `product`(" \
                                      "`maker` char(1) DEFAULT NULL, " \
                                      "`model` int NOT NULL, " \
                                      "`type` varchar(50) DEFAULT NULL, " \
                                      "PRIMARY KEY(`model`))"
                cursor.execute(sqlQueryCategories1)

                drop2 = "DROP TABLE IF EXISTS pc"
                cursor.execute(drop2)
                sqlQueryCategories2 = "CREATE TABLE IF NOT EXISTS `pc` (" \
                                      "`model` int NOT NULL, " \
                                      "`speed` double DEFAULT NULL, " \
                                      "`ram` int DEFAULT NULL, " \
                                      "`hd` int DEFAULT NULL, " \
                                      "`price` int DEFAULT NULL, " \
                                      "PRIMARY KEY (`model`))"
                cursor.execute(sqlQueryCategories2)

                drop3 = "DROP TABLE IF EXISTS laptop"
                cursor.execute(drop3)
                sqlQueryCategories3 = "CREATE TABLE IF NOT EXISTS `laptop` (" \
                                      "`model` int NOT NULL, " \
                                      "`speed` double DEFAULT NULL, " \
                                      "`ram` int DEFAULT NULL, " \
                                      "`hd` int DEFAULT NULL, " \
                                      "`screen` double DEFAULT NULL, " \
                                      "`price` int DEFAULT NULL, " \
                                      "PRIMARY KEY (`model`))"
                cursor.execute(sqlQueryCategories3)

                drop4 = "DROP TABLE IF EXISTS printer"
                cursor.execute(drop4)
                sqlQueryCategories4 = "CREATE TABLE IF NOT EXISTS `printer` ( " \
                                      "`model` int NOT NULL, " \
                                      "`color` tinyint(1) DEFAULT NULL, " \
                                      "`type` varchar(50) DEFAULT NULL, " \
                                      "`price` int DEFAULT NULL, " \
                                      "PRIMARY KEY (`model`))"
                cursor.execute(sqlQueryCategories4)

                connection.commit()
                connection.close()

                state = "Create 4 tables successfully"


        elif request.POST.get("insert")!=None:
            with connection.cursor() as cursor:
                sqlQueryCategories1 = "INSERT IGNORE INTO product (maker, model, type) VALUES (%s, %s, %s)"
                value1 = [('A', '1001', 'pc'), ('A', '1002', 'pc'), ('A', '1003', 'pc'), ('B', '1004', 'pc'),
                          ('B', '1005', 'pc'),
                          ('B', '1006', 'pc'), ('C', '1007', 'pc'), ('D', '1008', 'pc'), ('D', '1009', 'pc'),
                          ('D', '1010', 'pc'),
                          ('E', '1011', 'pc'), ('E', '1012', 'рс'), ('E', '1013', 'pc'), ('E', '2001', 'laptop'),
                          ('E', '2002', 'laptop'),
                          ('E', '2003', 'laptop'), ('A', '2004', 'laptop'), ('A', '2005', 'laptop'),
                          ('A', '2006', 'laptop'),
                          ('B', '2007', 'laptop'), ('F', '2008', 'laptop'), ('F', '2009', 'laptop'),
                          ('G', '2010', 'laptop'),
                          ('E', '3001', 'printer'), ('E', '3002', 'printer'), ('E', '3003', 'printer'),
                          ('D', '3004', 'printer'),
                          ('D', '3005', 'printer'), ('H', '3006', 'printer'), ('H', '3007', 'printer')]
                cursor.executemany(sqlQueryCategories1, value1)

                sqlQueryCategories2 = "INSERT IGNORE INTO pc (model, speed, ram, hd, price) VALUES (%s, %s, %s, %s, %s)"
                value2 = [(1001,2.66,1024,250,2114), (1002,2.1,512,250,995), (1003,1.42,512,80,478),
                          (1004,2.8,1024,250,649), (1005,3.2,512,250,630), (1006,3.2,1024,320,1049),
                          (1007,2.2,1024,200,510), (1008,2.2,2048,250,770), (1009,2.0,1024,250,650),
                          (1010,2.8,2048,300,770), (1011,1.86,2048,160,959), (1012,2.8,1024,160,649),
                          (1013,3.06,512,80,529)]
                cursor.executemany(sqlQueryCategories2, value2)

                sqlQueryCategories3 = "INSERT IGNORE INTO laptop (`model`, `speed`, `ram`, `hd`, `screen`, `price`) " \
                                      "VALUES (%s, %s, %s, %s, %s, %s)"
                value3 = [(2001,2.0,2048,240,20.1,3673), (2002,1.73,1024,80,17.0,949), (2003,1.8,512,60,15.4,549),
                          (2004,2.0,512,60,13.3,1150), (2005,2.16,1024,120,17.0,2500), (2006,2.0,2048,80,15.4,1700),
                          (2007,1.83,1024,120,13.3,1429), (2008,1.6,1024,100,15.4,900), (2009,1.6,512,80,14.1,680),
                          (2010,2.0,2048,160,15.4,2300)]
                cursor.executemany(sqlQueryCategories3, value3)

                sqlQueryCategories4 = "INSERT IGNORE INTO printer (`model`, `color`, `type`, `price`) " \
                                      "VALUES (%s, %s, %s, %s)"
                value4 = [(3001,1,'ink-jet',99), (3002,0,'laser',239), (3003,1,'laser',899), (3004,1,'ink-jet',120),
                          (3005,0,'laser',120), (3006,1,'ink-jet',100), (3007,1,'laser',200)]
                cursor.executemany(sqlQueryCategories4, value4)

                connection.commit()
                connection.close()

                state = "Insert all values successfully"


        else:
            outputOfQuery1 = []
            outputOfQuery2 = []
            outputOfQuery3 = []
            outputOfQuery4 = []

            with connection.cursor() as cursor:
                sqlQuery1 = "SELECT AVG(hd) FROM pc;"
                cursor.execute(sqlQuery1)
                fetchResultQuery1 = cursor.fetchall()

                sqlQuery2 = "SELECT maker, AVG(speed) FROM product, laptop WHERE product.model = laptop.model GROUP BY maker;"
                cursor.execute(sqlQuery2)
                fetchResultQuery2 = cursor.fetchall()

                sqlQuery3 = "SELECT maker, laptop.model, price FROM product, laptop WHERE product.model = laptop.model " \
                            "AND maker IN (SELECT maker FROM product, laptop WHERE product.model = laptop.model GROUP BY maker " \
                            "HAVING COUNT(maker) = 1);"
                cursor.execute(sqlQuery3)
                fetchResultQuery3 = cursor.fetchall()

                sqlQuery4 = "SELECT maker, printer.model, price FROM product, printer WHERE product.model = printer.model " \
                            "AND (maker, price) IN (SELECT DISTINCT maker, MAX(price) FROM product, printer " \
                            "WHERE product.model = printer.model GROUP BY maker);"
                cursor.execute(sqlQuery4)
                fetchResultQuery4 = cursor.fetchall()

                connection.commit()
                connection.close()

                for temp in fetchResultQuery1:
                    eachRow = {'AVGhd': temp[0]}
                    outputOfQuery1.append(eachRow)

                for temp in fetchResultQuery2:
                    eachRow = {'maker': temp[0], 'AVGspeed': temp[1]}
                    outputOfQuery2.append(eachRow)

                outputOfQuery2 = sorted(outputOfQuery2, key=lambda outputOfQuery2: (outputOfQuery2['maker']))

                for temp in fetchResultQuery3:
                    eachRow = {'maker': temp[0], 'model': temp[1], 'price': temp[2]}
                    outputOfQuery3.append(eachRow)

                for temp in fetchResultQuery4:
                    eachRow = {'maker': temp[0], 'model': temp[1], 'price': temp[2]}
                    outputOfQuery4.append(eachRow)

                outputOfQuery4 = sorted(outputOfQuery4, key=lambda outputOfQuery4: (outputOfQuery4['maker']))

                connection.commit()
                connection.close()

                state = "Queries are executed successfully"


        with connection.cursor() as cursor:
            sqlQueryCategories1 = "SELECT maker, model, type FROM product;"
            cursor.execute(sqlQueryCategories1)
            fetchResultCategories1 = cursor.fetchall()

            sqlQueryCategories2 = "SELECT * FROM pc;"
            cursor.execute(sqlQueryCategories2)
            fetchResultCategories2 = cursor.fetchall()

            sqlQueryCategories3 = "SELECT * FROM laptop;"
            cursor.execute(sqlQueryCategories3)
            fetchResultCategories3 = cursor.fetchall()

            sqlQueryCategories4 = "SELECT * FROM printer;"
            cursor.execute(sqlQueryCategories4)
            fetchResultCategories4 = cursor.fetchall()

            connection.commit()
            connection.close()

            for temp in fetchResultCategories1:
                eachRow = {'maker': temp[0], 'model': temp[1], 'type': temp[2]}
                outputCategories1.append(eachRow)

            for temp in fetchResultCategories2:
                eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'price': temp[4]}
                outputCategories2.append(eachRow)

            for temp in fetchResultCategories3:
                eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'screen': temp[4],
                           'price': temp[5]}
                outputCategories3.append(eachRow)

            for temp in fetchResultCategories4:
                eachRow = {'model': temp[0], 'color': temp[1], 'type': temp[2], 'price': temp[3]}
                outputCategories4.append(eachRow)

            connection.commit()
            connection.close()

        if request.POST.get("create")==None and request.POST.get("insert")==None:
            return render(request, 'myApp/index.html', {"products": outputCategories1, "pcs": outputCategories2,
                                                        "laptops": outputCategories3, "printers": outputCategories4,
                                                        "output1": outputOfQuery1, "output2": outputOfQuery2,
                                                        "output3": outputOfQuery3, "output4": outputOfQuery4,
                                                        "state": state})

        else:
            return render(request, 'myApp/index.html', {"products": outputCategories1, "pcs": outputCategories2,
                                                        "laptops": outputCategories3, "printers": outputCategories4,
                                                        "state": state})

    else:
        return render(request, 'myApp/index.html')

def display(request):
    outputCategories1 = []
    outputCategories2 = []
    outputCategories3 = []
    outputCategories4 = []
    outputOfQuery1 = []
    outputOfQuery2 = []
    outputOfQuery3 = []
    outputOfQuery4 = []
    with connection.cursor() as cursor:
        sqlQueryCategories1 = "SELECT maker, model, type FROM product;"
        cursor.execute(sqlQueryCategories1)
        fetchResultCategories1 = cursor.fetchall()

        sqlQueryCategories2 = "SELECT * FROM pc;"
        cursor.execute(sqlQueryCategories2)
        fetchResultCategories2 = cursor.fetchall()

        sqlQueryCategories3 = "SELECT * FROM laptop;"
        cursor.execute(sqlQueryCategories3)
        fetchResultCategories3 = cursor.fetchall()

        sqlQueryCategories4 = "SELECT * FROM printer;"
        cursor.execute(sqlQueryCategories4)
        fetchResultCategories4 = cursor.fetchall()

        sqlQuery1 = "SELECT AVG(hd) FROM pc;"
        cursor.execute(sqlQuery1)
        fetchResultQuery1 = cursor.fetchall()

        sqlQuery2 = "SELECT maker, AVG(speed) FROM product, laptop WHERE product.model = laptop.model GROUP BY maker;"
        cursor.execute(sqlQuery2)
        fetchResultQuery2 = cursor.fetchall()

        sqlQuery3 = "SELECT maker, laptop.model, price FROM product, laptop WHERE product.model = laptop.model " \
                    "AND maker IN (SELECT maker FROM product, laptop WHERE product.model = laptop.model GROUP BY maker " \
                    "HAVING COUNT(maker) = 1);"
        cursor.execute(sqlQuery3)
        fetchResultQuery3 = cursor.fetchall()

        sqlQuery4 = "SELECT maker, printer.model, price FROM product, printer WHERE product.model = printer.model " \
                    "AND (maker, price) IN (SELECT DISTINCT maker, MAX(price) FROM product, printer " \
                    "WHERE product.model = printer.model GROUP BY maker);"
        cursor.execute(sqlQuery4)
        fetchResultQuery4 = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultCategories1:
            eachRow = {'maker': temp[0], 'model': temp[1], 'type': temp[2]}
            outputCategories1.append(eachRow)

        for temp in fetchResultCategories2:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'price': temp[4]}
            outputCategories2.append(eachRow)

        for temp in fetchResultCategories3:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'screen': temp[4], 'price': temp[5]}
            outputCategories3.append(eachRow)

        for temp in fetchResultCategories4:
            eachRow = {'model': temp[0], 'color': temp[1], 'type': temp[2], 'price': temp[3]}
            outputCategories4.append(eachRow)

        for temp in fetchResultQuery1:
            eachRow = {'AVGhd': temp[0]}
            outputOfQuery1.append(eachRow)

        for temp in fetchResultQuery2:
            eachRow = {'maker': temp[0], 'AVGspeed': temp[1]}
            outputOfQuery2.append(eachRow)

        outputOfQuery2 = sorted(outputOfQuery2, key=lambda outputOfQuery2: (outputOfQuery2['maker']))

        for temp in fetchResultQuery3:
            eachRow = {'maker': temp[0], 'model': temp[1], 'price': temp[2]}
            outputOfQuery3.append(eachRow)

        for temp in fetchResultQuery4:
            eachRow = {'maker': temp[0], 'model': temp[1], 'price': temp[2]}
            outputOfQuery4.append(eachRow)

    return render(request, 'myApp/index.html',{"products": outputCategories1, "pcs": outputCategories2,
                                               "laptops": outputCategories3, "printers": outputCategories4,
                                               "output1": outputOfQuery1, "output2": outputOfQuery2,
                                               "output3": outputOfQuery3, "output4": outputOfQuery4})


