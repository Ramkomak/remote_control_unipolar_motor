#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "pico/binary_info.h"
 

const uint A_plus = 2;
const uint A_minus = 3;
const uint B_plus = 4;
const uint B_minus = 5;

const uint left = 1;
const uint right = 0;


const int control_tab1[4] = {0,1,1,0};
const int control_tab2[4] = {1,1,0,0};
const int control_tab3[4] = {1,0,0,1};
const int control_tab4[4] = {0,0,1,1};


static int speed_control = 10000;
static int direction = left;


//gipo enable and set direction
void enable_pins()
{
    gpio_init(A_plus);
    gpio_init(A_minus);
    gpio_init(B_plus);
    gpio_init(B_minus);

    gpio_set_dir(A_minus,1);
    gpio_set_dir(A_plus,1);
    gpio_set_dir(B_plus,1);
    gpio_set_dir(B_minus,1);
}
void call_back(u_int gpio, u_int32_t events)
{
    
    
    if(events == GPIO_IRQ_EDGE_RISE)
    {
        
        if(gpio == 6)
        {
            
            printf("działa %d\n",speed_control);
            speed_control = speed_control+100;
            
        }
        if(gpio == 7)
        {
                printf("działa %d\n",speed_control);
            if (speed_control>1001)
                speed_control = speed_control-100;
            else
            {
                gpio_put(25,1);
                for (int r = 0; r++; r<100)
                if(r == 99)
                    gpio_put(25,0);
            }
        }
        if(gpio == 8)
        {
            direction = left;
            printf("left\n");
        }
        if(gpio == 9)
        {
            direction = right;
            printf("right\n");
        }
    }    
}
void rotate()
{
int i = 0;

while(1)
{
    if(direction == left)
        gpio_put(A_plus,control_tab1[i]); gpio_put(B_plus,control_tab2[i]); gpio_put(A_minus,control_tab3[i]); gpio_put(B_minus,control_tab4[i]);
    if(direction == right)
        gpio_put(A_plus,control_tab1[i]); gpio_put(B_plus,control_tab4[i]); gpio_put(A_minus,control_tab3[i]); gpio_put(B_minus,control_tab2[i]);
    sleep_us(speed_control);
    i++;
    if(i>4)
        i = 0; 
}

}

int main() {

stdio_init_all();

enable_pins();

gpio_pull_up(6);
gpio_pull_up(7);
gpio_pull_up(8);
gpio_pull_up(9);

gpio_set_irq_enabled_with_callback(6, GPIO_IRQ_EDGE_RISE , true, &call_back);
gpio_set_irq_enabled_with_callback(7, GPIO_IRQ_EDGE_RISE , true, &call_back);
gpio_set_irq_enabled_with_callback(8, GPIO_IRQ_EDGE_RISE , true, &call_back);
gpio_set_irq_enabled_with_callback(9, GPIO_IRQ_EDGE_RISE , true, &call_back);


while(1)
{
    rotate();
}

return 0;
}


