
## Table of Contents ##

[An Industrial Raspberry Shield: MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#an-industrial-raspberry-shield-miniioex-3g)

[Who is for MiniIOEx-3G?](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#who-is-for-miniioex-3g)

[What is in the box?](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#what-is-in-the-box-)

[IO Handling](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#io-handling)

- [Test GUI Program](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#io-test-gui-program)

- [Digital Input](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#digital-input)

- [Digital Output](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#digital-output)

- [Analog Input](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#analog-input)

- [Reading Analog Input Values ](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#miniioex-3g-analog-input-read)

[Serial Port](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#serial-port)

[3G / GPS Commissioning](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#3g--gps-commissioning)

- [GPS Commissioning](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#gps-commissioning)

[RTC and EEPROM Usage](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#real-time-clock-and-eeprom)

[Application Notes](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#application-notes)

- [FAN Motor Control](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#sample-1--fan-motor-control-with-startstop-button-on-miniioex-3g)

- [FAN Motor Control Using WEB Reference](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#sample-2--controlling-of-fan-motor-with-startstop-and-web-reference)

- [Reading Values from energy Analyzer via RS485](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#sample-3--reading-values-from-energy-analyser-via-rs485)

- [Controlling Siemens AC Motor by ABB Motor Driver via RS485](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#sample-4--ac-motor-control-by-using--ac-motor-driver-with-miniioex-rs485)

- [Reading Analog Values from Siemens CO2 Sensor](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#sample-5---reading-values-from-siemens-co2-sensor)

- [Danfoss FC51 Motor Driver Control via Modbus RTU](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#sample-6---danfoss-fc51-motor-driver-control-via-modbus-rtu)
- [Battery Voltage Read](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#sample-7---reading-battery-voltage-and-monitoring)

[Other Topic](https://github.com/pe2a/miniIOEx3G#other-topic)

- [Installing Raspbian OS](https://github.com/pe2a/miniIOEx3G#installing-raspbian-os)

- [How to Find MAC ID of Raspberry Pi](https://github.com/pe2a/miniIOEx3G#How-to-find-your-MAC-ID-of-your-Raspberry-Pi)

[Support](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#support)

[BUY](https://github.com/pe2a/miniIOEx3G/blob/master/README.md#buy)


# An Industrial Raspberry Shield: MiniIOEx-3G #

MiniIOEx-3G is Raspberry Pi shield that can be used in industrial areas with 3G Module. MiniIOEx-3G has affordable price to use with Raspberry Pi. You can easily commissioning shield and you can easily integrate in your projects.  

There are very useful informations for engineers and interested people in the automation field, who are new to the IOT sector and who want to communicate with machines in this study. In this document, examples are often given in languages such as C / C ++ and Python. However, this document will mention many things like Raspberry Pi's control of GPIO pins, serial port applications, transferring data from servers to servers, exiting internetting using 3G feature, using USB ports.Using this information, you can also develop your ideas about how you can improve your progeny and use Raspberry Pi.

MiniIOEx-3G has specifications mentioned at below:

| Technical Data  	| MiniIOEx-3G      |
| ------------- | ------------- |
| Digital Input | 	2ch(<4V FALSE, >4V TRUE ) |
| Digital Output |	4ch (2ch Relay@5V, 2ch transistor@24V) |
| Analog Input	 | 2ch 12bit 0-30V OR 2ch 12 bit 4-20mA |
| SeriPort	| RS232 OR RS485 |
| Power Input 	| 24V on Terminal OR 5V on RPI USB | 
| 3G Module	| QEUCTEL UC20/EC20 MiniPCI  |
| EEPROM	| 32kBit | 
| Real Time Clock | 	Yes |
| Size with Case	| 80x94x42mm(WxLxH)|
| Weight	| ~30gr |

You can easily integrate RS232 / RS485 to communicate with other devices. If you have no Ethernet or Wireless possibility in the fields so MiniIOEx-3G can be used with IO features. If MiniIOEx-3G will be used in industrial area and it is provided 24V DC input on MiniIOEx-3G terminal. Else, you can use 5V on Raspberry Pi USB for boosting MiniIOEx-3G. 

We have some pictures for industrial shields at below:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3369.jpg)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3373.jpg)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3380.jpg)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3383.jpg)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3378.jpg)

*The MiniIOEx-3G has standart sheet metal case.*

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3367.jpg)

*The terminal on which the IOs are located is specified on the MiniIOEx.*

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3435.jpg)

*MiniIOEx-3G has standard industrial terminal.*

MiniIOEx-3G has standart **Metal Sheet** to be used in electrical panels and industrial fields. So, you can easily mount it your projects. MiniIOEx-3G has also industrial 2x12 push-in terminal. Because of this feature, you will not worry cable installation time and robustness. For the MiniIOEx Terminal, the reference ground for all inputs is the 0 V power contact. The wires can be connected without tools in the case of solid wires using a direct plug-in technique. 

MiniIOEx terminal features:

| Terminal Features	| Comment |
| ------------- | ------------- |
| Terminal Number	|2x12 |
| Nominal Voltage	| 300V |
| Nominal Current	| 8A |
| Resistance Voltage	| 2000V |
| Max. Cable Size	| 2.5mm2 |
| Working Temperature	| -40C   +105C |



## Who is For MiniIOEx-3G? ##

The Raspberry-based control solutions enable you to run any applications for vaious IOT platforms: building automation, urban automation, smart city applications to operate and monitoring. MiniIOEx significantly reduces hardware and software costs and there is also not any licence prices thanks to Raspberry Pi. 

When developing industrial automation projects, the most important feature is to use high level languages such as C / C ++ / Python / JAVA in PLC, uploading data/pictures etc. to server, to reduce load on SCADA by installing local database on PLC. GUI applications on Raspberry Pi, retrieving data over serial port or direct IOs, and transferring the data to a server / creating WEB application are very easy. That's why Raspberry Pi has an operating system on it and it provides that we can program on Linux. 

There are many Raspberry Pi education cards on the market, but we can not use any of these cards in our industrial projects. That's why I witnessed many Raspberry Pi's being taken for the first time with enthusiasm. We want to you make your projects will be work in real fiel with our industrial shields with MiniIOEx, MedIoEx etc. 

So if we're going to sum it up, who's MiniIOEx for?

- Building Automation,
- Urban Automation,
- IOT applications,
- End user,
- Energy Monitoring via seri port, 
- Ship automation,
- Machine Tools,
- Robotics in Handling, Production and Assembly,
- Handling and Assembly Technology,
- Railway applications, 
- AV and Media Technology,
- Real time data stream,
- Camera stream via 3G,
- Students/Engineers who aim to develop about Embedded Linux plaftorms. 


![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/miniIOex_poster_01.jpg)


## What is in the box ? ##

If you just buy *MiniIOEx* without 3G module :

- MiniIOEx
- MiniIOEx Metal Sheet
- Sheet mount parts

If you buy  *MiniIOEx-3G* with **3G module** :

- MiniIOEx
- Quectel UC20 MiniPCI Express Module
- GPRS Antenna 
- GPRS Antenna Cable
- MiniIOEx Metal Sheet
- Sheet mount parts

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/miniIOex_poster_02.jpg)

# IO Handling #

MiniIOEx has Digital Input, Digital Output and Analog Input functions for your IOT/IIOT applications. Digital IOs are directly connected Raspberry pin to pin and Analog Input is connected over SPI. So, you will use SPI functions to get Analog Input Data. 

At the below table, you can find which MiniIOEx pins are connected to Raspberry PINs. 

| IO  	| Raspberry GPIO Place |
| ------------- | ------------- |
| Digital Input 1 	| 31 |
| Digital Input 2	| 33 |
| Digital Output Relay 1	| 35 |
| Digital Output Relay 2	| 36 |
| Digital Output  Transistor 1	| 38 |
| Digital Output  Transistor 2	| 40 |
| Digital Output  *RUN* LED	| 37 |

# Terminal Number #

Terminal naming becomes very important when you develop applications in the field.
Terminal addresses can easily be used in MiniIOEx.Terminal number is added at below figure with table. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/MiniIOEx_terminalNumber.PNG)

Terminal numbers are listed below:

|24V|RL2_NO|RL1_NO|DIG_OUT_2|DIG_OUT_1|AI_IN2|AI_IN1|DIG_IN2|DIG_IN1|RS232_TX OR RS485_A| 
| ------------- | -------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
|GND|RL2_COM|RL1_COM|GND|GND|GND|GND|GND|RS_GND|RS232_RX OR RS485_B|

All terminal numbers and comments can be found in the table below.

| IO  	| Terminal Number | Comment |
| ------------- | ------------- |------------- |
| 0V 	| 1 | |
| 24V	| 2 | |
| RL1_COM	| 3 | UP TO 24VDC|
| RL1_NO	| 4 | |
| RL2_COM	| 5 |UP TO 24VDC|
| RL2_NO  	| 6 | |
| GND	| 7 |
| DIG_OUT_2	| 8 | 24VDC,max. 80mA |
| GND	| 9 | |
| DIG_OUT_2	| 10 |  24VDC,max. 80mA | 
| GND	| 11 | |
| AI_IN2	| 12 | 0-30VDC or 4-20mA|
| GND	| 13 | |
| AI_IN1	| 14 | 0-30VDC or 4-20mA |
| GND	| 15 | |
| DIG_IN_2	| 16 | UP TO 30VDC |
| RS_GND	| 17 | ALL GND IS SHORT-CIRCUITED |
| DIG_IN_2	| 18 | UP TO 30VDC |
| RS232_TX OR RS485_B	| 19 | |
| RS232_RX OR RS485_A	| 20 | |



## IO Test GUI Program ##

You can use the GUI program to control all IOs. To use this program, you need to do the following:

- SPI -> *enable*
- Install spidev library 
- Run the program by using *"python3 testGUI.py"* command 

After the running, you should see GUI as follows :

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/testGUI.PNG)

The code you can access: https://github.com/pe2a/miniIOEx3G/blob/master/testGUI.py


## Digital Input ##

We mentioned before MiniIOEx-3G has 2ch Digital Inputs. Digital Input on MiniIOEx has given characteristics at below table:

| Technical Data  	| Digital Input |
| --- | --- |
| Terminal Connection 	| 2 Wire |
| Digital Input Channel	| 2 |
| Nominal Voltage	| 24V |
| “0” Signal Voltage	| 0..3.9V |
| “1” Signal Voltage 	| 4.2V..30V |
| Input Filter	| - |
| Confituration	| GPIO or bcm2835 library install |

| IO  	| Raspberry GPIO Place |
| ------------- | ------------- |
| Digital Input 1 	| 31 |
| Digital Input 2	| 33 |


![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/27.jpg)

*MiniIOEx Digital Input Terminal*

Terminal 16 and 18 is Digital Input connection point. You can easily mount your cable with **ground** on terminal. 

Sample connection of buttons:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/28.jpg)

*MiniIOEx Digital Input Connection Diagram*

Given in the example code, you can monitor your Digital contacts/switches/buttons etc.

**di_test.py**

```python
import RPi.GPIO as GPIO
import time

#definition GPIO
RASP_DIG_IN_1 = 6   #DI_1
RASP_DIG_IN_2 = 13  #DI_2

#init function
GPIO.setmode(GPIO.BCM) #bcm library
#for digital inputs
GPIO.setup(RASP_DIG_IN_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RASP_DIG_IN_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setwarnings(False)

while 1:
    DI_In1 = not GPIO.input(RASP_DIG_IN_1)
    DI_In2 = not GPIO.input(RASP_DIG_IN_2)
    
    if  DI_In1:
        print(“DI_IN_1 : True”)
    if DI_In2:
        print(“DI_IN_2 : True”)
    time.sleep(1) #for holding time   
```
You can run program with at below command. 

```sh
python3 di_test.py
```

## Digital Output ##

MiniIOEx-3G has 4ch Digital Outputs. 2ch relay and 2ch 24VDC transistor you can use. Load resistors are set up to allow the transistors to draw no more current and a maximum current of 80mA is allowed to be drawn. If you need more load, you can use the relays on MiniIOEX or external relays to connect these transistors.

You can view the Digital Outputs on the MiniIOEx in the following table:

| Raspberry Pi Pin 	| MiniIOEx3G | 
| --- | --- |
| 35	| Digital Output Relay - 1 |
| 36	| Digital Output Relay - 2 |
| 37	| Digital Output RUN LED |
| 38	| Digital Output Transistor 2 |
| 40	| Digital Output Transistor 1 |


**Important Note**

**If you supply MiniIOEx with 24V, you can use all Digital Output pins. You can only use Relay outputs if you supply directly from Raspberry via 5V USB.**

| Technical Data  	| Digital Output | 
| --- | --- |
| Terminal Connection |	2 wire |
| Digital Output Relay | 	2ch |
| Digital Output Transistor 	| 2ch |
| Relay Switch Current and Volatge	| 1A,24VDC |
| Transistor Switch Current and Voltage	| 80mA, 24VDC |
| Configuration	| GPIO or bcm2835 library install |


![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/29.jpg)
*MiniIOEx Relay Datasheet Informations*

With MiniIOEx, many basic automation operations can be performed. For example, the data can be sent to the central servers from a device via RS485 / RS232 and then the device can be started / stopped / performance monitored with this information. When we look at the whole of document, many examples like this are shared.

The following codes uses all Output of MiniIOEx: https://github.com/pe2a/miniIOEx3G/blob/master/output.py

```python
import RPi.GPIO as GPIO
import time
import random 

DO_Relay1 = 19 #relay1 1A,24VDC
DO_Relay2 = 16 #relay2 1A,24VDC
DO_TR1 = 21 #TRANSISTOR 2A,5VDC
DO_TR2 = 20 #TRANSISTOR, 2A,5VDC
DO_RunLed = 26 #RunLED on PCB 

#init function
GPIO.setmode(GPIO.BCM) #bcm library

GPIO.setup(DO_Relay1,GPIO.OUT)
GPIO.setup(DO_Relay2,GPIO.OUT)
GPIO.setup(DO_TR1,GPIO.OUT) #LOW ON, HIGH OFF
GPIO.setup(DO_TR2,GPIO.OUT) #LOW ON, HIGH OFF
GPIO.setup(DO_RunLed,GPIO.OUT)

GPIO.setwarnings(False)

while (1):
	
	
	#led 
	GPIO.output(DO_RunLed,GPIO.HIGH) #ON
	time.sleep(0.2) #200ms
	GPIO.output(DO_RunLed,GPIO.LOW) #OFF
	time.sleep(0.2) #200ms
	
	#relay1 
	GPIO.output(DO_Relay1,GPIO.HIGH) 
	time.sleep(0.2) #200ms
	GPIO.output(DO_Relay1,GPIO.LOW) 
	time.sleep(0.2) #200ms
	
	#relay2 
	GPIO.output(DO_Relay2,GPIO.HIGH) 
	time.sleep(0.2) #200ms
	GPIO.output(DO_Relay2,GPIO.LOW) 
	time.sleep(0.2) #200ms
	
	#mosfet1 
	GPIO.output(DO_TR1,GPIO.LOW) #ON
	time.sleep(0.2) #200ms
	GPIO.output(DO_TR1,GPIO.HIGH) #OFF
	time.sleep(0.2) #200ms
	
	#mosfet2 
	GPIO.output(DO_TR2,GPIO.LOW) 
	time.sleep(0.2) #200ms
	GPIO.output(DO_TR2,GPIO.HIGH) 
	time.sleep(0.2) #200ms
```


## Analog Input ##

The *MiniIOEx-3G* has the *MCP3208* Analog Input integration. With this integration, it is possible to receive voltage / current information from the field at **12bit** resolution and process this data on Raspberry. Raspberry and ADC integration communicate with each other via SPI. Raspberry has 2 Chip Selects. These bus lines can be programmed as desired. The ADC integration is connected to CS0. By default, the SPI bus is 'disabled'. This can be enabled / disabled via "raspi-config" or manually via the "raspi-blacklist.conf" file, depending on the library to be used.

With the MCP3208 ADC integration it is possible to receive ~ 75000 data at the moment. At 3.3V, the ADC integration has ~ 63kSPS. From this value, the value of SCLK is 24bit * 63 000 = 1.5MHz. At 16 μs, the ADC integrate can read / write. If you want to take sampling in such a short interval, it might be a problem for embedded system platforms running on the operating system. Therefore, in our ADC programs on Raspberry ~ 1ms 'delay' data acquisition will be correct in terms of program sustainability. 

We will give some examples of what we can do in our code.

The table below shows which PINs are used on Raspberry:

| PIN Name  	| Raspberry GPIO Place | 
| --- | --- |
| Chip Select |	CS0 - 24 |
| SDO	| 19 |
| SDI	| 21 |
| SCLK	| 23 |
	
According to this table, an external SPI ADC communication library can also be created for MiniIOEx. The following steps must be followed to read the ADC data:
- Installing the SPI library
- Raspberry SPI enable / disable based on installed library
- Terminal cable installation or reading of input supplies

When using SPI libraries in Raspberry, different configuration settings need to be made in different software libraries.

| Library Name	| SPI Enable / Disable | 
| --- | --- |
| bcm2835 (C) 	| **Disable** |
| Wiring Pi  (C) | 	**Enable** |
| SpiDev (Python) |	**Enable** |

When we use the above libraries, we also need to make the necessary settings in Raspberry Pi. So, if you are using the bcm2835 library **SPI -> Disable** 
Otherwise your program will likely get 'fatal error' at 'Run Time' even if it does not get an error in 'Compile Time'. Raspberry's new models  have **BCM2836** or **BCM2837** chips are used. So do not think bcm2835's library will not work. The bcm2835 ibrary is compatible with  all bcmXX  models.


## MiniIOEx-3G Analog Input Read ##

MiniIOEx-3G can provide 2ch analog inputs can be received from the field. The MiniIOEx also reads the voltages on the 5V and 24V internal supply. The value of the field shall be max.**33.0V**. Sensors with a **4-20mA** variable current source can also be installed in the MiniIOEx-3G. Be careful with the possibility of damaging the Raspberry or MiniIOEx-3G when you are at higher voltages. 

In the following image, the Analog Input model between MiniIOEx-3G and Raspberry Pi integration is explained. As seen in this model, the 5V and 24V readings are carried out with the voltage divider on the MiniIOEx and there are 2ch Analog Input inputs that MiniIOEx-3G can read from the field. You can read MiniIOEx-3G input voltages from the relevant library and use them in your operations.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/35.jpg)

*MiniIOEx Analog Input*

The following table contains the terminal numbers for the analog data to be input from the field. 

| Physical Input | MiniIOEx-3G Terminal No | 
| --- | --- |
| Analog Input 1 |	14 |
| Analog Input 2 |	12 |
| Analog Input GND |	13 |
| Analog Input GND |	11 |

You can use the MiniIOEx-3G Analogue Input Module by wiring the following terminals:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/36.jpg)

*MiniIOEx Analog Input Terminal Number*

**IMPORTANT NOTE**

**To use the analog input module as a 4-20mA sensor input, the following buttons must be pulled in the direction of ON.**

![Image of MiniIOEx-3G](http://pe2a.com/docs/img/miniioex/37.jpg)

*MiniIOEx 4-20mA Selection Button will be pulled in the direction of ON*

In the applications we saw on the field, there was a request to measure Raspberry's input voltage or battery voltage. Therefore, you can measure 5V and 24V power input supplies directly from Raspberry via MiniIOEx without any external cabling.

**IMPORTANT NOTE**

**There is no need to take any end from your 24V or 5V supply source and enter the MiniIOEx connector. These input feeds are measured internally on MiniIOEx.**

To describe with a sample scenario; You feed the MiniIOEx with the battery and the battery voltage is dropping. If this voltage is never tracked, you can only understand it when Raspberry is shut down. If you follow the battery voltage, you may be warned when the battery voltage begins to fall and when it drops below the critical level, you can turn off all files running on the Raspberry.

Sensors used in industrial applications generally have * 0-10V * and * 4-20mA * outputs. As mentioned above, the MiniIOEx allows up to 33V . So you can use these sensors with MiniIOEx you can easily measure.

Everything is measured **DIGITAL** when operating in microprocessors. That is, although the outputs of the sensors are voltage, they are reflected in the ADC integrations as **DIGITAL** according to the resolution. In MiniIOEx, we also digitally measure the voltage information from the field. If this incoming **DIGITAL** value is written we can write simple functions to convert real sensor value. 

The following table shows the voltage limit values for the MiniIOEx Analog Input read data and the corresponding **DIGITAL** values.

| Analog Input Voltage Min. 	| Analog/Digital Circuit(ADC) Min. Digital Value |
| --- | --- |
| 0V	| 0 |


| Analog Input Voltage Max. 	| Analog/Digital Circuit(ADC) Max. Digital Value |
| --- | --- |
| 33.0V	| 4095 |

From there, the necessary functions can be written in the software. In this document, how to read the sensor data and translate it into meaningful values will be explained with examples.

The ADC circuit of MiniIOEx-3G provides data exchange via SPI. Therefore, Raspberry Pi SPI libraries are also used to read from MCP3208. How these libraries are used is also shared in this document with different programming language examples. The MCP3208 circuit 8 channels. Only 4 of these channels are used in MiniIOEx.

| Physical Input	| MCP3208 Channel Name |
| --- | --- |
| Analog Input 1	| 0 .  |
| Analog Input 2	| 1 .  |
| Analog Input 3 (Raspberry Pi Power In - 5V) |	6. |
| Analog Input 4 (MiniIOEx-3G Power In - 24V) |	7. |

As shown in the table above, the 6th and 7th legs of the MCP3208 circuit are used to measure the voltages on the Raspberry Pi and MiniIOEx-3G. When you run the Analog Input test code written in Python, you should see values of ~ 620 on channel 6. This value is the Raspberry Pi feed input voltage given in the above table. With a simple calculator it is possible to transform this digital value into a truly meaningful value.

## Reading Analog Input Value from MiniIOEx-3G ##

The following values are fixed values for MiniIOEx Analogue Reading functions. When you write your own function, you can use the following limit values.

- Digital value read from the Entire (x),
- Max. 12bit ADC Digital Value -> 4095 (2 ^ 12),
- Max. Field Input Voltage -> 33V.

As a result, if we want to find the voltage value of the power supply supplied by Raspberry, we have to solve the following equation:


 *eq1.* Power Supply Input Voltage = (Digital Data (x) * Max Field Input Voltage) / (Max.Digital Data)
 *eq2.* Power Supply Input Voltage = (620 * 33V) / (4095) = 4.996V

In order to read the digital value from the MCP3208 integration, the code block below is shared and the conversion of this value to voltage and sensor data is detailed in the headers of the document. 

**Important Note**

**Since the Python library is used, **Raspi-Config -> Interfacing Options -> SPI** *enable* is required.**

```python
def readAI(ch):
        if 7 <= ch <= 0:
            raise Exception('MCP3208 channel must be 0-7: ' + str(ch))

        cmd = 128  # 1000 0000
        cmd += 64  # 1100 0000
        cmd += ((ch & 0x07) << 3)
        ret = spi.xfer2([cmd, 0x0, 0x0])

        # get the 12b out of the return
        val = (ret[0] & 0x01) << 11  
        val |= ret[1] << 3           
        val |= ret[2] >> 5           

        return (val & 0x0FFF)  
	
	
#digital value for 5V

print(readAI(6))

```

The equivalence of the above Python code written in C language is as follows. You can select the code block for which you want to work with the programming language in your work.

```c
//AI reading channel val
int smallex_getVal(const int channel){
    char tbuf[3]; //transmitting values to mcp3208
    char rbuf[3]; //reading value from mcp3208
    
    int adc = 0;
    int adcDigNumber = 0;
    
    if(channel == 0){
        
        //ch0
        tbuf[0] = 0b00000110;
        tbuf[1] = 0b00000000;
        tbuf[2] = 0b00000000;
        
    }
    if(channel == 1){
        //ch1
        tbuf[0] = 0b00000110;
        tbuf[1] = 0b01000000;
        tbuf[2] = 0b00000000;  
    }
                    
    if(channel == 6){
        
        //ch6
        tbuf[0] = 0b00000111;
        tbuf[1] = 0b10000000;
        tbuf[2] = 0b00000000;
            
    }
    
    if(channel == 7){
        
        //ch7
        tbuf[0] = 0b00000111;
        tbuf[1] = 0b11000000;
        tbuf[2] = 0b00000000;
        
    }
    
    bcm2835_spi_transfernb(tbuf, rbuf,sizeof(tbuf));
    adcDigNumber = (rbuf[1] << 8) + rbuf[2];
    adcDigNumber &= 0xFFF;
    
    return adcDigNumber; //should be 0 - 4095
```

You can use this function block in your program. You can also check this value with any voltage meter (multimeter).
Since there is no voltage dropping element on the MiniIOEx in the 5V line, this value is the voltage that Raspberry feeds directly. However, you need to add approximately 1.4V (0.7V * 2) to the voltage value that you measure the 24V value because the following bridge diode is on the 24V line. In the illustration below you can see the MiniIOEx-3G power supply input bridge diode connection.

<img src="https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/38.jpg" alt="drawing" width="250"/>

As you can see above pictures, MinIOEx has bridge diode for 24V power in. 


## Serial Port ##

Serial communication is a type of communication that operates on software protocols specified in the standard on the physical shell specified in the telecom standards and allows for bi-directional data communication. In industrial systems, RS232 and RS485 protocols generally come to mind in terms of serial communication. MiniIOEx supports RS232 and RS485 physical communication serial paths. RS-232 is a serial communication standard designed for short distance communications. The information transmitted via RX and TX is determined according to the reference level GND. With RS-232, short distances and speeds of 115.2 Kbit / s can be achieved. This standard is not suitable for noisy environments. RS-232 drives are not designed to be able to sustain many receivers at the same time.

Data is transimitted throug a serial port 1 bit at a time. This differs from the transmission of data
through a parallel port, which sends 1byte at a time. The transmission is called asyncronous because
the length of time that passes between thre transmission of each byte of data(1 bit at a time) does
not amtter. However, both the timing and sequence of the transmission of the bits that compose the
byte and some other information are critical.

Each byte of data transmitted by the serial port uses this sequence of signals:
- One start bit
- Eight data bits(seven in some siuations)
- Optional partiy bit
- One or two stop bits

The start bit signals the start of the transmission of a new byte by driving the line low for one cycle. The data bits are then transmitted, followed by an optional parity bit. Finally, 1 or 2 stop bits are sent, which also drive the line low. The stop bits determine the shortest time between bytes. Usually, it does not matter a great deal whether you use 1 or 2 stop bits, as long as both the transmitting port and the receiving port use the same number. The parity bit, if supplied, checks for errors in transmission. Parity can be either even or odd. If even parity is selected, the parity bit is set in such a way that an even number of 1 bits will be transmitted. If odd parity is used, the parity bit will be set so that an odd number of 1 bits is transmitted. for further informatioın please check out the book name of **The Art of C: Elegant Programming Solutions, Herbert Schildt**

UART (*Universal Asynchronous Receiver / Transmitter*) serial bus provides serial communication with two cables on Raspberry as standard. With Raspberry 3, serial port settings can be made on the "raspi-config" screen. Raspberry Pi should be restarted after these changes are made. This document explains how to make these settings. Tx and Rx pins on Raspberry Pi are responsible for serial communication. Raspberry can easily communicate with a device on another serial port hardware. If Raspberry will communicate with another serial port device, "console login" feature should be removed. These changes will also be mentioned.

The RS-485 is a serial transmission developed for use at longer distances, in noisy environments, where higher speeds are required. MiniIOEx-3G also supports these two serial transmission routes.

The serial port PIN table on the MiniIOEx is shared below.

MiniIOEx Seri Port Pin table is given at below:

| Serial Port Pin | MiniIOEx-3G Terminal No | 
| --- | --- |
| RS232-RX	| 19 |
| RS232-TX	| 20 |
| RS485-B	| 19 |
| RS485-A	| 20 |
| Serial GND	| 17 |

Since Raspberry has a single UART output, we use serial port converters in MiniIOEx: UART / RS232 and UART / RS485. You can control a button on MiniIoEx and you can choose which serial port can be used. It should be known RS232 uses three cables and RS485 uses two cables. 

If we can not use these two converters at the same time, we have to make a choice. You can choose according to the serial port you will use as follows: For RS485, you can push upwards the switches, for RS232 you can choose the other direction.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/40.jpg)
*RS485 Selection*

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/41.jpg)
*RS232 Selection*

To change the serial port selection buttons while the serial port terminal is plugged into a device: It may break the integrations on MiniIOex. Therefore, if any serial port is selected, the buttons need to be adjusted in that direction before connecting to the device.

We need to use the Raspberry Pi configuration tool to configure the serial ports. In the terminal, we write ** "raspi-config" **.

```sh
$raspi-config > Interfacing Options > Serial 
```
After pressing the "enter" key on the **"Serial"** menu, follow the steps below.

**On the Login menu, use Serial Port> Off (No)**

If this menu is missed, the program using the serial port will fail when it starts to work. Therefore, in order to use Login, serial port must be closed.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/42.jpg)
*Serial Port Using Login Shell*

**Serial Port Hardware Use -> On / (Yes)**

This menu makes the Raspberry Pi serial port terminals programmable.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/43.jpg)
*Serial Port Hardware Usage*

When all the processes are finished, we need to see a screen like this:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/44.jpg)
*Serial Port Usage Informations*

With the "minicom" program that can run on Raspberry, you can see the variables coming from Raspberry via serial port or give any reference through this program.

If you want to install the Minicom program, you can follow the steps below:

**1. Minicom Install:**

```sh
$sudo apt-get install minicom 
```

**2. Minicom Starting Program**

If you use before Raspberry Pi 3 version, you need to use port adress as being "ttyAMA0". 

```sh
$sudo minicom -b 9600 -o -D /dev/ttyAMA0 
```
If you use  Raspberry Pi 3 version and the others, you need to use port adress as being "ttyS0". 

```sh
$sudo minicom -b 9600 -o -D /dev/ttyS0

```
The 9600 number entered in the parameter is the baudrate rate. You can change this speed according to the standard speeds. Usually this value is also used in 115200. After this process, you can send or receive data to Raspberry by using serial port from any PC or any other device. You can change these settings with the ** "minicom -s" ** parameter.

In this document we will illustrate with practical examples how we can obtain data via **"Entes MPR63 Energy Analyzer"** using RS485 as an example.


## 3G / GPS Commissioning ##

One of the most important and basic features of the MiniIOEx is that it has a structure that is compatible with 3G and 4G communication. So if you are in a place where Wireless and Ethernet are not available or if work is being done on site, data communication with 3G is the most convenient method. This communication can be fully exploited from the data exchange capacity of 3G since it is realized via USB rather than through serial port. 3G services have been added to the MiniIOEx because some service providers can not provide full performance on 3G services. It is compatible with MiniIOEx-3G, Raspberry V2, V3, Zero devices and software tests have been tested on Jessie and later operating systems. Quectel 3G Module can provide 14.4 Mbps downlink and 5.76 Mbps uplink service. Due to its compact and modular structure, it can be easily used in projects with MiniIOEx-3G. If you did not purchase the MiniIOEx with the 3G module, it will be enough to place only 3G module in your plans in the future.
Where MiniIOEx-3G is available:

- IOT applications,
- Exporting data from another PLC or PC,
- Remote monitoring of industrial machines,
- Real Time Data stream operations,
- Camera stream operations,
- Transferring images via camera etc.

The fact that the MiniIOEx can be fed with 24V is a very useful feature for industrial environments. For an application that consumes too much power and draws instantaneous pulsating currents like 3G, it is very important for the continuity of communication that there is a 24V supply alternative. Many tests and studies have been conducted on this subject. Below are 2 oscilloscope screenshots. These are the graphs of voltage the 3G modem tries to connect to the first internete. As you can see in this chart, there is a voltage drop due to the flow in the red box. This voltage drop has been tried to be kept at the lowest voltage possible. The module does not operate by resetting the module itself at any serious voltage drop because it operates with 3.3V precision supply voltage. Therefore, it was tried to obtain a linear voltage graph at the module feed.


![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/52.jpg)

*Voltage Graph during 3G Module Connection*

As shown in the oscilloscope screen image below, the voltage is steady state even though the data download / upload operations after connecting the internet.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/53.jpg)

*After 3G connection Voltage Graph*

As a result of this work MiniIOEx and 3G module works synchronously and efficiently. In the following chapters, the commissioning of the 3G module is shown. The products listed below are needed to perform these operations.
- USB Cable
- Antenna
- Antenna cable

These products are shipped in the product package when you buy MiniIOEx-3G. There is no need to buy an external material.

## Configuration of 3G Connection ##

We can test the Quectel 3G module using the following steps:

- Fitting on Quectel Modul Shield,
- Placement of the SIM card on the module,
- Installation of Raspberry on Shield,
- Installation of USB cable to Raspberry Pi,
- Installation of 3G antenna on Quectel UC20 module.

Once the physical module and the Raspberry have been installed, the corresponding 'scripts' can be activated to activate the 3G module. As expected, the 3G module requires a high current source in the internete coupling stage. If this current is not met, the voltage drops and the module resets itself. This topic is about sahada and lab. We did a lot of research / development in our tests. In MiniIOEX and similar 3G products, we have also ensured that this voltage regulator protects our 3G connection more stable.
6- It is recommended to operate the latest operating system on the operating system. The Minicom program displays the data received from the serial port sockets for SIM card and the Module tests. For **speedtest-cli**, you can also use the device's internete connection speed for testing purposes.

Relevant examples are given in the text.

- sudo apt-get update
- sudo apt-get minicom
- sudo apt-get speedtest-cli
- sudo apt-get rpi-update
- sudo apt-get upgrade
- sudo reboot
- git clone git: //github.com/pe2a/miniIOEx3G.git

After the installation is finished, the terminal is opened and the **lsusb** command is executed. This command then shows the devices connected to the USB. If there is no situation, you should see a screen like below. If we can not see Quectel UC20 Module, it could be the Quectel UC20 module or the USB cable itself. For this situation, It may be beneficial to insert and remove the module. 

**Important Note**

**Installation work on the module should be done without energy**

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/54.jpg)

*Other USB ports on the screen can be wireless keyboard / mouse or portable USB disk.*

Since MiniIOEx-3G physically connected to USB, we can send the **AT** commands.  AT commands can be used communicating with the 3G module. With these commands, the information on the device can be queried as well as features such as SMS and Search can be performed by these commands. Just write these commands on the Minicom. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/55.jpg)

The description of the basic AT commands in the red block is given below:

1-) Quectel device serial number -> **ATI**

2-) Indicates that the Sim card is ready for use if there is no problem with Sim Lock on the device. You can disable the SIM card PIN feature on any mobile phone if you have just bought a SIM card: **AT + CPIN?**

3-) Indicates whether the network is ready or not. If the network is not ready, you can return the CME Error  and see what error it is on the following document: **AT + CREG?**

4-) The net capacity of the net. This ratio changes according to the quality of the antenna, the proximity of the base station and the environmental factors. Below 30 is acceptable. 99.99 indicates no network capture: **AT + CSQ**

5-) Shows the operator of the SIM card on the card. Vodafone SIM card was used during the tests. Turk Telekom or Turkcell'te IOT compatible SIM card is produced. If the SIM card is empty or shows the network connection 99 here, there may be a problem on the SIM card or the service provider. Please try the same process again with another SIM card: **AT + COPS?**

You can also inquire about the IMEI number of the device you have purchased through the municipality. **This question applies only to Turkey.** If IMEI is not registered, please contact the company where you purchased the modules.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/56.jpg)

