#include <main.h>
                  //No low voltage prgming, B3(PIC16) or B5(PIC18) used for I/O


#define LCD_ENABLE_PIN  PIN_E1                                    ////
#define LCD_RS_PIN      PIN_E0                                    ////
#define LCD_RW_PIN      PIN_E2                                    ////
#define LCD_DATA4       PIN_B4                                    ////
#define LCD_DATA5       PIN_B5                                    ////
#define LCD_DATA6       PIN_B6                                    ////
#define LCD_DATA7       PIN_B7                                    ////
#include "lcd.c"
#use fast_io(b) 
   
   
int16 d0,d1,d2,d3,update = 0;
#INT_timer0
void adcdac(){
   set_timer0(0);
   set_adc_channel(0);//akim
   delay_us(300);
   d0 = read_adc();
   set_adc_channel(1);//olculen gerilim
   delay_us(300);
   d1 = read_adc();
   set_adc_channel(3);//gerilim ayarý
   delay_us(300);
   d2 = read_adc();
   set_adc_channel(4); //akim ayarý
   delay_us(300);
   d3 = read_adc();
   update = 1;

}
void dac(int16 dacv){
   int1 LSB0,LSB1;
   LSB0 = dacv&1;  //1.bit
   LSB1 = dacv&2/2; //2.bit
   if (LSB0 == 1){
      output_high(pin_b2);//1.bit 1
   }else if(LSB0==0){
      output_low(pin_b2);//1.bit 0
   }
   if (LSB1 == 1){
      output_high(pin_b3);//2.bit 1
   }else if(LSB1 == 0){
      output_low(pin_b3);//2.bit 0
   }
   dacv = (dacv- LSB0 -LSB1*2)/4;//1ve2 hariç tüm bitler
   output_d(dacv);//3,4,5,6,7,8,9,10. bitler 
}
void main()
{

   setup_timer_1(T1_DISABLED); // T1 zamanlayýcýsý devre dýþý
   setup_timer_2(T2_DISABLED,0,1); // T2 zamanlayýcýsý devre dýþý


   setup_CCP1(CCP_OFF); // CCP1 birimi devre dýþý
   setup_CCP2(CCP_OFF); // CCP2 birimi devre dýþý
   setup_adc(adc_clock_div_32);
   setup_adc_ports(AN0_AN1_AN2_AN3_AN4);
   setup_timer_0(RTCC_INTERNAL|RTCC_DIV_256);
   enable_interrupts(INT_timer0);
   enable_interrupts(GLOBAL);
   set_tris_d(0x00);
   set_tris_b(0x00);
   set_tris_e(0x00);
   set_tris_a(0xff);
   lcd_init();
   delay_us(100);
   int i = 0;
   float akim = 0,gerilim = 0,g=0,a=0;
  while(1)
   {
   dac(d2);
   if (update == 1){
      lcd_putc("\f");
      akim = (((float) d0)*(5/(1024*0.22*((20/3.3)+1))));
      gerilim = d1*(0.0048828)*(4.063030);
      g = (((((float) d2)*(5)/1024)*(22/6.8)+1));
      printf(lcd_putc,"V: %f A: %f\nA: %f G: %f"g,a,akim,gerilim);
      update = 0;
   }

   }

}
