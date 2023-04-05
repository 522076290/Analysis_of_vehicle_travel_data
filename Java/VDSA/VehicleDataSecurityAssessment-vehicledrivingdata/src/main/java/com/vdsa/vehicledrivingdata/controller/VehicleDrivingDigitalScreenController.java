package com.vdsa.vehicledrivingdata.controller;

import cn.hutool.core.date.DateUtil;
import com.vdsa.common.core.controller.BaseController;
import com.vdsa.common.core.page.TableDataInfo;
import com.vdsa.vehicledrivingdata.domain.VehicleDigitalScreenResp;
import com.vdsa.vehicledrivingdata.domain.VehicleDrivingBehaviorScore;
import com.vdsa.vehicledrivingdata.domain.VehicleDrivingData;
import com.vdsa.vehicledrivingdata.domain.VehicleTravelMap;
import com.vdsa.vehicledrivingdata.service.IVehicleDrivingBehaviorScoreService;
import com.vdsa.vehicledrivingdata.service.IVehicleDrivingDataService;
import com.vdsa.vehicledrivingdata.service.IVehicleTravelMapService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;


import java.util.List;

import static com.vdsa.common.utils.PageUtils.startPage;

/**
 * 专门返回数字大屏的数据
 * @author lan
 * @version 1.0
 * @data 2023/4/5 15:02
 */
@RestController
@RequestMapping("/vehicledriving/digital")
public class VehicleDrivingDigitalScreenController extends BaseController {
    @Autowired
    private IVehicleDrivingDataService vehicleDrivingDataService;

    @Autowired
    private IVehicleTravelMapService vehicleTravelMapService;

    @Autowired
    private IVehicleDrivingBehaviorScoreService vehicleDrivingBehaviorScoreService;


    /**
     * 查询车辆驾驶行为得分的统计量
     */
    @GetMapping("/statistical-magnitude")
    public TableDataInfo statisticalMagnitude()
    {
        startPage();
        VehicleDrivingBehaviorScore vehicleDrivingBehaviorScore = new VehicleDrivingBehaviorScore();
        List<VehicleDrivingBehaviorScore> list = vehicleDrivingBehaviorScoreService.selectVehicleDrivingBehaviorScoreList(vehicleDrivingBehaviorScore);
        VehicleDigitalScreenResp vehicleDigitalScreenResp = new VehicleDigitalScreenResp();

        // 获取今天日期字符串
        String dateString = DateUtil.today();
        // 将日期字符串解析成日期对象
        Date today = DateUtil.parse(dateString);

        int todayStatisticsNumbers = 0;
        int nowStatisticsNumbers = 0;

        for (VehicleDrivingBehaviorScore item:list
             ) {
            // 获取今天日期
            if(DateUtil.isSameDay(today, item.getCreateTime())){
                todayStatisticsNumbers++;
            }
            if (item.getScoringStatus().equals(1L)){
                nowStatisticsNumbers++;
            }
        }
        // 设置统计数量
        vehicleDigitalScreenResp.setAllStatisticsNumbers(list.size());
        vehicleDigitalScreenResp.setTodayStatisticsNumbers(todayStatisticsNumbers);
        vehicleDigitalScreenResp.setNowStatisticsNumbers(nowStatisticsNumbers);
        List<VehicleDigitalScreenResp> digitalList =new ArrayList<VehicleDigitalScreenResp>();
        digitalList.add(vehicleDigitalScreenResp);
        return getDataTable(digitalList);
    }



    /**
     * 查询车辆数据处理情况
     */
    @GetMapping("/statistical-processing-data")
    public TableDataInfo statisticalProcessingData()
    {
        startPage();
        VehicleDrivingData vehicleDrivingData = new VehicleDrivingData();
        List<VehicleDrivingData> list = vehicleDrivingDataService.selectVehicleDrivingDataList(vehicleDrivingData);
        VehicleDigitalScreenResp vehicleDigitalScreenResp = new VehicleDigitalScreenResp();

        int throughStatisticalRiskDataNumbers = 0;
        int uncountedRiskDataNumbers = 0;
        int throughPreprocessingDataNumbers = 0;
        int uncountedPreprocessingDataNumbers = 0;

        for (VehicleDrivingData item:list
        ) {
            if(item.getStatisticalState().equals(0L)){
                uncountedRiskDataNumbers++;
            }
            if (item.getStatisticalState().equals(2L)){
                throughStatisticalRiskDataNumbers++;
            }
            if(item.getPreprocessingState().equals(0L)){
                uncountedPreprocessingDataNumbers++;
            }
            if (item.getPreprocessingState().equals(2L)){
                throughPreprocessingDataNumbers++;
            }
        }
        // 设置统计数量
        vehicleDigitalScreenResp.setThroughStatisticalRiskData(throughStatisticalRiskDataNumbers);
        vehicleDigitalScreenResp.setThroughPreprocessingData(throughPreprocessingDataNumbers);
        vehicleDigitalScreenResp.setUncountedRiskData(uncountedRiskDataNumbers);
        vehicleDigitalScreenResp.setUncountedPreprocessingData(uncountedPreprocessingDataNumbers);

        List<VehicleDigitalScreenResp> digitalList =new ArrayList<VehicleDigitalScreenResp>();
        digitalList.add(vehicleDigitalScreenResp);
        return getDataTable(digitalList);
    }

}
