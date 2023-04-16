package com.vdsa.vehicledrivingdata.domain;

import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;
import com.vdsa.common.annotation.Excel;
import com.vdsa.common.core.domain.BaseEntity;

/**
 * 车辆驾驶行为得分对象 vehicle_driving_behavior_score
 *
 * @author ruoyi
 * @date 2023-04-15
 */
public class VehicleDrivingBehaviorScore extends BaseEntity
{
    private static final long serialVersionUID = 1L;

    /** 主键 */
    private Long id;

    /** 对应驾驶数据id */
    @Excel(name = "对应驾驶数据id")
    private Long vehicleDataId;

    /** 评价生成状态(0未处理 1处理中 2处理完成) */
    @Excel(name = "评价生成状态(0未处理 1处理中 2处理完成)")
    private Long scoringStatus;

    /** 安全模型得分 */
    @Excel(name = "安全模型得分")
    private Long securityModelScore;

    /** 节能模型得分 */
    @Excel(name = "节能模型得分")
    private Long energySavingModelScore;

    /** 综合模型评分 */
    @Excel(name = "综合模型评分")
    private Long compositeModelScore;

    /** 综合评价 */
    @Excel(name = "综合评价")
    private Long comprehensiveAssessment;

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
    public void setScoringStatus(Long scoringStatus)
    {
        this.scoringStatus = scoringStatus;
    }

    public Long getScoringStatus()
    {
        return scoringStatus;
    }
    public void setSecurityModelScore(Long securityModelScore)
    {
        this.securityModelScore = securityModelScore;
    }

    public Long getSecurityModelScore()
    {
        return securityModelScore;
    }
    public void setEnergySavingModelScore(Long energySavingModelScore)
    {
        this.energySavingModelScore = energySavingModelScore;
    }

    public Long getEnergySavingModelScore()
    {
        return energySavingModelScore;
    }
    public void setCompositeModelScore(Long compositeModelScore)
    {
        this.compositeModelScore = compositeModelScore;
    }

    public Long getCompositeModelScore()
    {
        return compositeModelScore;
    }
    public void setComprehensiveAssessment(Long comprehensiveAssessment)
    {
        this.comprehensiveAssessment = comprehensiveAssessment;
    }

    public Long getComprehensiveAssessment()
    {
        return comprehensiveAssessment;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this,ToStringStyle.MULTI_LINE_STYLE)
                .append("id", getId())
                .append("vehicleDataId", getVehicleDataId())
                .append("scoringStatus", getScoringStatus())
                .append("securityModelScore", getSecurityModelScore())
                .append("energySavingModelScore", getEnergySavingModelScore())
                .append("compositeModelScore", getCompositeModelScore())
                .append("comprehensiveAssessment", getComprehensiveAssessment())
                .append("createBy", getCreateBy())
                .append("createTime", getCreateTime())
                .append("updateBy", getUpdateBy())
                .append("updateTime", getUpdateTime())
                .append("remark", getRemark())
                .toString();
    }
}
