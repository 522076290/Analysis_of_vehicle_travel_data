package com.vdsa.vehicledrivingdata.domain;

/**
 * 数字大屏响应 domain
 * @author lan
 * @version 1.0
 * @data 2023/4/5 16:48
 */
public class VehicleDigitalScreenResp {

    /**当日统计数量*/
    private Integer todayStatisticsNumbers;

    /**总共统计数量*/
    private Integer AllStatisticsNumbers;

    /**正在统计的数量*/
    private Integer NowStatisticsNumbers;

    /**已危险统计的数据*/
    private Integer ThroughStatisticalRiskData;

    /**未危险统计的数据*/
    private Integer UncountedRiskData;

    /**通过预处理的数据*/
    private Integer ThroughPreprocessingData;

    /**未通过预处理的数据*/
    private Integer UncountedPreprocessingData;



    public Integer getTodayStatisticsNumbers() {
        return todayStatisticsNumbers;
    }

    public void setTodayStatisticsNumbers(Integer todayStatisticsNumbers) {
        this.todayStatisticsNumbers = todayStatisticsNumbers;
    }

    public Integer getAllStatisticsNumbers() {
        return AllStatisticsNumbers;
    }

    public void setAllStatisticsNumbers(Integer allStatisticsNumbers) {
        AllStatisticsNumbers = allStatisticsNumbers;
    }

    public Integer getNowStatisticsNumbers() {
        return NowStatisticsNumbers;
    }

    public void setNowStatisticsNumbers(Integer nowStatisticsNumbers) {
        NowStatisticsNumbers = nowStatisticsNumbers;
    }

    public Integer getThroughStatisticalRiskData() {
        return ThroughStatisticalRiskData;
    }

    public void setThroughStatisticalRiskData(Integer throughStatisticalRiskData) {
        ThroughStatisticalRiskData = throughStatisticalRiskData;
    }

    public Integer getUncountedRiskData() {
        return UncountedRiskData;
    }

    public void setUncountedRiskData(Integer uncountedRiskData) {
        UncountedRiskData = uncountedRiskData;
    }

    public Integer getThroughPreprocessingData() {
        return ThroughPreprocessingData;
    }

    public void setThroughPreprocessingData(Integer throughPreprocessingData) {
        ThroughPreprocessingData = throughPreprocessingData;
    }

    public Integer getUncountedPreprocessingData() {
        return UncountedPreprocessingData;
    }

    public void setUncountedPreprocessingData(Integer uncountedPreprocessingData) {
        UncountedPreprocessingData = uncountedPreprocessingData;
    }

    @Override
    public String toString() {
        return "VehicleDigitalScreenResp{" +
                "todayStatisticsNumbers=" + todayStatisticsNumbers +
                ", AllStatisticsNumbers=" + AllStatisticsNumbers +
                ", NowStatisticsNumbers=" + NowStatisticsNumbers +
                ", ThroughStatisticalRiskData=" + ThroughStatisticalRiskData +
                ", UncountedRiskData=" + UncountedRiskData +
                ", ThroughPreprocessingData=" + ThroughPreprocessingData +
                ", UncountedPreprocessingData=" + UncountedPreprocessingData +
                '}';
    }
}
