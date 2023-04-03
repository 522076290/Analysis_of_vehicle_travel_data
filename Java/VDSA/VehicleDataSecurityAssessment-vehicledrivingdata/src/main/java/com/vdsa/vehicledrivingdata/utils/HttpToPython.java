package com.vdsa.vehicledrivingdata.utils;

import cn.hutool.http.HttpRequest;
import cn.hutool.json.JSONObject;
import cn.hutool.json.JSONUtil;
import com.vdsa.common.config.RuoYiConfig;
import org.springframework.stereotype.Component;



/**
 * http访问python接口工具类
 * @author lan
 * @version 1.0
 * @data 2023/4/1 13:14
 */
@Component
public class HttpToPython {

    /**
     * python接口地址
     */
    private static String pythonApiPath = RuoYiConfig.getPythonApiPath();

    /**
     * 数据预处理接口
     * @param json
     */
    public static void datapreProcessing(String json){
        String url = pythonApiPath+"datapreProcessing/";
        String result2 = HttpRequest.post(url)
                .body(json)
                .execute().body();
    }

    /**
     * 车辆危险驾驶行为统计
     * @param json
     */
    public static void dataStatistics(String json){
        String url = pythonApiPath+"trafficStatistics/";
        String result2 = HttpRequest.post(url)
                .body(json)
                .execute().body();
    }


    /**
     * 车辆行驶地图绘制
     * @param json
     */
    public static void drawMap(String json){
        String url = pythonApiPath+"drawMap/";
        String result2 = HttpRequest.post(url)
                .body(json)
                .execute().body();
    }


    /**
     * 车辆行驶得分计算
     * @param vehicleDrivingBehaviorScoreJson 车辆得分对象json
     * @param vehicleDrivingDataJson 车辆数据对象json
     */
    public static void dataScore(String vehicleDrivingBehaviorScoreJson,String vehicleDrivingDataJson){
        String url = pythonApiPath+"drivingBehaviorScore/";
        JSONObject requestData = new JSONObject();
        requestData.put("vehicleDrivingBehaviorScoreJson", vehicleDrivingBehaviorScoreJson);
        requestData.put("vehicleDrivingDataJson", vehicleDrivingDataJson);
        String requestBody = JSONUtil.parseObj(requestData, false).toString();
        String result2 = HttpRequest.post(url)
                .body(requestBody)
                .execute().body();
    }

}
