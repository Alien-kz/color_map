Скрипт для раскрашивания карты

# Установка
```
pip install matplotlib pandas cartopy
```

Структура
```
plot.py
stat.csv
color.csv
map/
```

# Данные

### Подписи
stat.csv
```
ADM1_EN,ADM2_EN,name,value,color
Abay Region,Abay District,Абайский район — город Абай,103.6,white
```

name - название для отображение

color - цвет для раскрашивания

value - значение для раскрашивания через color.csv (если нет color)

### Цвета
color.csv
```
min,max,color
60,80,coral
80,100,lightcoral
100,120,lightgreen
120,140,green
```
Все цвета здесь https://matplotlib.org/stable/gallery/color/named_colors.html

### Карта
```
map
-- kaz_admbnda_adm2_unhcr_2023.cpg
-- kaz_admbnda_adm2_unhcr_2023.dbf
-- kaz_admbnda_adm2_unhcr_2023.prj
-- kaz_admbnda_adm2_unhcr_2023.shp
-- kaz_admbnda_adm2_unhcr_2023.shp.xml
-- kaz_admbnda_adm2_unhcr_2023.shx
```

Например здесь
https://data.humdata.org/dataset/?q=kazakhstan&sort=last_modified%20desc&ext_page_size=25

# Отрисовка
```
python3 plot.py
```

Результаты
```
fig.png
districts_all.txt - все район
districts_not_found.txt - районы которые не нашли
```