If the module's IMEI number is registered, we need to get an answer as above.

**Important Note: Please inform us if the device will be used abroad.**

After completing the SIM card and USB tests, you can connect to the internet by running the following script.

```sh
sudo chmod +x ./pe2a_miniIOEx.sh
sudo ./pe2a_miniIOEx.sh internet ttyUSB3
```
The **ttyUSB3** address will change according to what you connect to the USB on Raspberry. If ttyUSB is incorrectly selected, the device will not be connect internet. Usually, the default APN for Vodafone is **'internet'**. This depends on the country you are located in and the operator you are servicing. The device can not connect internet on the wrong APN. For Turkcell, the APN may be **"mgbs"**. Detailed information can be reached at: https://www.turkcell.com.tr/kurumsal/kurumsal-cozumler/statik-ip/sikca-sorulan-sorular (only in Turkish)

**Important Note**

**The port number you use as ttyUSB2 in minicom needs to be as ttyUSB3 when running the .sh script.**

Do not forget to close the internet connections after this:

```sh
sudo ifconfig eth0 down
sudo ifconfig wlan0 down
```
After the APN settings, you can connect to the internet with the following command:

```sh
sudo pppd call gprs
```
If you want the program backplane to work, you can add '&' to the command line as follows.

```sh
sudo pppd call gprs&
```

