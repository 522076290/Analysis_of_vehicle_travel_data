package com.vdsa.vehicledrivingdata.domain;

import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;
import com.vdsa.common.annotation.Excel;
import com.vdsa.common.core.domain.BaseEntity;

/**
 * 车辆驾驶行为数据对象 vehicle_driving_data
 * 
 * @author lan
 * @date 2023-03-31
 */
public class VehicleDrivingData extends BaseEntity
{
    private static final long serialVersionUID = 1L;

    /** 车辆行驶数据编号 */
    private Long vehicleDataId;

    /** 对应用户id */
    @Excel(name = "对应用户id")
    private Long userId;

    /** 文件上传地址 */
    @Excel(name = "文件上传地址")
    private String dataPath;

    /** 车速方差 */
    @Excel(name = "车速方差")
    private Long speedStd;

    /** 急加速次数 */
    @Excel(name = "急加速次数")
    private Long rapidAccNumbers;

    /** 急加速时长 */
    @Excel(name = "急加速时长")
    private String rapidAccDuration;

    /** 急减速次数 */
    @Excel(name = "急减速次数")
    private Long rapidDecNumbers;

    /** 急减速时长 */
    @Excel(name = "急减速时长")
    private String rapidDecDuration;

    /** 熄火滑行次数 */
    @Excel(name = "熄火滑行次数")
    private Long slideFrameoutNumbers;

    /** 熄火滑行时长 */
    @Excel(name = "熄火滑行时长")
    private String slideFrameoutDuration;

    /** 超速次数 */
    @Excel(name = "超速次数")
    private Long overspeedNumbers;

    /** 超速时长 */
    @Excel(name = "超速时长")
    private String overspeedDuration;

    /** 疲劳驾驶次数 */
    @Excel(name = "疲劳驾驶次数")
    private Long fatiguedrivingNumbers;

    /** 疲劳驾驶时长 */
    @Excel(name = "疲劳驾驶时长")
    private String fatiguedrivingHours;

    /** 急转弯次数 */
    @Excel(name = "急转弯次数")
    private Long suddenturnNumbers;

    /** 怠速预热次数 */
    @Excel(name = "怠速预热次数")
    private Long idlePreheatingNumbers;

    /** 怠速预热时长 */
    @Excel(name = "怠速预热时长")
    private String idlePreheatingMins;

    /** 超长怠速次数 */
    @Excel(name = "超长怠速次数")
    private Long overlongIdleNumbers;

    /** 超长怠速时长 */
    @Excel(name = "超长怠速时长")
    private String overlongIdleMins;

    /** 预处理状态(0未处理 1处理中 2处理完成) */
    @Excel(name = "预处理状态(0未处理 1处理中 2处理完成)")
    private Long preprocessingState;

    /** 统计状态(0未处理 1处理中 2处理完成) */
    @Excel(name = "统计状态(0未处理 1处理中 2处理完成)")
    private Long statisticalState;

    public void setVehicleDataId(Long vehicleDataId)
    {
        this.vehicleDataId = vehicleDataId;
    }

    public Long getVehicleDataId()
    {
        return vehicleDataId;
    }
    public void setUserId(Long userId)
    {
        this.userId = userId;
    }

    public Long getUserId()
    {
        return userId;
    }
    public void setDataPath(String dataPath)
    {
        this.dataPath = dataPath;
    }

    public String getDataPath()
    {
        return dataPath;
    }
    public void setSpeedStd(Long speedStd)
    {
        this.speedStd = speedStd;
    }

    public Long getSpeedStd()
    {
        return speedStd;
    }
    public void setRapidAccNumbers(Long rapidAccNumbers)
    {
        this.rapidAccNumbers = rapidAccNumbers;
    }

    public Long getRapidAccNumbers()
    {
        return rapidAccNumbers;
    }
    public void setRapidAccDuration(String rapidAccDuration)
    {
        this.rapidAccDuration = rapidAccDuration;
    }

    public String getRapidAccDuration()
    {
        return rapidAccDuration;
    }
    public void setRapidDecNumbers(Long rapidDecNumbers)
    {
        this.rapidDecNumbers = rapidDecNumbers;
    }

    public Long getRapidDecNumbers()
    {
        return rapidDecNumbers;
    }
    public void setRapidDecDuration(String rapidDecDuration)
    {
        this.rapidDecDuration = rapidDecDuration;
    }

