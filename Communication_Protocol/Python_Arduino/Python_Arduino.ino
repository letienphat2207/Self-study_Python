int x;
void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(13, OUTPUT);
}
void loop() {
  // digitalWrite(13, HIGH);
  // delay(500);
  // digitalWrite(13, LOW);
  // delay(500);

  while (!Serial.available())
    ;
  x = Serial.readString().toInt();
  if (x == 1) {
    digitalWrite(13, HIGH);

  } else if (x == 2) {
    digitalWrite(13, LOW);
  }
  Serial.print(x + 2);
}