After the **"sudo pppd call gprs"** command, you should see a screen like this:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/57.jpg)

If the device does not connect internet, it will give a "script failed" error. The most common problems are that the APN address of the SIM card is incorrect, the PIN code is insufficient, etc. You can access the IP of the device by executing the following command on the device internete.

```sh
sudo ifconfig
```
If you want to see internet speed, ** speedtest-cli ** program should be installed. Through this program, we can see the speed of the international exit. Below is a sample screenshot of the relevant topic:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/58.jpg)

## GPS Commissioning ##

The MiniIOEx can be used for GPRS-based applications as well as for GPRS connectivity. Location data from GPS satellites and hours from GPS can be used in applications. It is possible to encounter many applications in the related market. Since the antennas used in GPS and GPRS are different, using the same antennas will result in incorrect reception or no data at all.

Be sure to connect to the module MiniIOEx and Raspberry via the **"lsusb"** command. Some of the most common mistakes are misdirecting the USB address path. You can also see this in detail via the **"lsusb-v"** command which USB devices are connected to which USB.

In this section, the data from the GPS data will be examined and the sample code will be shared. You can then perform your actions accordingly. **The GPS antenna needs to be connected to the Quentel UC20 modular GNSS connector.** You need to download and run MiniIOEx-gps.py from GitHub. You can revise the "AT" commands sent in UC20 mode through the program according to the commands you need from the link on the right.

