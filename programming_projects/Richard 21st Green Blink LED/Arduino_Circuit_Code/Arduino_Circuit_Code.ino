/*
Hardware Layout:
 GND = GND pin of Arduino
 
 Pin 10 is connected to a 330 \Ohm resistor.
 330 \Ohm resistor is connected to the green pin of an RGB LED
 RGB LED common ground is connected GND
*/

const int GREEN_PIN = 10;

void setup()
{
  pinMode(GREEN_PIN, OUTPUT);
}


void loop()
{
  int delay_time = 1000;
  int x = delay_time/255;

  Green_Loop(x, delay_time);
}


void Green_Loop(int x, int delay_time)
{
  off_on(x);
  delay(delay_time);
  on_off(x);
  delay(delay_time);
}


void off_on(int delay_time)
{
  int greenIntensity;
  for (greenIntensity = 0; greenIntensity <= 255; greenIntensity++)
  {
    analogWrite(GREEN_PIN, greenIntensity);
    delay(delay_time);
  }
}

void on_off(int delay_time)
{
  int greenIntensity;
  for (greenIntensity = 255; greenIntensity >= 0; greenIntensity--)
  {
    analogWrite(GREEN_PIN, greenIntensity);
    delay(delay_time);
  }
}
