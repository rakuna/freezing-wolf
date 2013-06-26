const int Button_Pins[] = {2,3,4,5};    //Pushbutton pins
const int LED_Pins[] =  {10,11,12,13};  // LED pins
const int Buzzer_Pin = 9;               //Buzzer pin

const char Notes[] = {"cegb"};

int Button_State[] = {0, 0, 0, 0};
int Previous_Button_State[] = {0, 0, 0, 0};
int level = 1; //Initialises the current level (and associated code sequence)



void setup()
{
  for(int x = 0; x < 4; x++)
  {
    // Set up the pushbutton pins to be an input:
    pinMode(Button_Pins[x], INPUT);
    
    // Set up the LED pins to be an ouput
    pinMode(LED_Pins[x], OUTPUT); 
  }
  
  // Set up the Buzzer pin as an output
  pinMode(Buzzer_Pin, OUTPUT);
  
  // Initialises the serial communication.
  Serial.begin(9600);
}


void loop()
{
  int Random_Array[100]; // Initialises the random array with a defining limit of 100 levels
  int Delay_Time = 500;
  int Button_State_Test[] = {0,0,0,0};
  int error_made = 0;

  
  // Begin
  delay(500);
  char levels[] = "b";
  for (int i = 0; i < level; i++)
  {
    tone(Buzzer_Pin, frequency(levels[0]), 150);
    delay(300);
  }
  delay(500);
  
  // Generate the random code
  Serial.print("Generate: ");
  Serial.println();
  Serial.print("Level: ");
  Serial.print(level);
  Serial.println();
  
  
  for(int x = 0; x < level; x++)
  {
    Random_Array[x] = random(4);
  }
  Serial.println();

  
  // Display the random code
  Serial.print("Display: ");
  Serial.println();
  for(int x = 0; x < level; x++)
  {
    delay(Delay_Time/4);
    for(int y = 0; y < 4; y++)
    {
      if(Random_Array[x] == y)
      {
        Button_State[y] = 1;
      }
      else
      {
        Button_State[y] = 0;
      }
    }
    LED_Update();
    Play_Tone();
    Serial_State();
    Button_State_Update();
    Button_State_Change();
    delay(Delay_Time);
    LED_Update();
  }
  
  Button_State_Update();
  LED_Update();
  
  
  // Input and comparison to random code
  Serial.print("Input");
  Serial.println();
  for(int x = 0; x < level; x++)
  {
    Serial.print("Button State Testing: ");
    for(int y = 0; y < 4; y++)
    {
      if(Random_Array[x] == y)
      {
        Button_State_Test[y] = 1;
      }
      else
      {
        Button_State_Test[y] = 0;
      }
      Serial.print(Button_State_Test[y]);
    }
    Serial.println();
    
    
    
    // Waiting for a state transition
    while(State_Change_Check() != 2)
    {}

    Button_State_Update();
    LED_Update();

    while(State_Change_Check() != 1)
    {}
    
    LED_Update();
    Play_Tone();
    
    Serial.print("State_Change");
    Serial_State();
    Serial.println();
    
    // Check if correct state input
    
    for(int y = 0; y < 4; y++)
    {
      if(Button_State_Test[y] != Button_State[y])
      {
        error_made = 1;
        error();
        break;
      }
    }
  }
  if(error_made == 0)
  {
    level_up();
  }
}


void level_up()
{
  while(State_Change_Check() != 2)
  {}
  Button_State_Update();
  LED_Update();


  Serial.println();
  Serial.print("Level Up");
  Serial.println();
  level++; 
  
/*  int songLength = 18;
  char notes[] = "cdfda ag cdfdg gf ";
  int beats[] = {1,1,1,1,1, 1, 4,4,2,1,1,1,1,1,1,4,4,2};
  int tempo = 150;
*/
  int songLength = 8;
  char notes[] = "cdfda ag";
  int beats[] = {1,1,1,1,1, 1, 4,4};
  int tempo = 150;


  int i, duration;

  for (i = 0; i < songLength; i++) // step through the song arrays
  {
    duration = beats[i] * tempo;  // length of note/rest in ms
    
    if (notes[i] == ' ')          // is this a rest? 
    {
      delay(duration);            // then pause for a moment
    }
    else                          // otherwise, play the note
    {
      tone(Buzzer_Pin, frequency(notes[i]), duration);
      delay(duration);            // wait for tone to finish
    }
    delay(tempo/10);              // brief pause between notes
  }
}

