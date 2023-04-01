package com.vdsa.vehicledrivingdata.mapper;

import java.util.List;
import com.vdsa.vehicledrivingdata.domain.VehicleDrivingData;

/**
 * 车辆驾驶行为数据Mapper接口
 * 
 * @author lan
 * @date 2023-03-31
 */
public interface VehicleDrivingDataMapper 
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
     * 删除车辆驾驶行为数据
     * 
     * @param vehicleDataId 车辆驾驶行为数据主键
     * @return 结果
     */
    public int deleteVehicleDrivingDataByVehicleDataId(Long vehicleDataId);

    /**
     * 批量删除车辆驾驶行为数据
     * 
     * @param vehicleDataIds 需要删除的数据主键集合
     * @return 结果
     */
    public int deleteVehicleDrivingDataByVehicleDataIds(Long[] vehicleDataIds);
}
