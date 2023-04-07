package com.vdsa.vehicledrivingdata.domain;

/**
 * 地图数据统计响应
 * @author lan
 * @version 1.0
 * @data 2023/4/6 9:24
 */
public class VehicleDigitalScreenMapNumResp {

    /**车辆id*/
    private Long id;

    /**已统计地图数量*/
    private Integer statisticsMapNum;

    /**未统计地图数量*/
    private Integer uncountedNum;


    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Integer getStatisticsMapNum() {
        return statisticsMapNum;
    }

    public void setStatisticsMapNum(Integer statisticsMapNum) {
        this.statisticsMapNum = statisticsMapNum;
    }

    public Integer getUncountedNum() {
        return uncountedNum;
    }

    public void setUncountedNum(Integer uncountedNum) {
        this.uncountedNum = uncountedNum;
    }


    @Override
    public String toString() {
        return "VehicleDigitalScreenMapNumResp{" +
                "id=" + id +
                ", statisticsMapNum=" + statisticsMapNum +
                ", uncountedNum=" + uncountedNum +
                '}';
    }
}