Quectel UC20 GNSS AT Commands Document link:
http://www.quectel.com/UploadImage/Downlad/Quectel_UC20_GNSS_AT_Commands_Manual_V1.1.pdf

The output of the program will be as follows:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/59.jpg)

*GNSS Outputs*

Functions that come after the program has been run: UTC Clock, Date, Coordinate, etc. can be used on Raspberry Pi. As you can see above, the coordinates change often. Therefore, users need to use functions such as optimizing coordinates on the ground for more accurate calculation of coordinate data. It is possible to get a more accurate result on this view. When you do the GOOGLE MAPS data entry in the location coordinate data, the place you are about will appear. UTC clock data also can be used with RTC as Raspberry Pi CPU clock and of course you can write that UTC Clock to EEPROM on MiniIOEx. 

## Real Time Clock and EEPROM  ##

In microprocessors, it is important that the clock is continuous. Since the Raspberry Pi does not have a Real Time Clock, your clock can start at 'fake' one hour or the last one you have when the energy of Raspberry Pi goes out. This leads to time-consuming changes in automation. For example, if you need to start an engine every day at 13:00, you can operate this pump at 18:00 after 5 hours of normal time. For such reasons we have integrated the real time clock into the MiniIOEx-3G. To use the time clock, you can follow the steps below. 

EEPROM and RTC communicate with MiniIOEx-3G via i2C. i2C is a popular communication protocol for receiving and sending data from many devices. It is possible to send / receive data at high speed with only 2 wires. The module that controls I2C devices is called 'master' and the module that is controlled is called 'slave'. Each i2c slave device has a unique address. Each i2C device communicates over the same serial clock (SCL) and serial data (SDA). The i2c protocol includes the states **START** and **STOP** to inform the master device whether the data starts or ends.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/60.jpg)

