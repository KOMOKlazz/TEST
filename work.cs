string[] array = new string[5] { "Привет", "Lets go", "123", "hi", "noo" };
string[] finalArray = new string[array.Length];
int rightarraycount = 0;
LocateArray(array, finalArray);
Print(finalArray);

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

void Print(string[] array)
{
    for (int g = 0; g < array.Length; g++)
    {
        Console.Write(finalArray[g] + " ");
    }

    Console.WriteLine();
}

