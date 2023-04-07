import request from '@/utils/request'

// 查询车辆统计量
export function digitalScreenStastatisticalNum() {
  return request({
    url: '/vehicledriving/digital/statistical-magnitude',
    method: 'get'
  })
}


// 查询车辆统计详情
export function digitalScreenProcessingData() {
  return request({
    url: '/vehicledriving/digital/statistical-processing-data',
    method: 'get'
  })
}


// 查询车辆地图统计详情
export function digitalScreenStatisticalMapNum() {
  return request({
    url: '/vehicledriving/digital/statistical-map-num',
    method: 'get'
  })
}