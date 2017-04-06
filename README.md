
# LED ring for Marlin Delta
The LED ring interface for Marlin Delta firmware. It contains 16 RGB LEDs controlled by Arduino Pro Mini. Arduino Mega 2560 communicate with Arduino Pro Mini via one of its USART serial. Mega can either controlling LEDs from Mini Pro or updating firmware in it. Been doing this way could not only allow updating firmware in both Mega and Pro Mini also could do functional tests by only using the USB port on Mega.

# Sequence Diagram
Refers to sequence diagram png file in this repository.

# Pins Swap
## Original RAMP 1.4 Pinouts

|ATMEGA Pins|Functions|PORT|NAME        |Digital/Analog|Arduino Pin|Arduino Name|Purpose        |
|-----------|---------|----|------------|--------------|-----------|------------|---------------|
|2          |RXD0     |PE0 |RXD0/PCINT8 |Digital       |pin 0      |RX0         |Serial over usb|
|3          |TXD0     |PE1 |TXD0        |Digital       |pin 1      |TX0         |Serial over usb|
|45         |RXD1     |PD2 |RXD1/INT2   |Digital       |pin 19     |RX1         |Z-MAX          |
|46         |TXD1     |PD3 |TXD1/INT3   |Digital       |pin 18     |TX1         |Z-MIN          |
|12         |RXD2     |PH0 |RXD2        |Digital       |pin 17     |RX2         |on aux4        |
|13         |TXD2     |PH1 |TXD2        |Digital       |pin 16     |TX2         |on aux4        |
|63         |RXD3     |PJ0 |RXD3/PCINT9 |Digital       |pin 15     |RX3         |Y-MAX          |
|64         |TXD3     |PJ1 |TXD3/PCINT10|Digital       |pin 14     |TX3         |Y-MIN          |

Need to define following in Marlin "Configuration.h" header file to free up pins for serial port connected to Arduino Pro Mini.

```C
#define DISABLE_MIN_ENDSTOPS
```
Then swap Z-MAX pin 19 to Y-MIN pin 14 as follow.

```C
#define Z_MAX_PIN	14
```
This will leave pin 19 and 18 free for use with Arduino Pro Mini for LED-Ring serial interface. Z-MIN pin 18 is also used for autoleveling. Since auto leveling is only used when Arduino Mega is running it should not effect by this change. Now the pinouts changed as below.

|ATMEGA Pins|Functions|PORT|NAME        |Digital/Analog|Arduino Pin|Arduino Name|Purpose        |
|-----------|---------|----|------------|--------------|-----------|------------|---------------|
|2          |RXD0     |PE0 |RXD0/PCINT8 |Digital       |pin 0      |RX0         |Serial over usb|
|3          |TXD0     |PE1 |TXD0        |Digital       |pin 1      |TX0         |Serial over usb|
|45         |RXD1     |PD2 |RXD1/INT2   |Digital       |pin 19     |RX1         |LED-Ring Controller|
|46         |TXD1     |PD3 |TXD1/INT3   |Digital       |pin 18     |TX1         |LED-Ring Controller or Z-MIN/Autolevel|
|12         |RXD2     |PH0 |RXD2        |Digital       |pin 17     |RX2         |on aux4        |
|13         |TXD2     |PH1 |TXD2        |Digital       |pin 16     |TX2         |on aux4        |
|63         |RXD3     |PJ0 |RXD3/PCINT9 |Digital       |pin 15     |RX3         |Y-MAX          |
|64         |TXD3     |PJ1 |TXD3/PCINT10|Digital       |pin 14     |TX3         |Z-MAX          |

The Marlin firmware needs to be modified with existing or new g-code to pass data to TX1/RX1 port. This g-code also needs to control the Marlin modes (Normal running & Pass-Through) to communicate with Arduino Pro Mini LED-Ring controller. The communication protocol between Arduino Mega running Marlin and Arduino Pro Mini LED-Ring controller still yet to be defined.