    public String getRapidDecDuration()
    {
        return rapidDecDuration;
    }
    public void setSlideFrameoutNumbers(Long slideFrameoutNumbers)
    {
        this.slideFrameoutNumbers = slideFrameoutNumbers;
    }

    public Long getSlideFrameoutNumbers()
    {
        return slideFrameoutNumbers;
    }
    public void setSlideFrameoutDuration(String slideFrameoutDuration)
    {
        this.slideFrameoutDuration = slideFrameoutDuration;
    }

    public String getSlideFrameoutDuration()
    {
        return slideFrameoutDuration;
    }
    public void setOverspeedNumbers(Long overspeedNumbers)
    {
        this.overspeedNumbers = overspeedNumbers;
    }

    public Long getOverspeedNumbers()
    {
        return overspeedNumbers;
    }
    public void setOverspeedDuration(String overspeedDuration)
    {
        this.overspeedDuration = overspeedDuration;
    }

    public String getOverspeedDuration()
    {
        return overspeedDuration;
    }
    public void setFatiguedrivingNumbers(Long fatiguedrivingNumbers)
    {
        this.fatiguedrivingNumbers = fatiguedrivingNumbers;
    }

    public Long getFatiguedrivingNumbers()
    {
        return fatiguedrivingNumbers;
    }
    public void setFatiguedrivingHours(String fatiguedrivingHours)
    {
        this.fatiguedrivingHours = fatiguedrivingHours;
    }

    public String getFatiguedrivingHours()
    {
        return fatiguedrivingHours;
    }
    public void setSuddenturnNumbers(Long suddenturnNumbers)
    {
        this.suddenturnNumbers = suddenturnNumbers;
    }

    public Long getSuddenturnNumbers()
    {
        return suddenturnNumbers;
    }
    public void setIdlePreheatingNumbers(Long idlePreheatingNumbers)
    {
        this.idlePreheatingNumbers = idlePreheatingNumbers;
    }

    public Long getIdlePreheatingNumbers()
    {
        return idlePreheatingNumbers;
    }
    public void setIdlePreheatingMins(String idlePreheatingMins)
    {
        this.idlePreheatingMins = idlePreheatingMins;
    }

    public String getIdlePreheatingMins()
    {
        return idlePreheatingMins;
    }
    public void setOverlongIdleNumbers(Long overlongIdleNumbers)
    {
        this.overlongIdleNumbers = overlongIdleNumbers;
    }

    public Long getOverlongIdleNumbers()
    {
        return overlongIdleNumbers;
    }
    public void setOverlongIdleMins(String overlongIdleMins)
    {
        this.overlongIdleMins = overlongIdleMins;
    }

    public String getOverlongIdleMins()
    {
        return overlongIdleMins;
    }
    public void setPreprocessingState(Long preprocessingState)
    {
        this.preprocessingState = preprocessingState;
    }

    public Long getPreprocessingState()
    {
        return preprocessingState;
    }
    public void setStatisticalState(Long statisticalState)
    {
        this.statisticalState = statisticalState;
    }

    public Long getStatisticalState()
    {
        return statisticalState;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this,ToStringStyle.MULTI_LINE_STYLE)
                .append("vehicleDataId", getVehicleDataId())
                .append("userId", getUserId())
                .append("dataPath", getDataPath())
                .append("speedStd", getSpeedStd())
                .append("rapidAccNumbers", getRapidAccNumbers())
                .append("rapidAccDuration", getRapidAccDuration())
                .append("rapidDecNumbers", getRapidDecNumbers())
                .append("rapidDecDuration", getRapidDecDuration())
                .append("slideFrameoutNumbers", getSlideFrameoutNumbers())
                .append("slideFrameoutDuration", getSlideFrameoutDuration())
                .append("overspeedNumbers", getOverspeedNumbers())
                .append("overspeedDuration", getOverspeedDuration())
                .append("fatiguedrivingNumbers", getFatiguedrivingNumbers())
                .append("fatiguedrivingHours", getFatiguedrivingHours())
                .append("suddenturnNumbers", getSuddenturnNumbers())
                .append("idlePreheatingNumbers", getIdlePreheatingNumbers())
                .append("idlePreheatingMins", getIdlePreheatingMins())
                .append("overlongIdleNumbers", getOverlongIdleNumbers())
                .append("overlongIdleMins", getOverlongIdleMins())
                .append("preprocessingState", getPreprocessingState())
                .append("statisticalState", getStatisticalState())
                .toString();
    }
}
