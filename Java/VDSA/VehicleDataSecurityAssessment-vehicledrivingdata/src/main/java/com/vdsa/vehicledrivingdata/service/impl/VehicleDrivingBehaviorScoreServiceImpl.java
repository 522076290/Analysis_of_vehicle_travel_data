package com.vdsa.vehicledrivingdata.service.impl;

import java.util.List;

import cn.hutool.json.JSONUtil;
import com.vdsa.common.utils.DateUtils;
import com.vdsa.vehicledrivingdata.domain.VehicleDrivingData;
import com.vdsa.vehicledrivingdata.mapper.VehicleDrivingDataMapper;
import com.vdsa.vehicledrivingdata.utils.HttpToPython;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.vdsa.vehicledrivingdata.mapper.VehicleDrivingBehaviorScoreMapper;
import com.vdsa.vehicledrivingdata.domain.VehicleDrivingBehaviorScore;
import com.vdsa.vehicledrivingdata.service.IVehicleDrivingBehaviorScoreService;

/**
 * 车辆驾驶行为得分Service业务层处理
 * 
 * @author ruoyi
 * @date 2023-04-03
 */
@Service
public class VehicleDrivingBehaviorScoreServiceImpl implements IVehicleDrivingBehaviorScoreService 
{
    @Autowired
    private VehicleDrivingBehaviorScoreMapper vehicleDrivingBehaviorScoreMapper;

    @Autowired
    private VehicleDrivingDataMapper vehicleDrivingDataMapper;

    /**
     * 查询车辆驾驶行为得分
     * 
     * @param id 车辆驾驶行为得分主键
     * @return 车辆驾驶行为得分
     */
    @Override
    public VehicleDrivingBehaviorScore selectVehicleDrivingBehaviorScoreById(Long id)
    {
        return vehicleDrivingBehaviorScoreMapper.selectVehicleDrivingBehaviorScoreById(id);
    }

    /**
     * 查询车辆驾驶行为得分列表
     * 
     * @param vehicleDrivingBehaviorScore 车辆驾驶行为得分
     * @return 车辆驾驶行为得分
     */
    @Override
    public List<VehicleDrivingBehaviorScore> selectVehicleDrivingBehaviorScoreList(VehicleDrivingBehaviorScore vehicleDrivingBehaviorScore)
    {
        return vehicleDrivingBehaviorScoreMapper.selectVehicleDrivingBehaviorScoreList(vehicleDrivingBehaviorScore);
    }

    /**
     * 新增车辆驾驶行为得分
     * 
     * @param vehicleDrivingBehaviorScore 车辆驾驶行为得分
     * @return 结果
     */
    @Override
    public int insertVehicleDrivingBehaviorScore(VehicleDrivingBehaviorScore vehicleDrivingBehaviorScore)
    {
        vehicleDrivingBehaviorScore.setCreateTime(DateUtils.getNowDate());
        // 修改处理状态 处理中
        Long mapState = 1L;
        vehicleDrivingBehaviorScore.setScoringStatus(mapState);
        // 获取VehicleDrivingData的对象
        VehicleDrivingData vehicleDrivingData = vehicleDrivingDataMapper.selectVehicleDrivingDataByVehicleDataId(vehicleDrivingBehaviorScore.getVehicleDataId());
        // 先执行插入获取主键id后调用绘制
        int result = vehicleDrivingBehaviorScoreMapper.insertVehicleDrivingBehaviorScore(vehicleDrivingBehaviorScore);
        // 调用python计算分数
        HttpToPython.dataScore(JSONUtil.toJsonStr(vehicleDrivingBehaviorScore),JSONUtil.toJsonStr(vehicleDrivingData));
        return result;
    }

    /**
     * 修改车辆驾驶行为得分
     * 
     * @param vehicleDrivingBehaviorScore 车辆驾驶行为得分
     * @return 结果
     */
    @Override
    public int updateVehicleDrivingBehaviorScore(VehicleDrivingBehaviorScore vehicleDrivingBehaviorScore)
    {
        vehicleDrivingBehaviorScore.setUpdateTime(DateUtils.getNowDate());
        return vehicleDrivingBehaviorScoreMapper.updateVehicleDrivingBehaviorScore(vehicleDrivingBehaviorScore);
    }

    /**
     * 对车辆行为分类
     * @param id 车辆驾驶行为得分id
     * @return
     */
    @Override
    public int classifVehicleDrivingBehaviorScore(Long id) {

        VehicleDrivingBehaviorScore vehicleDrivingBehaviorScore = vehicleDrivingBehaviorScoreMapper.selectVehicleDrivingBehaviorScoreById(id);

        vehicleDrivingBehaviorScore.setCreateTime(DateUtils.getNowDate());
        // 修改处理状态 处理中
        Long mapState = 1L;
        vehicleDrivingBehaviorScore.setScoringStatus(mapState);

        // 获取VehicleDrivingData的对象
        VehicleDrivingData vehicleDrivingData = vehicleDrivingDataMapper.selectVehicleDrivingDataByVehicleDataId(vehicleDrivingBehaviorScore.getVehicleDataId());

        // 调用python空闲分类
        HttpToPython.classifScore(JSONUtil.toJsonStr(vehicleDrivingBehaviorScore),JSONUtil.toJsonStr(vehicleDrivingData));

        vehicleDrivingBehaviorScore.setUpdateTime(DateUtils.getNowDate());
        return vehicleDrivingBehaviorScoreMapper.updateVehicleDrivingBehaviorScore(vehicleDrivingBehaviorScore);
    }

    /**
     * 批量删除车辆驾驶行为得分
     * 
     * @param ids 需要删除的车辆驾驶行为得分主键
     * @return 结果
     */
    @Override
    public int deleteVehicleDrivingBehaviorScoreByIds(Long[] ids)
    {
        return vehicleDrivingBehaviorScoreMapper.deleteVehicleDrivingBehaviorScoreByIds(ids);
    }

    /**
     * 删除车辆驾驶行为得分信息
     * 
     * @param id 车辆驾驶行为得分主键
     * @return 结果
     */
    @Override
    public int deleteVehicleDrivingBehaviorScoreById(Long id)
    {
        return vehicleDrivingBehaviorScoreMapper.deleteVehicleDrivingBehaviorScoreById(id);
    }
}
