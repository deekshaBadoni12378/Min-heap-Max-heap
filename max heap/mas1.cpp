#include <iostream>
#include <conio.h>
using namespace std;
void heapify(int *x, int l, int m)
{
    int k, temp;
    temp = x[l];
    k = 2 * l;
    while (k <= m)
    {
        if (k < m && x[l+1] > x[k])
            k = k + 1;
        if (temp > x[k])
            break;
        else if (temp <= x[k])
        {
            x[k / 2] = x[k];
            k = 2 * k;
        }
    }
    x[k/2] = temp;
    return;
}
void maxheap(int *x,int m)
{
    int l;
    for(l = m/2; l >= 1; l--)
    {
        heapify(x,l,m);
    }
}
int main()
{
    int m, l, y;
    cout<<"enter number of elements \n";
    cin>>m;
    int x[50];
    for (l = 1; l <= m; l++)
    {
        cout<<"enter element"<<endl;
        cin>>x[l];
    }
    maxheap(x,m);
    cout<<"max heap array\n";
    for (l = 1; l <= m; l++)
    {
        cout<<x[l]<<endl;
    }
    getch();
}
