#define LED1 3
#define LED2 5
#define LED3 6

void setup() {
  Serial.begin(9600);

  // Configuración de pines
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);

  // Apagado inicial
  digitalWrite(LED1, LOW);
  digitalWrite(LED2, LOW);
  digitalWrite(LED3, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();

    // LED 1
    if (comando == 'a') {
      digitalWrite(LED1, HIGH);
      Serial.println("LED 1 encendido");
    } 
    else if (comando == 'A') {
      digitalWrite(LED1, LOW);
      Serial.println("LED 1 apagado");
    }
    // LED 2
    else if (comando == 'b') {
      digitalWrite(LED2, HIGH);
      Serial.println("LED 2 encendido");
    } 
    else if (comando == 'B') {
      digitalWrite(LED2, LOW);
      Serial.println("LED 2 apagado");
    }
    // LED 3
    else if (comando == 'c') {
      digitalWrite(LED3, HIGH);
      Serial.println("LED 3 encendido");
    } 
    else if (comando == 'C') {
      digitalWrite(LED3, LOW);
      Serial.println("LED 3 apagado");
    }
    // Mensaje de error para caracteres no válidos (ignora Enter y Salto de línea)
    else if (comando != '\n' && comando != '\r') {
      Serial.println("Valor no reconocido");
    }
  }
}