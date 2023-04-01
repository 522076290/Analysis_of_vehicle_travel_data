package com.vdsa.vehicledrivingdata.service.impl;

import java.util.List;

import cn.hutool.json.JSONUtil;
import com.vdsa.common.core.domain.model.LoginUser;
import com.vdsa.common.utils.SecurityUtils;
import com.vdsa.vehicledrivingdata.utils.HttpToPython;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.vdsa.vehicledrivingdata.mapper.VehicleDrivingDataMapper;
import com.vdsa.vehicledrivingdata.domain.VehicleDrivingData;
import com.vdsa.vehicledrivingdata.service.IVehicleDrivingDataService;

/**
 * 车辆驾驶行为数据Service业务层处理
 * 
 * @author lan
 * @date 2023-03-31
 */
@Service
public class VehicleDrivingDataServiceImpl implements IVehicleDrivingDataService 
{
    @Autowired
    private VehicleDrivingDataMapper vehicleDrivingDataMapper;

    /**
     * 查询车辆驾驶行为数据
     * 
     * @param vehicleDataId 车辆驾驶行为数据主键
     * @return 车辆驾驶行为数据
     */
    @Override
    public VehicleDrivingData selectVehicleDrivingDataByVehicleDataId(Long vehicleDataId)
    {
        return vehicleDrivingDataMapper.selectVehicleDrivingDataByVehicleDataId(vehicleDataId);
    }

    /**
     * 查询车辆驾驶行为数据列表
     * 
     * @param vehicleDrivingData 车辆驾驶行为数据
     * @return 车辆驾驶行为数据
     */
    @Override
    public List<VehicleDrivingData> selectVehicleDrivingDataList(VehicleDrivingData vehicleDrivingData)
    {
        return vehicleDrivingDataMapper.selectVehicleDrivingDataList(vehicleDrivingData);
    }

    /**
     * 新增车辆驾驶行为数据
     * 
     * @param vehicleDrivingData 车辆驾驶行为数据
     * @return 结果
     */
    @Override
    public int insertVehicleDrivingData(VehicleDrivingData vehicleDrivingData)
    {
        LoginUser loginUser = SecurityUtils.getLoginUser();
        vehicleDrivingData.setUserId(loginUser.getUserId());
        return vehicleDrivingDataMapper.insertVehicleDrivingData(vehicleDrivingData);
    }

    /**
     * 修改车辆驾驶行为数据
     * 
     * @param vehicleDrivingData 车辆驾驶行为数据
     * @return 结果
     */
    @Override
    public int updateVehicleDrivingData(VehicleDrivingData vehicleDrivingData)
    {
        return vehicleDrivingDataMapper.updateVehicleDrivingData(vehicleDrivingData);
    }

    /**
     * 预处理车辆驾驶行为数据
     *
     * @param vehicleDrivingData 车辆驾驶行为数据
     * @return 结果
     */
    @Override
    public int preprocessingVehicleDrivingData(VehicleDrivingData vehicleDrivingData) {
        // 修改处理状态 处理中
        Long preprocessingState = 1L;
        vehicleDrivingData.setPreprocessingState(preprocessingState);
        HttpToPython.datapreProcessing(JSONUtil.toJsonStr(vehicleDrivingData));
        return vehicleDrivingDataMapper.updateVehicleDrivingData(vehicleDrivingData);
    }

    @Override
    public int statisticsVehicleDrivingData(VehicleDrivingData vehicleDrivingData) {
        // 修改统计状态 处理中
        Long statisticsState = 1L;
        vehicleDrivingData.setStatisticalState(statisticsState);
        HttpToPython.dataStatistics(JSONUtil.toJsonStr(vehicleDrivingData));
        return vehicleDrivingDataMapper.updateVehicleDrivingData(vehicleDrivingData);
    }

    /**
     * 批量删除车辆驾驶行为数据
     * 
     * @param vehicleDataIds 需要删除的车辆驾驶行为数据主键
     * @return 结果
     */
    @Override
    public int deleteVehicleDrivingDataByVehicleDataIds(Long[] vehicleDataIds)
    {
        return vehicleDrivingDataMapper.deleteVehicleDrivingDataByVehicleDataIds(vehicleDataIds);
    }

    /**
     * 删除车辆驾驶行为数据信息
     * 
     * @param vehicleDataId 车辆驾驶行为数据主键
     * @return 结果
     */
    @Override
    public int deleteVehicleDrivingDataByVehicleDataId(Long vehicleDataId)
    {
        return vehicleDrivingDataMapper.deleteVehicleDrivingDataByVehicleDataId(vehicleDataId);
    }
}
