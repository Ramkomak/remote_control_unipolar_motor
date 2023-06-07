#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "pico/binary_info.h"
 
// const uint LED_PIN = 25;
const uint A_plus = 2;
const uint A_minus = 3;
const uint B_plus = 4;
const uint B_minus = 5;




// gpio_set_dir(LED_PIN, GPIO_OUT);

//gipo
void enable_pins(){

gpio_init(A_plus);
gpio_init(A_minus);
gpio_init(B_plus);
gpio_init(B_minus);

gpio_set_dir(A_minus,1);
gpio_set_dir(A_plus,1);
gpio_set_dir(B_plus,1);
gpio_set_dir(B_minus,1);


}



int main() {
stdio_init_all();
enable_pins();

while(1){
    gpio_put(B_plus,1);
    gpio_put(A_minus,1);
    sleep_ms(10);
    gpio_put(A_minus,0);
    gpio_put(A_plus,1);
    sleep_ms(10);
    gpio_put(B_plus,0);
    gpio_put(B_minus,1);
    sleep_ms(10);
    gpio_put(A_plus,0);
    gpio_put(A_minus,1);
    sleep_ms(10);
    gpio_put(B_minus,0);

}


}


