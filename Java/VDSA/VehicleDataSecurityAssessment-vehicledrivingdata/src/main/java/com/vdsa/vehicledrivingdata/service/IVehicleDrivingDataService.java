package com.vdsa.vehicledrivingdata.service;

import java.util.List;
import com.vdsa.vehicledrivingdata.domain.VehicleDrivingData;

/**
 * 车辆驾驶行为数据Service接口
 * 
 * @author lan
 * @date 2023-03-31
 */
public interface IVehicleDrivingDataService 
{
    /**
     * 查询车辆驾驶行为数据
     * 
     * @param vehicleDataId 车辆驾驶行为数据主键
     * @return 车辆驾驶行为数据
     */
    public VehicleDrivingData selectVehicleDrivingDataByVehicleDataId(Long vehicleDataId);

    /**
     * 查询车辆驾驶行为数据列表
     * 
     * @param vehicleDrivingData 车辆驾驶行为数据
     * @return 车辆驾驶行为数据集合
     */
    public List<VehicleDrivingData> selectVehicleDrivingDataList(VehicleDrivingData vehicleDrivingData);

    /**
     * 新增车辆驾驶行为数据
     * 
     * @param vehicleDrivingData 车辆驾驶行为数据
     * @return 结果
     */
    public int insertVehicleDrivingData(VehicleDrivingData vehicleDrivingData);

    /**
     * 修改车辆驾驶行为数据
     * 
     * @param vehicleDrivingData 车辆驾驶行为数据
     * @return 结果
     */
    public int updateVehicleDrivingData(VehicleDrivingData vehicleDrivingData);

    /**
     * 预处理车辆驾驶行为数据
     *
     * @param vehicleDrivingData 车辆驾驶行为数据
     * @return 结果
     */
    public int preprocessingVehicleDrivingData(VehicleDrivingData vehicleDrivingData);

    /**
     * 统计车辆危险驾驶行为
     *
     * @param vehicleDrivingData 车辆驾驶行为数据
     * @return 结果
     */
    public int statisticsVehicleDrivingData(VehicleDrivingData vehicleDrivingData);

    /**
     * 批量删除车辆驾驶行为数据
     * 
     * @param vehicleDataIds 需要删除的车辆驾驶行为数据主键集合
     * @return 结果
     */
    public int deleteVehicleDrivingDataByVehicleDataIds(Long[] vehicleDataIds);

    /**
     * 删除车辆驾驶行为数据信息
     * 
     * @param vehicleDataId 车辆驾驶行为数据主键
     * @return 结果
     */
    public int deleteVehicleDrivingDataByVehicleDataId(Long vehicleDataId);
}
