package com.vdsa.vehicledrivingdata.service;

import java.util.List;
import com.vdsa.vehicledrivingdata.domain.VehicleDrivingBehaviorScore;

/**
 * 车辆驾驶行为得分Service接口
 * 
 * @author ruoyi
 * @date 2023-04-03
 */
public interface IVehicleDrivingBehaviorScoreService 
{
    /**
     * 查询车辆驾驶行为得分
     * 
     * @param id 车辆驾驶行为得分主键
     * @return 车辆驾驶行为得分
     */
    public VehicleDrivingBehaviorScore selectVehicleDrivingBehaviorScoreById(Long id);

    /**
     * 查询车辆驾驶行为得分列表
     * 
     * @param vehicleDrivingBehaviorScore 车辆驾驶行为得分
     * @return 车辆驾驶行为得分集合
     */
    public List<VehicleDrivingBehaviorScore> selectVehicleDrivingBehaviorScoreList(VehicleDrivingBehaviorScore vehicleDrivingBehaviorScore);

    /**
     * 新增车辆驾驶行为得分
     * 
     * @param vehicleDrivingBehaviorScore 车辆驾驶行为得分
     * @return 结果
     */
    public int insertVehicleDrivingBehaviorScore(VehicleDrivingBehaviorScore vehicleDrivingBehaviorScore);

    /**
     * 修改车辆驾驶行为得分
     * 
     * @param vehicleDrivingBehaviorScore 车辆驾驶行为得分
     * @return 结果
     */
    public int updateVehicleDrivingBehaviorScore(VehicleDrivingBehaviorScore vehicleDrivingBehaviorScore);


    /**
     * 修改车辆驾驶分类
     *
     * @param id 车辆驾驶行为得分id
     * @return 结果
     */
    public int classifVehicleDrivingBehaviorScore(Long id);


    /**
     * 批量删除车辆驾驶行为得分
     * 
     * @param ids 需要删除的车辆驾驶行为得分主键集合
     * @return 结果
     */
    public int deleteVehicleDrivingBehaviorScoreByIds(Long[] ids);

    /**
     * 删除车辆驾驶行为得分信息
     * 
     * @param id 车辆驾驶行为得分主键
     * @return 结果
     */
    public int deleteVehicleDrivingBehaviorScoreById(Long id);
}
