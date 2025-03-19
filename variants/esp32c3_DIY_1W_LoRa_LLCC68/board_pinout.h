#ifndef BOARD_PINOUT_H_
#define BOARD_PINOUT_H_

    //  LoRa Radio
    #define HAS_LLCC68
    #define HAS_1W_LORA
    #define RADIO_SCLK_PIN          4
    #define RADIO_MISO_PIN          5
    #define RADIO_MOSI_PIN          6
    #define RADIO_CS_PIN            7
    #define RADIO_RST_PIN           2
    #define RADIO_DIO1_PIN          10
    #define RADIO_BUSY_PIN          3
    #define RADIO_RXEN              1
    #define RADIO_TXEN              0

    //  Display
    #define HAS_DISPLAY
    
    #undef  OLED_SDA
    #undef  OLED_SCL
    #undef  OLED_RST
    
    #define OLED_SDA                8
    #define OLED_SCL                9
    #define OLED_RST                -1
    
    //  GPS
    #define GPS_RX              20
    #define GPS_TX              21
#endif