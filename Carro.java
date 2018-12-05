class Carro {
  boolean estadoInicial = false;
  String chassi = "14789656522";
  String marca = "Fiat";
  String modelo = "Mobi";
  String tipoCombustivel = "Gasolina"; //Tipo de Combustivel:(Diesel, alcool ou gasolina)
  int numPassageiro = 5;
  float capacidadeTanque = 200;
  float nivelCombustivel = 0;
  float velocidadeAtual = 0;
  float velocidadeMax = 260;
  int cambio = 0;
  
  
   void Ligar() {
     if(this.estadoInicial == true) {
       System.out.println("O veiculo já está ligado");
     }
       
     else {
       System.out.println("Ligando o veiculo...");
       this.estadoInicial = true;
     }
   }
  
   void Desligar() {
     if(this.estadoInicial==false) {
       System.out.println("O veiculo já está desligado");
     }
     
     else {
           System.out.println("Desligando o veiculo...");
           this.estadoInicial = false;
       }

   }
  
   void Acelerar() {
     if((this.estadoInicial == true) && (this.velocidadeAtual<this.velocidadeMax)&&(nivelCombustivel>0)) {
       System.out.println("Acelerando o veiculo...");
           this.velocidadeAtual += 10;
           this.nivelCombustivel -= 5;

     }
     else {
       System.out.println("O carro deve estar ligado, sua velocidade não pode ser maior que a Máxima e possuir combustivel");
     }
     
     
   }
  
   void Freiar() {
     if (this.velocidadeAtual == 0) {
       this.velocidadeAtual = 0;
       System.out.println("O veiculo já se encontra parado");
     }
     else {
       System.out.println("Você pisou no freio...");
       this.velocidadeAtual -= 10;
       
     }
     
   }
  
   void Trocar_Marcha(int nova_marcha) {
       if((nova_marcha<0)||(nova_marcha>5)){
         System.out.println("Marcha inválida. Operação não foi concluida!");
       }   
       else {
           this.cambio= nova_marcha;
       }       
   }

   void Abastecer(int quantidadeL) {
     
     this.nivelCombustivel += quantidadeL;
     
     if(quantidadeL>this.capacidadeTanque) {
       System.out.println("Quantidade maior que a capacidade do tanque");
       this.nivelCombustivel = nivelCombustivel - quantidadeL;
           System.out.println("Capacidade Máxima:" + this.capacidadeTanque +  "litros");
     }   
       if(this.nivelCombustivel>this.capacidadeTanque) {
         System.out.println("O tanque está cheio!");
           this.nivelCombustivel = this.nivelCombustivel - quantidadeL;
           System.out.println("Nível do combustivel:" + this.nivelCombustivel + "litros");
         
       }   
   }
  
   void Mostrar_Status() {
     System.out.println("Estado do Veiculo: " + this.estadoInicial);
     System.out.println("Chassi: " + this.chassi);
     System.out.println("Marca: " + this.marca);
     System.out.println("Modelo: " + this.modelo);
  System.out.println("Tipo de Combustivel: "+ this.tipoCombustivel);
  System.out.println("Numeros de Passageiros: " + this.numPassageiro);
  System.out.println("Nivel de combustivel:"+ this.nivelCombustivel +  " litros");
  System.out.println("Capacidade do Tanque: " + this.capacidadeTanque + " litros");
  System.out.println("Velocidade atual: "+ this.velocidadeAtual + " KM");
  System.out.println("Velocidade Maxima:"+ this.velocidadeMax + " KM");
   }
   
}

