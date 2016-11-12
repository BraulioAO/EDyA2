#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

typedef struct nodo nodo;
struct nodo{
    nodo *next;
    int key;
};

nodo *head = NULL, *tail = NULL;

nodo* crear(int e){
  nodo *nuevo =  malloc(sizeof(nodo));
  nuevo->key = e;
  return nuevo;
}

void push(int e){
  nodo *nodo = crear(e);
  if(head == NULL){
      head = nodo;  //La cola esta vacia
      tail = nodo;
  }else{
    nodo->next = head;
    head = nodo;

  }

}

int pop(){
  if(head != NULL){
      nodo *tmp = head;
      head = head->next;
      if(head == NULL){
        tail = NULL;
      }
      return tmp->key;
}else{
  return -1;
}

}

void imprimir_cola(){
  nodo *aux = head;
  printf("Contenido de la cola { ");
  while (aux != NULL) {
    printf("%i , ",aux->key );
    aux = aux->next;
  }
  printf("}");
}


int main() {
/*
  push(10);
  push(20);
  push(33);
  printf("%d\n",pop() );
  printf("%d\n",pop() );
  printf("%d\n",pop() );
*/

  #pragma omp parallel num_threads(5)
  {
      int id = omp_get_thread_num();
      int i;
      for ( i = 0; i < id; i++) {
            #pragma omp critical
            {

                push(id);
            }

          }

      #pragma omp critical
      {
        imprimir_cola();
        printf("Eliminando: %d thread: %d\n",pop(),id );

      }


  }
  imprimir_cola();
  printf("\n%d\n",pop());
  printf("%d\n",pop());
  imprimir_cola();
  return 0;
}
