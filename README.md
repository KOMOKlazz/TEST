# Задача

## Описание программы решения

1. Ввод строк в массив

       string[] array = new string[5] {"Привет", "Lets go", "123", "hi", "noo" };
       string[] finalArray = new string[array.Length];

2. Вызов двух методов

       LocateArray(array, finalArray);
       Print(finalArray);

3. Первый метод

       void LocateArray(string[] array, string[] finalArray)
       {
           for (int i = 0; i < array.Length; i++)
           {
               if (array[i].Length <= 3)
               {
                   finalArray[rightarraycount] = array[i];
                   rightarraycount++;
               }
           }
       }

3. Второй метод

       void Print(string[] array)
       {
           for (int g = 0; g < array.Length; g++)
           {
               Console.Write(finalArray[g] + " ");
           }

           Console.WriteLine();
       }



