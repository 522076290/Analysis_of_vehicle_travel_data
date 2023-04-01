package com.vdsa;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;

/**
 * 启动程序
 * 
 * @author lan
 */
@SpringBootApplication(exclude = { DataSourceAutoConfiguration.class })
public class RuoYiApplication
{
    public static void main(String[] args)
    {
        // System.setProperty("spring.devtools.restart.enabled", "false");
        SpringApplication.run(RuoYiApplication.class, args);
        System.out.println("(♥◠‿◠)ﾉﾞ  车辆行驶数据安全评估系统启动成功   ლ(´ڡ`ლ)ﾞ  \n" +
                " __      __  _     _      _            _       _                                   _ _                                                            _   \n" +
                " \\ \\    / / | |   (_)    | |          | |     | |                                 (_) |                                                          | |  \n" +
                "  \\ \\  / /__| |__  _  ___| | ___    __| | __ _| |_ __ _   ___  ___  ___ _   _ _ __ _| |_ _   _    __ _ ___ ___  ___  ___ ___ _ __ ___   ___ _ __ | |_ \n" +
                " |(_ o    \\ \\/ / _ \\ '_ \\| |/ __| |/ _ \\  / _` |/ _` | __/ _` | / __|/ _ \\/ __| | | | '__| | __| | | |  / _` / __/ __|/ _ \\/ __/ __| '_ ` _ \\ / _ \\ '_ \\| __|\n" +
                "    \\  /  __/ | | | | (__| |  __/ | (_| | (_| | || (_| | \\__ \\  __/ (__| |_| | |  | | |_| |_| | | (_| \\__ \\__ \\  __/\\__ \\__ \\ | | | | |  __/ | | | |_ \n" +
                "     \\/ \\___|_| |_|_|\\___|_|\\___|  \\__,_|\\__,_|\\__\\__,_| |___/\\___|\\___|\\__,_|_|  |_|\\__|\\__, |  \\__,_|___/___/\\___||___/___/_| |_| |_|\\___|_| |_|\\__|\n" +
                "                                                                                          __/ |                                                       \n" +
                "                                                                                         |___/                                                        "
        );
    }
}
