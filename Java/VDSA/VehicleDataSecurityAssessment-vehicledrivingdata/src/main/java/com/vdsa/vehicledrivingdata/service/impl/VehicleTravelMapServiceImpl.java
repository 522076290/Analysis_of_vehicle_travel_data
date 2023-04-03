package com.vdsa.vehicledrivingdata.service.impl;

import java.util.List;

import cn.hutool.json.JSONUtil;
import com.vdsa.common.utils.DateUtils;
import com.vdsa.vehicledrivingdata.mapper.VehicleDrivingDataMapper;
import com.vdsa.vehicledrivingdata.utils.HttpToPython;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.vdsa.vehicledrivingdata.mapper.VehicleTravelMapMapper;
import com.vdsa.vehicledrivingdata.domain.VehicleTravelMap;
import com.vdsa.vehicledrivingdata.service.IVehicleTravelMapService;

/**
 * 车辆数据地图Service业务层处理
 * 
 * @author ruoyi
 * @date 2023-04-02
 */
@Service
public class VehicleTravelMapServiceImpl implements IVehicleTravelMapService 
{
    @Autowired
    private VehicleTravelMapMapper vehicleTravelMapMapper;
    @Autowired
    private VehicleDrivingDataMapper vehicleDrivingDataMapper;

    /**
     * 查询车辆数据地图
     * 
     * @param id 车辆数据地图主键
     * @return 车辆数据地图
     */
    @Override
    public VehicleTravelMap selectVehicleTravelMapById(Long id)
    {
        return vehicleTravelMapMapper.selectVehicleTravelMapById(id);
    }

    /**
     * 查询车辆数据地图列表
     * 
     * @param vehicleTravelMap 车辆数据地图
     * @return 车辆数据地图
     */
    @Override
    public List<VehicleTravelMap> selectVehicleTravelMapList(VehicleTravelMap vehicleTravelMap)
    {
        return vehicleTravelMapMapper.selectVehicleTravelMapList(vehicleTravelMap);
    }

    /**
     * 新增车辆数据地图
     * 
     * @param vehicleTravelMap 车辆数据地图
     * @return 结果
     */
    @Override
    public int insertVehicleTravelMap(VehicleTravelMap vehicleTravelMap)
    {
        vehicleTravelMap.setCreateTime(DateUtils.getNowDate());
        // 修改处理状态 处理中
        Long mapState = 1L;
        vehicleTravelMap.setBuildMapStatus(mapState);
        // 获取数据地址
        vehicleTravelMap.setMapPath(vehicleDrivingDataMapper.selectVehicleDrivingDataByVehicleDataId(vehicleTravelMap.getVehicleDataId()).getDataPath());
        // 先执行插入获取主键id后调用绘制
        int result = vehicleTravelMapMapper.insertVehicleTravelMap(vehicleTravelMap);
        // 调用python绘制地图
        HttpToPython.drawMap(JSONUtil.toJsonStr(vehicleTravelMap));
        return result;
    }

    /**
     * 修改车辆数据地图
     * 
     * @param vehicleTravelMap 车辆数据地图
     * @return 结果
     */
    @Override
    public int updateVehicleTravelMap(VehicleTravelMap vehicleTravelMap)
    {
        vehicleTravelMap.setUpdateTime(DateUtils.getNowDate());
        return vehicleTravelMapMapper.updateVehicleTravelMap(vehicleTravelMap);
    }

    /**
     * 批量删除车辆数据地图
     * 
     * @param ids 需要删除的车辆数据地图主键
     * @return 结果
     */
    @Override
    public int deleteVehicleTravelMapByIds(Long[] ids)
    {
        return vehicleTravelMapMapper.deleteVehicleTravelMapByIds(ids);
    }

    /**
     * 删除车辆数据地图信息
     * 
     * @param id 车辆数据地图主键
     * @return 结果
     */
    @Override
    public int deleteVehicleTravelMapById(Long id)
    {
        return vehicleTravelMapMapper.deleteVehicleTravelMapById(id);
    }
}