In the picture below, you can find the BIT chart of SCL and SDA. SCL is a clock, consecutive reference signals; SDA produced the data of the slave device.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/61.jpg)

In the terminal **raspi-config-> Interface Options-> i2c-> Enable** then it is recommended to start Raspberry Pi reboot. To access the I2C devices, you can run terminal command that **i2cdetect -y 1**. For older Raspberry Pi version, it shall be **i2cdetect -y 0**

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/62.jpg)

The ** EEPROM ** on MiniIOEx **(24LC512)** unique address is **0x50**. We also need to use this unique address in the software. If RTC data is written to EEPROM and Raspberry Pi is restarted, RTC data can be read from EEPROM, or some 'secret' passwords can be written to EEPROM. 

Below is a sample program written in *.c*. In this code, clock data from RTC is printed on EEPROM and this data is read through EEPROM.

```c
#include <stdio.h>
#include <sys/ioctl.h> // ioctl
#include <fcntl.h>     // open
#include <unistd.h>    // read/write usleep
#include <time.h>
#include <netinet/in.h> // htons
#include <linux/i2c-dev.h>

#pragma pack(1)

#define PAGESIZE 32
#define NPAGES  128
#define NBYTES (NPAGES*PAGESIZE)

#define ADDRESS 0x50  //  24LC512's address on I2C bus 

typedef struct {
    ushort AW;
    char  buf[PAGESIZE+2];
}WRITE;

static WRITE AT = {0};

int main() {
  int fd;
  char bufIN[180] = {0};
  time_t clock=time(NULL);

  snprintf(AT.buf, PAGESIZE+1, "%s: my first attempt to write", ctime(&clock)); //  the buffer to write, cut to 32 bytes

  if ((fd = open("/dev/i2c-1", O_RDWR)) < 0) {  printf("Couldn't open device! %d\n", fd); return 1; }

  if (ioctl(fd, I2C_SLAVE, ADDRESS) < 0)     { printf("Couldn't find device on address!\n"); return 1; }

  AT.AW = htons(32);    //  I will write to start from byte 0 of page 1 ( 32nd byte of eeprom )

  if (write(fd, &AT, PAGESIZE+2) != (PAGESIZE+2)) { perror("Write error !");    return 1; }
  while (1) { char ap[4];  if (read(fd,&ap,1) != 1) usleep(500); else break; } //   wait on write's end 

  if (write(fd, &AT, 2) != 2) {  perror("Error in sending the reading address");    return 1;  }

  if (read(fd,bufIN,PAGESIZE) != PAGESIZE) { perror("reading error\n"); return 1;}
  printf ("\n%s\n", bufIN);

  close(fd);
  return 0;
}


```
![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/63.jpg)

*You can test real time clock with hwclock -r command*

## Application Notes ##

You can review applications made on MiniIOEx-3G in this section.

### Sample #1 – FAN Motor Control with Start/Stop Button on MiniIOEx-3G ###

Below is a nice example that we can create using 2 Digital Inputs and 1 Digital Output. 'FAN' is operated by receiving data from *'Start'* and *'Stop'* buttons. In fact, this FAN could be even a big fan or elevator engine in real life. As in the picture below, a small fan is preferred in this application and this fan output is connected to the transistor output output.

The equipments required in this application:

-	1ch 24VDC FAN [24VDC 80mA]
-	1ch Start Butonu - Normally Open (NO)
-	1ch Stop Butonu – Normally Close (NC)
-	24VDC 30W Power Supply [Phoenix UNO Power Supply is preferred]
-	Raspberry Pi 3 
-	Class 10 16GB SD Card 

The libraries required in this application:

-	Python GPIO
-	Python SpiDev

**Automation Scenario**:
*FAN motor works when Start button is pressed for 1 second; If you press the 1sec Stop button, the FAN Motor will stop.*

Although the scenario seems very simple, we will be working together with Raspberry Pi to learn many of the applications we have learned before. At first, we will code the script with Python, we will carry it into WEB and we will design a FAN engine web site which can be accessed from anywhere by adding some Javascript. 

If the scenario is going to be a chart, we can get the following chart. We also need to program according to this chart:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/300.jpg)

As you can see in the graphic above, when the Start button or the Stop button is pressed for 1 second, the value of the FAN motor must change to the rising or falling edge. The 1 second duration actually provides 'digital filter'. That means that the Xms energized Start button allows for the FAN motor to move because of any interference. Such filters are important for the software application to work with the hardware.

The following terminal numbers are used in connection:

| Terminal Number | Comments |
| --- | --- |
| 18 |	Digital Input - 1 | 
| 16 |	Digital Input - 2 |
| 10 | 	Transistor Output 1 |

*The any relay of the MiniIOEx-3G is not used in this application. The reason for this is that the load to be switched requires high current.*

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/30.jpg)
*Fan Motor Working Process- 1*

We can do the wiring as above. **FAN GND**is shorted to power supply GND. The voltage is given by switching from the transistor by software. In the following illustration, the cable ends are shared:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/31.jpg)
*Fan Motor Terminal Cable Commissioning*


```python
import RPi.GPIO as GPIO
import time

#definition GPIO
RASP_DIG_IN_1 = 6 #START BUTTON
RASP_DIG_IN_2 = 13  #STOP BUTTON
RASP_DIG_tr_OUT_1 = 21 #TRANSISTOR Output 

#init function
GPIO.setmode(GPIO.BCM) #bcm library
#for digital inputs
GPIO.setup(RASP_DIG_IN_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RASP_DIG_IN_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RASP_DIG_tr_OUT_1,GPIO.OUT)
GPIO.setwarnings(False)

while 1:
    DI_In1 = not GPIO.input(RASP_DIG_IN_1)
    DI_In2 = not GPIO.input(RASP_DIG_IN_2)
    
    if  DI_In1:
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.HIGH)

    if not DI_In2:
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.LOW)
    
    time.sleep(1) #for holding time   

```
We can examine the code at below.

```python
    DI_In1 = not GPIO.input(RASP_DIG_IN_1)
    DI_In2 = not GPIO.input(RASP_DIG_IN_2)
```

This code aims that our intended Digital Inputs are **PULL_UP** so that Raspberry arrives *1*  even if the buttons are not pressed at the moment of opening. We are returning the inputs here to the physical value by adding **not**.

```python
if  DI_In1:
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.HIGH)

if not DI_In2:
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.LOW)
```

In this structure, the **Start** button is pressed and the FAN motor starts to work. The only requirement to interrupt this work is to press the **Stop** button for 1 second. The **Stop** button is Normally Close (NC), so its value always will be **1** if the stop button is not pressed. When the **Stop** button is pressed, the value will be **0**.



### Sample #2 – Controlling of FAN Motor with Start/Stop and WEB Reference ###

In this application, WEB reference will be used with Start/Stop button. Firebase is the key of WEB controlling. the following libraries must be installed:

-	PYTHON GPIO
-	PYTHON Firebase-pyrebase

**Automation Scenario:**

If **Start button** is pressed for 1 second or **WEB Start button** is activated, FAN motor will work.
If the **Stop button** is pressed OR the **WEB STOP button** is activated, the FAN Motor is stopped.

We create a database name on Firebase called **WEBSample** and their child is **StartButton** and **StopButton**. Since these values come from WEB, we have to adjust our program accordingly it.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/33.jpg)
*Firebase WEB Reference Values*

Since the **StopButton Reference** on the WEB does not have a feature like Normally Closed, we can get it as a normal variable. Since the variables stored in the Firebase are strings, we need to act accordingly. You can also use it directly as a string, or you can convert it to *integer*. Web Reference  or physical button value is necessary for the operation of the FAN motor.

```python
if (DI_In1 or myConnect.WEB_REF_1 == '1'):
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.HIGH)
        print("web ref_1")
#stop comes from firebase DB
if (not DI_In2 or myConnect.WEB_REF_2 == '1'):
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.LOW)
```
Our software is currently working on values coming from WEB and values coming from physical.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/34.jpg)
*Firebase WEB Referance Values*

When you change the **StarButton** value from the **Firebase** console screen, you can see that the FAN engine starts to rotate. Of course this can be changed and assigned according to the user. Our program will now start to work through a WEB database. This will now allow us to reach Raspberry Pi from a world outside. As an example, you can access Raspberry Pi via mobile application or WEB application when required services are written in this database. Accessing Raspberry Pi via a server can also result in security weakness. As a result, you need to configure security for your server against security adjustments and possible attacks. In the case of services such as Firebase, you are unlikely to encounter such a problem.

Below is the application you can control the FAN engine via Firebase. Here are some parameters that will be available via Firebase. Once you log in to Firebase, you can easily retrieve this information from the main page. You need to use these parameters in applications you write.

Here's what these parameters are:

```python
myFirebaseConfig = {
              "apiKey": "",
              "authDomain": "",
              "databaseURL": "",
              "projectId": "",
              "storageBucket": "",
              "messagingSenderId": "",
        }
```
You can find out that'a all the program at below:

```python
import RPi.GPIO as GPIO
import time
import spidev
import pyrebase

RASP_DIG_IN_1 = 6 #START BUTTON
RASP_DIG_IN_2 = 13  #STOP BUTTON
RASP_DIG_tr_OUT_1 = 21 #RPI PIN: 40

#init function
GPIO.setmode(GPIO.BCM) #bcm library
#for digital inputs
GPIO.setup(RASP_DIG_IN_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RASP_DIG_IN_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#transistor output definition
GPIO.setup(RASP_DIG_tr_OUT_1,GPIO.OUT)
GPIO.setwarnings(False)

#firebase connection 
class connectCloudPolly():
    
    def __init__(self,myConfig):
        
        self.myCloudConfig = myConfig
        self.cloud = pyrebase.initialize_app(self.myCloudConfig)
        self.db = self.cloud.database()
       
       
    
    def ReadButtonInf(self):
        self.WEB_REF_1 = self.db.child("/WEBSample/StartButton/").get().val()
        self.WEB_REF_2 = self.db.child("/WEBSample/StopButton/").get().val()
        
        print(bWEB_REF_1,bWEB_REF_2)
        
#firebase connection struct 
#you can easily get the values from firebase console
myFirebaseConfig = {
              "apiKey": "",
              "authDomain": "",
              "databaseURL": "",
              "projectId": "",
              "storageBucket": "",
              "messagingSenderId": "",
        }
#firebase connection
myConnect = connectCloudPolly(myFirebaseConfig)

while 1:
    DI_In1 = not GPIO.input(RASP_DIG_IN_1)
    DI_In2 = not GPIO.input(RASP_DIG_IN_2)
    
    myConnect.ReadButtonInf()
                #start comes from firebase DB
    if (DI_In1 or myConnect.WEB_REF_1 == '1'):
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.HIGH)
        print("web ref_1")
                    #stop comes from firebase DB
    if (not DI_In2 or myConnect.WEB_REF_2 == '1'):
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.LOW)
    
    time.sleep(1) #for holding time

```

