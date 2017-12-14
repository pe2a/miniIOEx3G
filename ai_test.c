#include <stdio.h>
#include <bcm2835.h>


#define ai_StepDown 100

/*pe2a SPI Clock */
#define smallex_SPI_Clock BCM2835_SPI_CLOCK_DIVIDER_65536
#define smallex_GPIO_AI_CS0 BCM2835_SPI_CS0  //analog input SPI chip select

//AI init
int smallex_AI_init(const int val){
	
	
	//val : 0 spi_close ; val : 1 spi open
	
	
	if(val){
		
	if (!bcm2835_init())
    {
      printf("bcm2835_init failed. Are you running as root??\n");
      return 1;
    }

    if (!bcm2835_spi_begin())
    {
      printf("bcm2835_spi_begin failed. Are you running as root??\n");
      return 1;
    }
    bcm2835_spi_begin();
    bcm2835_spi_setBitOrder(BCM2835_SPI_BIT_ORDER_MSBFIRST);      // The default
    bcm2835_spi_setDataMode(BCM2835_SPI_MODE0);                   // The default
    bcm2835_spi_setClockDivider(smallex_SPI_Clock); // The default
    bcm2835_spi_chipSelect(smallex_GPIO_AI_CS0);                      // The default
    bcm2835_spi_setChipSelectPolarity(smallex_GPIO_AI_CS0, LOW);      // the default
		
	}
	
	else{
		
		
		bcm2835_spi_end(); //ATTENTION! SPI will be closed
		
	}
	
	return -1;
	
	
}


//AI reading channel val
int smallex_getVal(const int channel){
	
	
	char tbuf[3]; //transmitting values to mcp3208
	char rbuf[3]; //reading value from mcp3208
	
	int adc = 0;
	int adcDigNumber = 0;
	//double adcVolt 0.0
	
	
	if(channel == 0){
		
		
		//ch0
		tbuf[0] = 0b00000110;
		tbuf[1] = 0b00000000;
		tbuf[2] = 0b00000000;
		
		
	}
	
		
	if(channel == 1){
		
		
		//ch0
		tbuf[0] = 0b00000110;
		tbuf[1] = 0b01000000;
		tbuf[2] = 0b00000000;
		
		
	}
	
	if(channel == 2){
		
		
		//ch0
		tbuf[0] = 0b00000110;
		tbuf[1] = 0b10000000;
		tbuf[2] = 0b00000000;
		
		
	}
	
		
	if(channel == 3){
		
		
		//ch3
		tbuf[0] = 0b00000110;
		tbuf[1] = 0b11000000;
		tbuf[2] = 0b00000000;
		
		
	}
	
			
	if(channel == 4){
		
		
		//ch4
		tbuf[0] = 0b00000111;
		tbuf[1] = 0b00000000;
		tbuf[2] = 0b00000000;
		
		
	}
	
				
	if(channel == 5){
		
		
		//ch5
		tbuf[0] = 0b00000111;
		tbuf[1] = 0b01000000;
		tbuf[2] = 0b00000000;
		
		
	}
	
	
					
	if(channel == 6){
		
		
		//ch0
		tbuf[0] = 0b00000111;
		tbuf[1] = 0b10000000;
		tbuf[2] = 0b00000000;
		
		
	}
	
	if(channel == 7){
		
		
		//ch0
		tbuf[0] = 0b00000111;
		tbuf[1] = 0b11000000;
		tbuf[2] = 0b00000000;
		
		
	}
	
	
	bcm2835_spi_transfernb(tbuf, rbuf,sizeof(tbuf));
	adcDigNumber = (rbuf[1] << 8) + rbuf[2];
	adcDigNumber &= 0xFFF;
	
	return adcDigNumber; //should be 0 - 4095
	
	/*
	 * adcVolt = adcDigNumber * 3300.0 / 4095.0
	 * 
	 * */
	
	
}

int main(){
	
	double adc = 0;
	//init for Analog Input 
	smallex_AI_init(1);
	
	
	while(1){
		
		
		//miniIOex uzerinde J4 konnektoru AI1
		printf("Digital Value channel :%d is  %d \n",0,smallex_getVal(0));
		printf("Voltage Value channel %d: %.2f \n",0,(smallex_getVal(0) * 3300.0 / 4095.0) / ai_StepDown);
		
		printf("\n");
		delay(250);
		
		//miniIOex uzerinde J4 konnektoru AI2
		printf("Digital Value channel :%d is : %d \n",1,smallex_getVal(1));
		printf("Voltage Value channel %d: %.2f \n",1,(smallex_getVal(1) * 3300.0 / 4095.0) / ai_StepDown);
		
			
		printf("\n");
		delay(250);
		
		
		printf("\n");
		
		//giris beslemesi, okunan degere 2*0.75V = 1.5V daha eklenebilir kopru diyot(cift) gerilim dusumunden dolayi
		printf("Digital Value channel :%d is : %d \n",7,smallex_getVal(7));
		printf("Voltage Value channel %d: %.2f \n",7,(smallex_getVal(7) * 3300.0 / 4095.0) / ai_StepDown);
		
			
		printf("\n");
	
	
		delay(3000);
		
		system("clear");
		
		
		
		
		
	}
	
	
	
	
	return 0;
}
