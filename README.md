Тестуються наступні алгоритми
* Боєра-Мура
* Кнута-Морріса-Пратта
* Рабіна-Карпа

Для тестування алгоритмів пошуку було довільно вибрано декілька підрядків.
Свідомо останій підрядок був сформований таким чином щоб як найменьше або взагалі не зустрічався в тексті в обох файлах.

Результати виконання алгоритмів з різними підрядками наступні:

```
**** Search in file: article.txt ****

==== Search string: оптимізаційних ====
Боєра-Мура 0.00042742298683151603
Кнута-Морріса-Пратта 0.0016571159940212965
Рабіна-Карпа 0.004971594025846571

==== Search string: інтервал ====
Боєра-Мура 0.0005329240229912102
Кнута-Морріса-Пратта 0.0010819419985637069
Рабіна-Карпа 0.002406385960057378

==== Search string: полягає ====
Боєра-Мура 0.0009599870536476374
Кнута-Морріса-Пратта 0.0017896440112963319
Рабіна-Карпа 0.004475530004128814

==== Search string: обходу ====
Боєра-Мура 0.0012895020190626383
Кнута-Морріса-Пратта 0.0023758659954182804
Рабіна-Карпа 0.005283554026391357

==== Search string: алго ====
Боєра-Мура 3.3322954550385475e-05
Кнута-Морріса-Пратта 3.988598473370075e-05
Рабіна-Карпа 0.000123421021271497

**** Search in file: article.txt ****

==== Search string: оптимізаційних ====
Боєра-Мура 0.0003956860164180398
Кнута-Морріса-Пратта 0.0016005460056476295
Рабіна-Карпа 0.003910330997314304

==== Search string: інтервал ====
Боєра-Мура 0.00040802499279379845
Кнута-Морріса-Пратта 0.000902339001186192
Рабіна-Карпа 0.002143335994333029

==== Search string: полягає ====
Боєра-Мура 0.0008148850174620748
Кнута-Морріса-Пратта 0.0016888039535842836
Рабіна-Карпа 0.004076940007507801

==== Search string: обходу ====
Боєра-Мура 0.0012319189845584333
Кнута-Морріса-Пратта 0.00244522700086236
Рабіна-Карпа 0.005301825993228704

==== Search string: алго ====
Боєра-Мура 3.3050018828362226e-05
Кнута-Морріса-Пратта 3.8788013625890017e-05
Рабіна-Карпа 0.00011593394447118044
```

Висновки.  
Найєфективнішим алгоритмом є Рабіна-Карпа. Цей алгоритм практично не залежить від кількості текста що треба перебрати для знаходження підрядка.  
Алгоритми Боєра-Мура та Кнута-Морріса-Пратта єфективні при умові якщо точно підрядок знаходиться в тексі. Інакше час виконання стає дуже великим. 
