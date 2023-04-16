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
    @Excel(name = "排序id")
    private Long vehicleDataId;

    /** 对应用户id */
    @Excel(name = "对应用户id")
    private Long userId;

    /** 文件上传地址 */
    @Excel(name = "文件上传地址")
    private String dataPath;

    /** 总里程 */
    @Excel(name = "总里程")
    private Long totalDistance;

    /** 实际驾驶时间 */
    @Excel(name = "实际驾驶时间")
    private Long drivingTime;

    /** 平均驾驶速度 */
    @Excel(name = "平均驾驶速度")
    private Long meanSpeed;

    /** 车速方差 */
    @Excel(name = "车速方差")
    private Long speedStd;

    /** 急加速次数 */
    @Excel(name = "急加速次数")
    private Long rapidAccNumbers;

    /** 急加速时长 */
    @Excel(name = "急加速时长")
    private Long rapidAccDuration;

    /** 急减速次数 */
    @Excel(name = "急减速次数")
    private Long rapidDecNumbers;

    /** 急减速时长 */
    @Excel(name = "急减速时长")
    private Long rapidDecDuration;

    /** 熄火滑行次数 */
    @Excel(name = "熄火滑行次数")
    private Long slideFrameoutNumbers;

    /** 熄火滑行时长 */
    @Excel(name = "熄火滑行时长")
    private Long slideFrameoutDuration;

    /** 超速次数 */
    @Excel(name = "超速次数")
    private Long overspeedNumbers;

    /** 超速时长 */
    @Excel(name = "超速时长")
    private Long overspeedDuration;

    /** 疲劳驾驶次数 */
    @Excel(name = "疲劳驾驶次数")
    private Long fatiguedrivingNumbers;

    /** 疲劳驾驶时长 */
    @Excel(name = "疲劳驾驶时长")
    private Long fatiguedrivingHours;

    /** 急转弯次数 */
    @Excel(name = "急转弯次数")
    private Long suddenturnNumbers;

    /** 怠速预热次数 */
    @Excel(name = "怠速预热次数")
    private Long idlePreheatingNumbers;

    /** 怠速预热时长 */
    @Excel(name = "怠速预热时长")
    private Long idlePreheatingMins;

    /** 超长怠速次数 */
    @Excel(name = "超长怠速次数")
    private Long overlongIdleNumbers;

    /** 超长怠速时长 */
    @Excel(name = "超长怠速时长")
    private Long overlongIdleMins;

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
    public void setTotalDistance(Long totalDistance)
    {
        this.totalDistance = totalDistance;
    }

    public Long getTotalDistance()
    {
        return totalDistance;
    }
    public void setDrivingTime(Long drivingTime)
    {
        this.drivingTime = drivingTime;
    }

    public Long getDrivingTime()
    {
        return drivingTime;
    }
    public void setMeanSpeed(Long meanSpeed)
    {
        this.meanSpeed = meanSpeed;
    }

    public Long getMeanSpeed()
    {
        return meanSpeed;
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
    public void setRapidAccDuration(Long rapidAccDuration)
    {
        this.rapidAccDuration = rapidAccDuration;
    }

    public Long getRapidAccDuration()
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
    public void setRapidDecDuration(Long rapidDecDuration)
    {
        this.rapidDecDuration = rapidDecDuration;
    }

    public Long getRapidDecDuration()
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
    public void setSlideFrameoutDuration(Long slideFrameoutDuration)
    {
        this.slideFrameoutDuration = slideFrameoutDuration;
    }

    public Long getSlideFrameoutDuration()
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
    public void setOverspeedDuration(Long overspeedDuration)
    {
        this.overspeedDuration = overspeedDuration;
    }

    public Long getOverspeedDuration()
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
    public void setFatiguedrivingHours(Long fatiguedrivingHours)
    {
        this.fatiguedrivingHours = fatiguedrivingHours;
    }

    public Long getFatiguedrivingHours()
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
    public void setIdlePreheatingMins(Long idlePreheatingMins)
    {
        this.idlePreheatingMins = idlePreheatingMins;
    }

    public Long getIdlePreheatingMins()
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
    public void setOverlongIdleMins(Long overlongIdleMins)
    {
        this.overlongIdleMins = overlongIdleMins;
    }

    public Long getOverlongIdleMins()
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
                .append("totalDistance", getTotalDistance())
                .append("drivingTime", getDrivingTime())
                .append("meanSpeed", getMeanSpeed())
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
