import request from '@/utils/request'

// 查询车辆驾驶行为数据列表
export function listVehicledrivingdata(query) {
  return request({
    url: '/vehicledrivingdata/vehicledrivingdata/list',
    method: 'get',
    params: query
  })
}

// 查询车辆驾驶行为数据详细
export function getVehicledrivingdata(vehicleDataId) {
  return request({
    url: '/vehicledrivingdata/vehicledrivingdata/' + vehicleDataId,
    method: 'get'
  })
}

// 新增车辆驾驶行为数据
export function addVehicledrivingdata(data) {
  return request({
    url: '/vehicledrivingdata/vehicledrivingdata',
    method: 'post',
    data: data
  })
}

// 修改车辆驾驶行为数据
export function updateVehicledrivingdata(data) {
  return request({
    url: '/vehicledrivingdata/vehicledrivingdata',
    method: 'put',
    data: data
  })
}

// 预处理车辆驾驶行为数据
export function preprocessingVehicledrivingdata(data) {
  return request({
    url: '/vehicledrivingdata/vehicledrivingdata/preprocessing',
    method: 'put',
    data: data
  })
}

// 统计车辆危险驾驶行为数据
export function statisticsVehicledrivingdata(data) {
  return request({
    url: '/vehicledrivingdata/vehicledrivingdata/statistics',
    method: 'put',
    data: data
  })
}

// 删除车辆驾驶行为数据
export function delVehicledrivingdata(vehicleDataId) {
  return request({
    url: '/vehicledrivingdata/vehicledrivingdata/' + vehicleDataId,
    method: 'delete'
  })
}