### Sample #3 – Reading values from Energy Analyser via RS485 ###

Thanks to RS485, we can connect and read/write data from many devices. With Raspberry Pi and MiniIOEx, this data can be sent via 3G or Ethernet / Wireless, thanks to which data can be transferred using IOs or stored in high resolution. Although this kind of process seems easy, the PLC or embedded PCs cost quite a lot for this basic process.

Used devices for this part:

- Raspberry Pi 3
- MiniIOEx
- Entes MPBR63 ENergy Analyzer
- Additional computer to monitor read/write data

Below is the topology we use in the system. There is also a computer outside the topology. The purpose of our computer use is to show how we receive this data because we have exchanged data with the MODBUS RTU protocol over the RS485 physical serial path. In other words, when we receive data from the energy analyzer, we actually receive this data with which questions we can easily see it on an external computer.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/entes-computer-mini.png)
*RS485 Device Connection Topology*
 
In the above system, the computer behaves as master / slave, the MiniIOEx is master and the analyzer is slave. *A* and *B* terminals of MiniIOEx RS485 are all short-circuited in the system. **"Modbus Master**" that Computer Serial Port Program and **"Terminal v1.9b**" programs installed on the computer, we can see the reference codes you need to go to read data from the Entes Analyzer. Of course, before we do this, we need to know which registers the analyzer has which information. We can also extract this from the **"Data Mapping"** document found on the analyzer web page of the Entes Analyzer.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/46.jpg)
*Register Table of the Energy Analyzer*

As you can see on the tablade there is *cosq* values *19,20,21* in the register. (It appears that the first value starts from 0 in the Register table.) Since the resolution for cosq value is 1000, it must be divided by 1000 so that the value coming from real cosq value. For example, when the value of 999 is reached, this value should be cosq = 999/1000 = 0.99. Since no current / voltage terminals are connected to the energy analyzer, there is no phase difference between them and therefore we need to see cosq = 1. Other information (voltage, current, etc.) can also be taken using this tissue when a field application is made.

When we connect the analyzer to the terminals of the computer and MiniIOEx terminal, we can proceed to read data.

| MiniIOEx Terminal Number  | MPBR63 Analyzer Terminal Number | 
| --- | --- |
| RS485-B, 19	| RS485-B, 15 |
| RS485-A, 20	| RS485-A, 14 |

First we need to write basic information such as node slave address, how many registers we want to read in the **MODBUS MASTER** program installed on the computer. The following screen shot also provides sample information:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/47.jpg)
*Query and Answer as HEX format*

The computer sends the query: **01 03 00 00 1E C5 C2**. According to this query, the Analyzer gave a long answer. Rx, the query sent by the computer; Tx is the answer from the analyzer. Data can not be retrieved without inquiry on RS485. These long answers are actually parameters such as Voltage / Current / Frequency / Power factor measured by the Analyzer. In order to use Cosq from these parameters, let us first examine the question sent by the Analyzer. The analyzer sent us the **03 E8** replies in sequence. This answer is actually **HEX 0x3E8**. In the decimal number system, it is expressed as "1000". In other words, the result of the query we made is 1000/1000 = 1 in the cosq register. If the value of 999 (0x3E7) came, it would be 999/1000 = 0.99. These operations are the most basic events that take place in the RS485 serial path. We make these operations simple by using protocols. If we want to make a computer-like query from Raspberry Pi, we can use the following code. 

The following code appears to have the **"python serial"** library. You can run this library by typing the following command at the terminal.

```sh
$sudo apt-get install python-serial
```
After uploading the library, we can send the related query by running the following program.

```python
import os,time
import serial
      
ser = serial.Serial(
              
    port='/dev/ttyS0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
            )

ser.write(serial.to_bytes([0x01,0x03,0x00,0x00,0x00,0x1E,0xC5,0xC2]))

```
In order to receive the data from the analyzer, we have mentioned above that we need to send the relevant parameter to the analyzer:**01 03 00 00 1E C5 C2** When we send this parameter through the serial port to the analyzer, it returns us the parameters in HEX again. We can see that the values again on **"Terminal v1.9b"** computer program.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/48.jpg)
*RS485 Query and Answer*

In the picture above, the query **(01 03 00 00 1E C5 C2)** to the Analyzer and the query from the analyzer and the answers from the analyzer according to this query. In this question, it is not really complicated. As an example, *"01"* defines Node address; *"1E"* shows how many registers are defined. The first query in the RS485 protocol then takes place in his reply. Both Write and Read via RS485 serial port at the same time can not be querried synchronously. This causes the fault.

When we run this basic code, the Analyzer will give a result like above. When we write this code with ModbusRTU protocol, understanding of parameters, Check-Sum calculations, CRC calculations are more comfortable.

There are many open source **ModbusRTU** libraries running on Raspberry. There are many documents related to this subject on the internet. **ModbusRTU** is a protocol that you can create if you wish but you do not need to "reinvent the wheel" here, which is also true in most areas like software. In this document **"PYMODBUS"** library is used. You can download the **PYMODBUS** library by entering the command at the following terminal.

```sh
$sudo pip install  -U pymodbus
```

When the **"PYMODBUS"** library is installed, we can use the ModbusRTU protocol to get the parameters received from the Analyzer from the field. The analyzer used in this example has no voltage or current source connected. Therefore, we can only query "cosq" data. Having the "cosq" data means that other data can be easily accessed. In order to receive other information, it is only necessary to know the correct "register" addresses.

```python
import serial
import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer
import time

client = ModbusClient(method = 'rtu', port = '/dev/ttyS0',baudrate = 9600,timeout = 1, parity = 'N')
client.connect()

while 1:

    try:
        result = client.read_holding_registers(0x00,40,unit = 0x01)
        #print(result.registers)
        print("cosqL1 : {}, cosqL2 : {}, cosqL3 : {}".format(result.registers[19]/1000.0,result.registers[20]/1000.0,result.registers[21]/1000.0))
    except:
        pass
    time.sleep(1)

```
Usage of *read_holding_registers* in python program:

```python
result = client.read_holding_registers(0x00,40,unit = 0x01)
```

In the above software example, the registers between 0 and 40 registers on the analyzer are being queried. The register table has been given above and we have seen that there are many parameters between these registers. Since the analyzer is the communication node "1", we add "0x01" or only "1" ID query parameter to the parameter of **"client.read_holding_registers"**. That is, the analyzer with unit ID:1 actually wants to send the parameters between 0. and 40. Registers. These parameters include  voltage, current, cosq, energy. If there is no analyzer with this ID number, the system will wait in *timeout*.

The output of the code is the value of the cosq values in the Active Power. If information such as voltage / current is to be received, inquiry should be made from the relevant Register table. We can also calculate COSQ through other informations from the Analyzer.

Basic Cosq calculation:

-	P = VIcosq  == cosq=P/VI
 
-	Sample#1 P = 3.4kW, V=400V, I=10A

-	Cosq = 3400W / (400Vx10A)

-	Cosq = 0.85

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/49.jpg)

Here we can calculate *CosQ* as *0.85*. In general, we always want CosQ to be close to 1. Since we can get the values angle of Voltage, Current, Active Power etc. from the analyzer, we can calculate cosq and accordingly angle calculations. If the system of cosq is not below 0.98, fines shall be paid.

You can also see the energy consumed and the energy generated from the analyzer. If you have a solar power plant, you can also get Spent and Generated Energy information and record it on a daily / weekly / monthly basis and send your data to your server without any internet service provider by using 3G module on MiniIOEx-3G. When there is energy production, the sign of the current will change. It should be noted.


### Sample #4 – AC Motor Control by using  AC Motor Driver with MiniIOEx RS485  ###

We have seen in the previous chapter that we can easily read data from the Energy Analyzer with MiniIOEx. Because MiniIOEx-3G is an industrial development card, it is designed for use in industrial environments. When it comes to industrial environments, mind motor control and applications come first. In this application, we will try to drive the motor by giving reference values via RS485 to the motor driver. RS485 will be used again in this study. Therefore, we assume that the following libraries are installed:

- **serial**
- **pymodbus**

If you have loaded these libraries, you can load them by looking at the previous example. **"Raspi-config"** should check that the serial port settings are open. Our goal here is to give the speed reference to the motor driver and to control this speed through Raspberry. The following equipment was used in this study:be

-	ABB ACH550 3P 400V 7.5kW Motor Driver
-	Siemens 2kW 3P 400V 1500rpm AC Motor 
-	Raspberry Pi 3 B+
-	MiniIOEx-3G 
-	Phoenix Contact UNO Power 230V/24V Power Supply

**IMPORTANT NOTE**

**Perform motor and driver connections with an experienced electrician. It should not be forgotten that there is a danger of death at 400V**

After setting the motor parameters of the ABB Driver, we need to enter the "Communication Parameter" settings. The corresponding parameter setting is available in the driver's manual. After setting the parameters, we are installing the RS485 terminals of the MiniIOEx in the ABB Motor Drive.

We create a file called **"abb.py"** on the terminal screen and we need to grant all rights to use serial port and IO operations in this file. If we write in the terminal we can give these rights by *"chmod + x abb.py"* command. If the driver's motor connections and communication connections are completed, we can switch to the corresponding software. When we read the manual page of our driver, we are registering the relevant registers and we need to check what information they contain. Although the drive consumes a lot of information from the consumed energy to the saved energy etc., we will only use the following parameters in our software:

