#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int isPrime(int i){
  int j;
  for (j = 1; j<=i; j++){
    if( (i % j == 0) && (i != j) )
      if ( j != 1)
        return 0;
  }
  return i;
}

int main(){
	int contador = 1;

  #pragma omp parallel num_threads(4) shared(contador)
	{
    int id = omp_get_thread_num();
    int tmp;
    int C;
    #pragma omp for //Hace que el for sea compartido entre todos los hilos
    for(C=200000; C>=1; C--){
      #pragma omp critcal
      {
        tmp = contador;
        contador++;
  		}

      int retorno = isPrime(tmp);
      if(retorno != 0)
        printf("El numero %d es primo y fue calculado con %d\n", retorno,id);
  	}
  }


	printf("\n\nFIN DE LA EJECUCION\n\n");
	return 0;

}

/*    while(contador <= 10){
      #pragma omp critcal
      {
        tmp = contador;
        contador++;
  		}

      int retorno = isPrime(tmp);
      if(retorno != 0)
        printf("El numero %d es primo y fue calculado con %d\n", retorno,id);
  	}
  }
*/

//gcc -fopenmp *.c -o nombre
//./nombre
