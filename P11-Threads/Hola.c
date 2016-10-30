#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main(){
	int i = 100;
	#pragma omp parallel num_threads(5) shared(i)
	//shared:es para compartir variables
	{
		#pragma omp critcal //Bloque atomico
		{
			int id = omp_get_thread_num();
			i = id;
			printf("La var fue modificada por: %d\n", id);
		}
		/*
		printf("hola mundo :)\n");
		for(i=0; i<10; i++){
			printf("Al Thread %d, numero %d\n",id,i);
		}
		*/
	}
	printf("\n\nFIN DE LA EJECUCION\n\n");
	printf("Valor final de la variable i: %d\n\n",i);
	return 0;

}


//gcc -fopenmp *.c -o nombre
//./nombre