-	Motor Speed[rpm]
-	Motor Current[A]
-	Motor Power[kW]
-	Driver DC Bus Voltage[V]
-	Driver Temperature [Celcius]

We can retrieve these values by querying the relevant registers. We only used the Motor Speed variable in our sample software. Other information can also be taken from the code. The Motor Temperature parameter is important for this information. In general, motor drivers can only operate for a certain time at a certain temperature. This value should be continuously checked for unintentional stops and if the temperature is too high (operating temperature is usually 40 °C max), the driver can be taken care of or the environmental conditions can be changed.

We read data via RS485 with the energy analyzer, but we did not write any data on the analyzer. In this example, there is also how to write data via Modbus.

```python
client = ModbusClient(method = 'rtu', port = '/dev/ttyS0',baudrate = 9600,timeout = 1, parity = 'N')
client.connect()

try:
    result = client.read_holding_registers(100,20,unit = 0x01)
    print("Motor Speed : {}".format(result.registers[2]))
```

We were questioning the '0' register while reading the data on the analyzer, but since the ACH550 driver told us that we could read from the 100th Register, we made 20 register's from the 100th register. The return value of the function ".read_holding_registers" contains all the variables mentioned above in the 'result' array. In the 100.register, because of the Speed ​​Variable, the result [0] will give us the instant speed variable in subsequent queries.

After the first interrogation, the program decides whether to start the engine by looking at the variables. Since we have a simple example here, we have not checked these variables. For example, the motor start temperature, DC bara voltage can be controlled, and if these values are not within the desired range, the motor should not start.

General flow diagram of the program:

- Read motor and drive parameters
- "Driver start" refer to the first conditions
- "Driver start"
- Driver motor speed reference sending as [Hz] type
- Increase motor speed reference
- Pull motor speed reference to 0 Hz
- Bring the drive to the stop state

In the first step we read the motor and drive parameters. Now we have to start the drive. 

In the analyzer we mentioned that we were just reading and writing here. We can perform the typing operation using the following function:

```python
result = client.write_registers(REGISTER_ADRESS,REGISTER_REF,unit = UNITID)
```

With this function, we can perform the desired write operation. First we need to perform the driver start operation in register *0* and not send the motor speed reference still. We can do all of this with the **"write_registers"** function.

Driver Start Bit Reference Values Initial Status:

| ACH550 Motor Driver Register Value[0]	| Bit Value |
| --- | --- |
| [0].1	| True |
| [0].2	| True |
| [0].3	| True |
| [0].4	| True |
| [0].5	| True |
| [0].6	| True |
| [0].7	| True |
| [0].10 | True |
| [0].0	| **False (Start Bit)** |

First of all references to the table should be sent. Since we send references as DECIMAL, the value of DECIMAL in this table is 1278.

```python
result = client.write_registers(0,1278,unit = 1)
```
After that, we will make the Start bit True, making the motor driver work.

Driver Start Bit Reference Values Second Condition:

| ACH550 Motor Driver Register Value[0]	| Bit Value|
| --- | --- |
| [0].1	| True |
| [0].2	| True |
| [0].3	| True |
| [0].4	| True |
| [0].5	| True |
| [0].6	| True |
| [0].7	| True |
| [0].10 | True |
| [0].0	| **True (Start Bit)** |

**[0] .0** Since the value of the start bit changes, the reference value we send to the register will increase. 

```python
result = client.write_registers(0,1279,unit = 1)
```

After this reference value, the motor drive will be ready for external reference. First we do not want to make all bits true. Therefore we gradually activated the motor drive. Now let's send the motor speed reference again using the **"write_registers"** function.

```python
result = client.write_registers(1,speedRef,unit = 1)
```
The ABB Motor document Indicates that there is a **"Speed Reference"** register in the driver's No. 1 register. We can increase the **"speedRef"** variable to speed up the motor. We specified that the speed reference parameter of the AC Motor drive is "Hz".

| Referance Value(Decimal) | Hz Response |
| --- | --- |
| 0	| 0 Hz |
| 10000	| 25Hz |
| 20000	| 50Hz |

Increases **speedRef** by 10,000 in each cycle to speed up the engine.

```python
myCounter = 5
speedRef = 0
    while myCounter:
        
        result = client.write_registers(1,speedRef,unit = 1)
        time.sleep(1)
        result = client.read_holding_registers(100,20,unit = 0x01)
        print("Motor Speed : {} ".format(result.registers[0]))
        myCounter = myCounter - 1 
        speedRef = speedRef + 10000
        time.sleep(10)
```
When we run the program, we get the speed values as follows:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/50.jpg)

*ABB Driver Speed Reference*


![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/51.jpg)

*Driver User Panel at full speed*

As seen in the above screen display, the motor speed is gradually increased in rpm and then gradually decreased. Due to the slip of the AC motor, the maximum speed rises to 1476 rpm not 1500.  The motor was rotated and stopped in the *FORWARD* direction by the ABB driver. It is possible to do all of these easily by using **PYTHON** language. Very good graphics can be developed by developing the program, the data can be sent to the WEB or the program can be run from the WEB in various situations. 


Below you will find the code needed to control the ABB ACH550 Motor drive.

**abb.py**

```python
import serial
import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer
import time

client = ModbusClient(method = 'rtu', port = '/dev/ttyS0',baudrate = 9600,timeout = 1, parity = 'N')
client.connect()

try:
    result = client.read_holding_registers(100,20,unit = 0x01)
    print("Motor Speed : {}".format(result.registers[2]))
    time.sleep(1)
    #start bit  0       
    result = client.write_registers(0,1278,unit = 1)
    time.sleep(1)
    #start bit  1
    result = client.write_registers(0,1279,unit = 1)
    time.sleep(1) 
    #after start operation 
    print("operation starts:")
    myCounter = 5
    speedRef = 0
    while myCounter:
        
        result = client.write_registers(1,speedRef,unit = 1)
        time.sleep(1)
        result = client.read_holding_registers(100,20,unit = 0x01)
        print("Motor Speed : {} ".format(result.registers[0]))
        myCounter = myCounter - 1 
        speedRef = speedRef + 10000
        time.sleep(10)
    #Stop Operation
    #speed ref will be 0 rpm
    time.sleep(5)
    result = client.write_registers(1,0,unit = 1)
    time.sleep(20)
    result = client.read_holding_registers(100,20,unit = 0x01)
    print("Motor Speed : {}".format(result.registers[0]))
    #driver start bit will be 0 and driver will stop
    result = client.write_registers(0,0,unit = 1)
    result = client.read_holding_registers(100,20,unit = 0x01)
    print("Motor Speed : {}".format(result.registers[0]))

except:
    pass
    
time.sleep(1)
client.close()

```

Modbus communication can be turned off by the *".close ()"* function.

```python
client.close()
```

### Sample #5 - Reading Values from Siemens CO2 Sensor ###

In this study, data values from the "Siemens QPA2002" CO2 / Air quality sensor will be processed. The processes described will then be compared to a real system.

• Sensor and MiniIOEX supply 24V during the test. The necessary cabling is also made accordingly.
• Sensor, 0-10V model with voltage output (U1) is preferred.

Siemens QPA2002 Sensor information:

*Min. CO2*  = (0) ppm
*Max. CO2* = 2000 ppm  

-	3 No’lu Pin : G
-	4 No’lu Pin : G0
-	5 No’lu Pin:  U1

The U1 pin output is the sensor voltage output. We can formalize the output voltage of the sensor as follows:

Output  = (Input-0V) * ((CO2 ppm max.  - CO2ppm min.)/(10V-0V )) + CO2 ppm Min. 

Output  = (Input) * ((2000ppm - 0ppm)/(10V-0V )) + 0ppm

Depending on the above equation we can also perform the function of the CO2 sensor as follows:

```python
def co2_sensor_converter(val):
    return val * 200.0
```

After the function related to the sensor data is written, we can execute the entire code as given in the above examples. 

**Note:**
It is recommended to not exceed 1000ppm for indoor air quality to be good. As you type, the program can create hysteresis curves for these values and control the ventilation fan *ON/OFF* accordingly.

Below is a sample code block written about this sensor. CO2 sensor is installed to MiniIOEx J2: 12 and their GNDs shorted together. If you blow into the air quality sensor, you can see that the 'ppm' data generated by the sensor due to the CO2 in your breath changes. This value will increase after blowing.

```python
import spidev
import time

#definition SPI parameter
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 7629
#definition Analog Input Var. 
AI_ANIN2 = 0 #J2, pin:12 and always GND is common with sensor
#definition co2 sensor data
co2SensorData = 0
#mcp3208 ADC
def readAI(ch):
        if 7 <= ch <= 0:
            raise Exception('MCP3208 channel must be 0-7: ' + str(ch))

        cmd = 128  # 1000 0000
        cmd += 64  # 1100 0000
        cmd += ((ch & 0x07) << 3)
        ret = spi.xfer2([cmd, 0x0, 0x0])

        # get the 12b out of the return
        val = (ret[0] & 0x01) << 11  
        val |= ret[1] << 3           
        val |= ret[2] >> 5           

        return (val & 0x0FFF)  

#converts digital number to voltage
def dig_vol_converter(val):
    return val*33.0/4095.0

#0 ppm -> 0V 2000ppm -> 10V
#Siemens QPA2002
#assume val is co2sensor voltage output : (val-0V) *[(2000ppm-0ppm / 10V-0V) + 0V]
def co2_sensor_converter(val):
    return val * 200
    
print('-' * 55)
# Main program loop.
while True:
    print('\n')
    print('{} | {} '.format('Sensor Voltage[V]','Sensor Data[ppm]'))
   
    # The read_adc function
    AI_ANIN2 = dig_vol_converter(readAI(1)) #Voltage
    #lets convert co2 value
    co2SensorData = round(co2_sensor_converter(AI_ANIN2),1) #ppm
    
    print('{:6f}  {:21f} '.format(AI_ANIN2,co2SensorData))
    time.sleep(1)
```

**Note**

All of the examples so far have been related to the linearity condition of sensors, but some sensors may not be linear. That is, voltage and sensor value may not be linearly proportional. In such cases, we can linearize the values by recording the sensor values. Once you have registered the values, we can calculate it at http://www.wolframalpha.com/.

