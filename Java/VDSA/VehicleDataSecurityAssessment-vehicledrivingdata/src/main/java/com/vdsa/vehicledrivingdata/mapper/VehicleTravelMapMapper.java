package com.vdsa.vehicledrivingdata.mapper;

import java.util.List;
import com.vdsa.vehicledrivingdata.domain.VehicleTravelMap;

/**
 * 车辆数据地图Mapper接口
 * 
 * @author ruoyi
 * @date 2023-04-02
 */
public interface VehicleTravelMapMapper 
{
    /**
     * 查询车辆数据地图
     * 
     * @param id 车辆数据地图主键
     * @return 车辆数据地图
     */
    public VehicleTravelMap selectVehicleTravelMapById(Long id);

    /**
     * 查询车辆数据地图列表
     * 
     * @param vehicleTravelMap 车辆数据地图
     * @return 车辆数据地图集合
     */
    public List<VehicleTravelMap> selectVehicleTravelMapList(VehicleTravelMap vehicleTravelMap);

    /**
     * 新增车辆数据地图
     * 
     * @param vehicleTravelMap 车辆数据地图
     * @return 结果
     */
    public int insertVehicleTravelMap(VehicleTravelMap vehicleTravelMap);

    /**
     * 修改车辆数据地图
     * 
     * @param vehicleTravelMap 车辆数据地图
     * @return 结果
     */
    public int updateVehicleTravelMap(VehicleTravelMap vehicleTravelMap);

    /**
     * 删除车辆数据地图
     * 
     * @param id 车辆数据地图主键
     * @return 结果
     */
    public int deleteVehicleTravelMapById(Long id);

    /**
     * 批量删除车辆数据地图
     * 
     * @param ids 需要删除的数据主键集合
     * @return 结果
     */
    public int deleteVehicleTravelMapByIds(Long[] ids);
}