void error()
{
  while(State_Change_Check() != 2)
  {}
  Button_State_Update();
  LED_Update();
  
  level = 1;

  int songLength = 7;
  char notes[] = "bagfedcba";
  int beats[] = {4,3,3,2,2,1,1}; //{1,1,2,2,3,3,4};
  int tempo = 50;
  
  int i, duration;
  
  for (i = 0; i < songLength; i++) // step through the song arrays
  {
    duration = beats[i] * tempo;  // length of note/rest in ms
    
    if (notes[i] == ' ')          // is this a rest? 
    {
      delay(duration);            // then pause for a moment
    }
    else                          // otherwise, play the note
    {
      tone(Buzzer_Pin, frequency(notes[i]), duration);
      delay(duration);            // wait for tone to finish
    }
    delay(tempo/10);              // brief pause between notes
  }

}

int Generate_Code(int length)
{
  int index;
  int delayTime;
  
  // The random() function will return a semi-random number each
  // time it is called. See http://arduino.cc/en/Reference/Random
  // for tips on how to make random() even more random.
  
  index = random(4);	// pick a random number between 0 and 3
  delayTime = 100;
}


void Play_Tone()
{
  int duration = 500;
  
  tone(Buzzer_Pin, Sound_Tone(), duration);
}

int Sound_Tone()
{
  for(int x = 0; x < 4; x++)
  {
    if(Button_State[x] == 1)
    {
      return(frequency(Notes[x]));
    }
  }
}





void Button_State_Update()
{
  for(int x = 0; x < 4; x++)
  {
    Button_State[x] = 1 - digitalRead(Button_Pins[x]); // Hardware button press = LOW, Software button press = HIGH
  }
}


int State_Change_Check() //Determines if a state transition has occured (0 = no transition, 2 = transition to base state, 1 = transition)
{
  // Get the most recent button states into memory
  Button_State_Update();
  int new_sum = 0;
  int old_sum = 0;
  for(int x = 0; x < 4; x++)
  {
    new_sum += Button_State[x];
    old_sum += Previous_Button_State[x];
  }
  if((new_sum == old_sum) && (new_sum == 0))
  { return(2); }
  
  for(int x = 0; x < 4; x++)
  {  
    if(Button_State[x] != Previous_Button_State[x])
    {
      Button_State_Change();
      return(1);
    }        
  }
  return(0);
}


void Button_State_Change()
{
  for(int x = 0; x < 4; x++)
  {
    Previous_Button_State[x] = Button_State[x];
  }
}


void LED_Update()
{
  for(int x = 0; x < 4; x++)
  {
    digitalWrite(LED_Pins[x], Button_State[x]);
  }
}


void Serial_State()
{
  for(int x = 0; x < 4; x++)
  {
    Serial.print(Button_State[x], Button_Pins[x]);
  }
  //     delay(150);
  
  Serial.println();
}


int frequency(char note) 
{
  // This function takes a note character (a-g), and returns the
  // corresponding frequency in Hz for the tone() function.
  
  int i;
  const int numNotes = 8;  // number of notes we're storing
  
  // The following arrays hold the note characters and their
  // corresponding frequencies. The last "C" note is uppercase
  // to separate it from the first lowercase "c". If you want to
  // add more notes, you'll need to use unique characters.

  // For the "char" (character) type, we put single characters
  // in single quotes.

  char names[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C' };
  int frequencies[] = {262, 294, 330, 349, 392, 440, 494, 523};
  
  // Now we'll search through the letters in the array, and if
  // we find it, we'll return the frequency for that note.
  
  for (i = 0; i < numNotes; i++)  // Step through the notes
  {
    if (names[i] == note)         // Is this the one?
    {
      return(frequencies[i]);     // Yes! Return the frequency
    }
  }
  return(0);  // We looked through everything and didn't find it,
              // but we still need to return a value, so return 0.
}