With an example, we can explain this situation more clearly. Sample values are taken from the book [Exploring Raspberry Pi, M. Derek, 2016](https://www.amazon.com/Exploring-Raspberry-Pi-Interfacing-Embedded/dp/1119188687)

Suppose that 3925 digital corresponds to 10cm, 2790 digital corresponds to 15cm. There is no linear decrease in the values here. We can not use a nonlinear equation on Raspebrry. Therefore, various theorems have been produced to approximate this value to linearization. (Marquardt-Levenberg) The Wolfram program will automatically linearize this value. All we need to do is write the following set of equations to the Wolfram program:

*exponential fit {3925,10}, {2790,15}, {2200,20}, {1755,25}, {1528,30},{1273,40}, {851,50}, {726,60}, {620,70}, {528,80}*

As a result of this program, we can obtain the following graph and equation.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/39.jpg)

If you have a sensor set of such a nonlinear output you can benefit from this theory.

### Sample #6 - Danfoss FC51 Motor Driver Control via Modbus RTU ###

We can transfer data from RS485 directly to our own server or cloud server via Wireless or Ethernet using Python with Raspberry Pi.

Using industrial communication protocols such as Modbus via Raspberry Pi brought with it a painful process. After a while, USB / RS485 converter has caused many problems in the field. There are also many users who want to use only the Raspberry Pi as a gateway. With the help of Raspberry Pi, we can transfer data from RS485 directly to our own server or cloud server via Wireless or Ethernet using C / C ++ / Python languages. However, we can handle these values and transfer them directly to the database we created on Raspberry Pi. The advantages of running the Linux operating system over Raspberry Pi is absolutely free. If you are coming from Industrial Automation side, licence price would be very annoying stuff.

In this case, we tried to show how to activate the Danfoss FC51 series motor drivers with Raspberry Pi and MiniIOEx. You can use the attached code as desired. We shared the video. So we tried to explain how the program works.

After installing the operating system on Raspberry Pi, we recommend that you should use the operating system in the most up-to-date. We need to skip the basic operations in this section.

We used Jessie as the operating system. In the project, the following libraries must be installed by the user:

```python
serial
pymodbus
```
You can install these libraries by following these commands:

```python
$pip3 install pyserial
$pip3 install pymodbus
```

After installing the program you can perform the installation of the MiniIOEx cable. The following cables may be connected to the terminals given below:


| MiniIOEx Terminal No| cable Name | Field Equivalent |
| --- | --- | --- |
| 1	| GND | POWER SUPPLY GND |
| 2	| 24VDC | POWER SUPPLY 24VDC |
| 16	| DI_2 | STOP BUTTON |
| 17	| SERIAL_GND | NO NEED |
| 18	| DI_1 | START BUTTON |
| 19	| RS485_B | DANFOSS ON TERMINAL NO:69 |
| 20	| RS485_A | DANFOSS ON TERMINAL NO:68 |

### Commissioning ###

In fact, our scenario consists of a very simple function. *When we press the start button, our speed increases by 100rpm and remains constant at that speed. When we press the stop button, motor speed goes to 0rpm.* Also, we can read driver information data from Danfoss DC51 Driver as using pymodbus.

we send the following speed reference to driver as using this function:


```python
 #sending motor speed  
 def sendMotorReference(motorSpeed_rpm):  
     return (int(motorSpeed_rpm*(21.845/2.0)))  
```

From the driver we can get the following information:

```python
 #motor parameter  
motorConstantParameter = {  
     "wrMotorSpeedRPM" : 0, #converted  data   
     "r_motorDCLinkV" : 0,  
     "r_motorPowerkW" : 0,  
     "r_motorCurrentA" : 0,  
     }    
```

Driver Modbus Register List:

```python
motorModbusParameter = {
	    
	    "motorID " : 0x1,
	    "w_motorSpeedReq" : 2810,
	    "r_motorDCLinkVReq" : 16299,
	    "r_motorPowerkWReq" : 16099,
	    "r_motorSpeedFreqReq": 16129,
	    "r_motorCurrentAReq" : 16139,
	    #"r_motorFreqPerReq" : 16149
	    
	    }
```
**Note: Start permission will be given at 1. Register Adress. 

Incoming speed is converted to RPM with the following function:

     
```python
 #calculation percent of requency of motor  
 def calculationPercentFreq(motorSpeedNumber):  
     return  (motorSpeedNumber / 32767.0*100.0)  
```
When the program is running, you can see that it is always flashing for RunLed on MiniIOEx. We provide this with the following function:

 
```python
#it  means a program running on OS    
def fLed():       
while 1:            
    GPIO.output(DO_RunLed,GPIO.HIGH) #ON            
    time.sleep(0.2) #200ms            
    GPIO.output(DO_RunLed,GPIO.LOW) #OFF            
    time.sleep(0.2) #200ms 
```

I also share the following code in github: https://github.com/pe2a/miniIOEx3G/blob/master/fc51.py

For Video: 
Check this out:

https://vimeo.com/304813868

#### Conclusion ####

After installing the relevant libraries and making the cable installation connections, you can run the program. Do not hesitate to contact support@pe2a.com if something is wrong. ;)

In the next article, we will try to prepare a document such as visualization of the relevant motor values on the GUI and transfer of the data to the cloud.

### Sample #7 - Reading Battery Voltage and Monitoring ###

Raspberry Pi can also be used in places without electricity. For example, water pumping stations or in areas such as animal monitoring and so Raspberry Pi work with battery. If the the values/data/image etc. are critical; it must be monitored continuously, it is important to keep the system alive. The way to do this is to monitor the battery voltage. If you can monitor the battery voltage, when the battery will run out, you can replace the battery with a spare battery. With the industrial Raspberry Shield named MiniIOEx, you can easily monitor the battery and Raspberry Pi supply voltage. An external cable connection is not required. The 12Bit Analog Input sensor on the MiniIOEx is also connected to the 24V and 5V line. The power block on the MiniIOEx converts the voltage from 5V to 30V to 5V. Therefore, you can also supply the MiniIOEx with 12V battery voltage instead of 24V.

#### Physical Interface ####

- 12V 7Ah Rechargeable Battery
- Industrial MiniIOEx
- Raspberry Pi 3 B+
- 16GB SD Card Class 10

#### External Library  ####

- matplotlib

You can easily install matplotlib by using at below command:

```python
pip install –U matplotlib
```
In addition, SPI must be enabled because we will use the python with the SPI-based comm. You can review the comments in the attached link. [https://github.com/pe2a/miniıoex3g/blob/master/readme.md#analog-input]

You can install the battery terminal to MiniIOEx terminal as shown at below:

| MiniIOEx Terminal No| Battery Terminal |
| --- | --- | 
| 1	| - | 
| 2	| + | 

The Matplotlib library is a program that draws highly useful graphics on Raspberry Pi and is very easy to use. Since we have installed the related library and made SPI settings, we need to run the following code: https://github.com/pe2a/miniIOEx3G/blob/master/batteryVoltage.py


![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/PowerSupply1min.png)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/PowerSupply10min.png)

How we measure battery voltage with MiniIOEx:
![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/BatteryTest.jpg)

#### Conclusion ####

After the run code, we can get 1min or 10min graphics of battery voltage. Raspberry Pi has Operating System and this system works unbalanced as considering current demand. So, you can see that unbalanced load in figures.   

#### References ####

https://matplotlib.org/

## Other Topic ##

### Installing Raspbian OS ###

Raspberry Pi runs the operating system on the SD card on it. Therefore, it is necessary to have a *"Disk Image"* program to load a high-quality and fast SD card (class 10 is recommended) and the operating system to be loaded in the correct format.
You can do this with "Win32 Disk Imager" on Windows by following the steps below:
Win32 Disk Imager Program: https://sourceforge.net/projects/win32diskimager/

If you are using GPIOs intensively, it is important to set up a Raspbian based operating system. Other operating systems do not have a stable working structure on Raspberry. The Raspberry Foundation updates its operating system during certain periods of the year. The latest Raspbian operating system is available on the link below.

Raspberry ISO Link: https://www.raspberrypi.org/downloads/raspbian/

There are two ISO formats Raspbian OS on the related link. "Raspbian Lite" only opens the terminal screen. It does not host any GUI. So if your program uses GPIO and this data is sent to a server as an example, you can download 'Lite' version without using any GUI process. In this way, the operating system will get rid of many programs that you do not use. If you are developing applications on Raspbian, if you also want to use programs like Office, 'with Desktop' will be the best choice.

After downloading the desired operating system, you can start the following operations by opening your 'Disk Imager' program and placing the SD card in your computer to format the SD card.

1)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/RPI1OS.jpg)

2)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/RPI2OS.jpg)

3)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/RPI3OS.jpg)

### How to find your MAC ID of your Raspberry Pi ###

If you are using the Raspberry Pi in an industrial area, you may need to register your computer's MAC ID for your IT department. Therefore, you need to know the MAC ID of your computer. As you know, Raspberry Pi is a Linux/GNU based operating system, so it is very easy to learn MAC ID.

You can learn your MAC address in 4 steps.

-	As the root user
-	Type “ifconfig –a”
-	Find eth0 or wlan0 which internet connection will be used. 
-	Locate the numbers next to the HWaddr. This is your MAC Address

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/rpi-your-mac-1.png)

Link: http://www.coffer.com/mac_info/locate-unix.html

The lines starting with **"b8: 27: eb"** is your  MAC address of Raspberry Pi. Let's give a hint. "b8: 27: eb" is the Raspberry Pi's registered MAC address. So even if you use another Raspberry Pi it starts with "b8: 27: eb". 16.777.215 is Raspberry Pi magic number. Please estimate this magic number..  


## Support ##

Please do not hesitate to create request for this document or product named MiniIOEx-3G, or you can contact to us directly as using support@pe2a.com .

## Buy ##

If you want to buy MiniIOEx-3G, you can also use support@pe2a.com or [BUY Link](https://www.tindie.com/products/yanikgo/industrial-raspberry-pi-mini-io-shield/)

Please, contact support@pe2a.com for bulk purchase. 

