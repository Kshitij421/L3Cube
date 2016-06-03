#include <stdio.h>
#include <stdlib.h>	

#define SIZE 365

void int_to_date_converter(int c);
int findups(int birthday[],int people);
double mathematicalprobability(int people);
void quicksort(int birthday[],int first,int last);


int main(int argc,char **argv)
{
	int people,trials,duplicate,totalduplicate;
	people=trials=duplicate=totalduplicate=0;

	printf("How many people need to add \n");
	scanf("%d",&people);

	int birthday[people];

	printf("How many trials need to take\n" );
	scanf("%d",&trials);

	//#pragma omp parallel for shared (dups) shared (totaldups)
	for(int i=0;i<trials;i++)
	{
		
		for(int j=0;j<people;j++)
		{
			int c=rand()%SIZE+1;
			birthday[j]=c;
		}

		duplicate=findups(birthday,people);

		if(duplicate)
			totalduplicate++;


	}

	printf("Total:%d\n",totalduplicate);

	double probability=mathematicalprobability(people);
	double probability1=(double)totalduplicate/trials;
	printf("Probability By Mathematical formula on %d Person  is %lf\n",people,probability);
	printf("Probability By Random Experiments on %d Person  is %lf\n",people,probability1);


}


int findups(int birthday[],int people)
{
	int count=0;
	quicksort(birthday,0,people);

	for (int i = 1; i < people; ++i)
	{
		if(birthday[i]==birthday[i-1])
			count++;
	}
	return count;
}


 void quicksort(int x[],int first,int last)
 {
    int pivot,j,temp,i;

     if(first<last)
     {
         pivot=first;
         i=first;
         j=last;

         while(i<j){
             while(x[i]<=x[pivot]&&i<last)
                 i++;
             while(x[j]>x[pivot])
                 j--;
             if(i<j){
                 temp=x[i];
                  x[i]=x[j];
                  x[j]=temp;
             }
         }

         temp=x[pivot];
         x[pivot]=x[j];
         x[j]=temp;
         quicksort(x,first,j-1);
         quicksort(x,j+1,last);


    }
}


double mathematicalprobability(int people)
{
	double prob = 1.0;
    int i;
    for(i=1; i<=people; i++)
    {
        prob = prob * ((double) ( 365 - i + 1) / 365);
    }
    prob = 1.0 - prob;
    return prob;
}
