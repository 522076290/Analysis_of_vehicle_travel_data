package com.vdsa.vehicledrivingdata.domain;

import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;
import com.vdsa.common.annotation.Excel;
import com.vdsa.common.core.domain.BaseEntity;

/**
 * 车辆数据地图对象 vehicle_travel_map
 * 
 * @author ruoyi
 * @date 2023-04-02
 */
public class VehicleTravelMap extends BaseEntity
{
    private static final long serialVersionUID = 1L;

    /** 主键 */
    private Long id;

    /** 对应驾驶数据id */
    @Excel(name = "对应驾驶数据id")
    private Long vehicleDataId;

    /** 地图路径 */
    @Excel(name = "地图路径")
    private String mapPath;

    /** 地图生成状态 */
    @Excel(name = "地图生成状态")
    private Long buildMapStatus;

    public void setId(Long id) 
    {
        this.id = id;
    }

    public Long getId() 
    {
        return id;
    }
    public void setVehicleDataId(Long vehicleDataId) 
    {
        this.vehicleDataId = vehicleDataId;
    }

    public Long getVehicleDataId() 
    {
        return vehicleDataId;
    }
    public void setMapPath(String mapPath) 
    {
        this.mapPath = mapPath;
    }

    public String getMapPath() 
    {
        return mapPath;
    }
    public void setBuildMapStatus(Long buildMapStatus) 
    {
        this.buildMapStatus = buildMapStatus;
    }

    public Long getBuildMapStatus() 
    {
        return buildMapStatus;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this,ToStringStyle.MULTI_LINE_STYLE)
            .append("id", getId())
            .append("vehicleDataId", getVehicleDataId())
            .append("mapPath", getMapPath())
            .append("buildMapStatus", getBuildMapStatus())
            .append("createBy", getCreateBy())
            .append("createTime", getCreateTime())
            .append("updateBy", getUpdateBy())
            .append("updateTime", getUpdateTime())
            .append("remark", getRemark())
            .toString();
    }
}
