#include <stdio.h>   // Biblioteca padrão para entrada e saída (printf, scanf)
#include <stdlib.h>  // Biblioteca padrão utilitária (memória, conversão, aleatórios, etc.)
#include <windows.h> // necessário no Windows

int main() {
    // Define UTF-8 para entrada e saída
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);
    //%d = inteiro, %s = String, %f = float
    char nome[50]; //para salvar o nome da pessoa que testaremos se passou
    int quantasnotas; // Variável para guardar a quantidade de notas que a pessoa terá
    float soma = 0, media; // soma acumula as notas; media será calculada no final
    float minhanota; //nota de corte para ser aprovado

    //Pegando o nome da pessoa que queremos dizer se passou ou não
    printf("Digite seu nome: "); //escreve na tela 
    scanf("%s", nome); //campo de entrada de texto qual a pessoa digitará seu nome o %S refere-se a string

    //verificando a quantidade de notas a serem digitadas
    printf("Quantas notas queres lançar: "); //escreve na tela
    scanf("%d", &quantasnotas); //campo de entrada definido para inteiro onde digitará a quantidade de notas

    //vamos definir a nota de corte, nota de corte é qual a media para ser aprovado
    printf("Qual a média para ser aprovado? ex: 7.0: "); //pergunta com quantos pontos passa
    scanf("%f", &minhanota); //atribui a nata de corte a variavel minhanota



    //definindo um array de notas que terá o tamanho definido pela pessoa
    float notas[quantasnotas];

    //looping para ler e gravas a botas

    for (int i = 0; i < quantasnotas; i++){
        printf("Digite sua nota %d: ", i +1); //exibirar em qual nivel e qual nota será preenchida
        scanf("%f", &notas[i]); //recebe a nota e atribui ao array
        soma += notas[i]; //soma a nota ao total
    }

    //Gerando a média
    media = soma/quantasnotas; // média/pela quantidade de notas

    // Exibe os resultados
    printf("\nAluno: %s\n", nome);      // Mostra o nome
    printf("Média: %.2f\n", media);     // Mostra a média com 2 casas decimais

    //Agora vamos verificar se o aluno passou ou reprovol
    if(media >= minhanota){
        printf("Você está aprovado");
    }else{
        printf("Você está reprovado");
    }
    

    getchar(); getchar();
    return 0;
}
